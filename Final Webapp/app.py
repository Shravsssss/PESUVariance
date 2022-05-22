#app.py
from flask import Flask, request, session, redirect, url_for, render_template, flash, jsonify
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
from werkzeug.security import generate_password_hash, check_password_hash
 
app = Flask(__name__)
app.secret_key = 'cairocoders-ednalan'

DB_HOST = "localhost"
DB_NAME = "pesuvariance"
DB_USER = "postgres"
DB_PASS = "postgres"
 
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()


@app.route('/')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
    
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))
 
@app.route('/login/', methods=['GET', 'POST'])
def login():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print(password)
 
        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM user_profile WHERE user_id = %s', (username,))
        # Fetch one record and return result
        account = cursor.fetchone()
 
        if account:
            password_rs = account['password']
            print(password_rs)
            # If account exists in users table in out database
            if (password_rs == password):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['user_id']
                session['username'] = account['name']
                # Redirect to home page
                return redirect(url_for('home'))
            else:
                # Account doesnt exist or username/password incorrect
                flash('Incorrect username/password')
        else:
            # Account doesnt exist or username/password incorrect
            flash('Incorrect username/password')
 
    return render_template('login.html')
  
@app.route('/register', methods=['GET', 'POST'])
def register():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
 
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        type1=request.form['type']
        dob=request.form['dob']
        coco=request.form['coco']
        num=request.form['num']
    
        #_hashed_password = generate_password_hash(password)
 
        #Check if account exists using PSQL
        cursor.execute('SELECT * FROM user_profile WHERE user_id = %s', (username,))
        account = cursor.fetchone()
        print(account)
        # If account exists show error and validation checks
        if account:
            flash('Account already exists!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!')
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('Username must contain only characters and numbers!')
        elif not username or not password or not email:
            flash('Please fill out the form!')
        else:
            # Account doesnt exists and the form data is valid, now insert new account into users table
            cursor.execute("INSERT INTO user_profile (user_id, name, emailid,type,dob,country_code,number,password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)", (username,fullname,email,type1,dob,coco,num,password))
            conn.commit()
            flash('You have successfully registered!')
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        flash('Please fill out the form!')
    # Show registration form with message (if any)
    return render_template('register.html')
   
   
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))

@app.route('/competitions',methods=['GET', 'POST'])
def compete():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if 'loggedin' in session:

        cursor.execute('SELECT * FROM user_profile WHERE user_id = %s;', (session['id'],))
        account=cursor.fetchone()
        cursor.execute('SELECT * FROM competitions;')
        data=cursor.fetchall()
        if request.method=='POST':
            value=request.form['comp_id']
            print(value)
            cursor.execute("INSERT INTO participated_by (pb_userid, pb_competitionid, participationid) VALUES (%s,%s,%s)", (session['id'],value,11))
            conn.commit()
            return render_template('home.html')

        else:
             return render_template('competitions.html',account=account,data=data)
    else:
        return render_template('home.html')

@app.route('/profile')
def profile(): 
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
    # Check if user is loggedin
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM user_profile WHERE user_id = %s', (session['id'],))
        # print(session['id'], session['username'])
        account = cursor.fetchone()
        # Show the profile page with account info
        return render_template('profile.html', account=account)
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))
 
@app.route('/quizmain', endpoint = 'quizmain')
def quizmain():
    cur.execute('''SELECT DISTINCT Quiz_Name FROM quiz ORDER BY Quiz_Name ASC;''')
    rows = cur.fetchall()
    my_list = []
    for row in rows:
        my_list.append(row[0])
    return render_template('quizmain.html', results=my_list)
    
    
@app.route('/quiz', methods = ["GET", "POST"], endpoint = 'quiz')
def quiz():
    #layout = request.args.get('layout')
    #if request.method == "POST":
    #    data = request.get_json(silent=True)
    #    print(data)
    #    print(jsonify(data))
    #else:
    #print(layout)
    cur.execute('''SELECT Question_Desc, A_Answer_1, A_Answer_2, A_Answer_3, A_Answer_Key FROM QUESTIONS FULL OUTER JOIN QUIZ ON Q_Quiz_ID = Quiz_ID FULL OUTER JOIN ANSWERS ON A_Question_ID = Question_ID WHERE Quiz_Name = 'Statistics' AND Question_Desc IS NOT NULL;''')
    rows = cur.fetchall()
    my_list = []
    for q,a1,a2,a3,key in rows:
        my_list.append([q,a1,a2,a3,key])
    return render_template('quiz.html', result = my_list)
 
 
if __name__ == "__main__":
    app.run(debug=True)
import os
import psycopg2
from flask import Flask, render_template, redirect
from urllib.parse import urlparse, urlunparse
#import urlparse
from os.path import exists
from os import makedirs

#url = urlparse.urlparse(os.environ.get('DATABASE_URL'))
#db = "dbname=%s user=%s password=%s host=%s " % (url.path[1:], url.username, url.password, url.hostname)

#schema = "schema.sql"
conn = psycopg2.connect(host ="localhost", database = "pesuvariance", user = "postgres", password = "postgres")
#conn = psycopg2.connect(db)

cur = conn.cursor()

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/quizmain', endpoint = 'quizmain')
def quizmain():
    cur.execute('''SELECT DISTINCT Quiz_Name FROM quiz ORDER BY Quiz_Name ASC;''')
    rows = cur.fetchall()
    my_list = []
    for row in rows:
        my_list.append(row[0])
    return render_template('quizmain.html', results=my_list)
    
    
@app.route('/quiz', endpoint = 'quiz')
def quiz():
    cur.execute('''SELECT Question_Desc, A_Answer_1, A_Answer_2, A_Answer_3, A_Answer_Key FROM QUESTIONS FULL OUTER JOIN QUIZ ON Q_Quiz_ID = Quiz_ID FULL OUTER JOIN ANSWERS ON A_Question_ID = Question_ID WHERE Quiz_Name = 'Statistics' AND Question_Desc IS NOT NULL;''')
    rows = cur.fetchall()
    my_list = []
    for q,a1,a2,a3,key in rows:
        my_list.append({'question': q, 'optionA': a1, 'optionB': a2, 'optionC': a3, 'correctOption': key})
    return render_template('quiz.html', results=my_list)    


@app.route('/homepage')
def homepage():
    """try:
        cur.execute('''SELECT name from salesforce.contact''')
        rows = cur.fetchall()
        response = ''
        my_list = []
        for row in rows:
            my_list.append(row[0])

        return render_template('template.html',  results=my_list)
    except Exception as e:
        print(e)
    return []"""
    return 'Hello world'

if __name__ == '__main__':
    app.run()
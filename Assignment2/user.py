#!/usr/bin/python
import psycopg2

def write(User_ID, Name, EmailID, Type, Bio, ActivityPath, ImagePath, DOB, Country_Code, Number, Password,):
    conn = None
    try:

        conn = psycopg2.connect(host ="localhost", database = "pesuvariance", user = "postgres", password = "YOUR PASSWORD")

        cur = conn.cursor()
        
        #for i in range(1,8):
         #   act = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/UserActivity%s.txt" % i, 'r').read()

        #   pic = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/image%s.jpg" % i,'rb').read()
        
        act = open(ActivityPath, 'r').read()

        pic = open(ImagePath,'rb').read()
            
        cur.execute("INSERT INTO USER_PROFILE(User_ID, Name, EmailID, Type, Bio, Profile_Picture, Activity, DOB, Country_Code, Number, Password)" + "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (User_ID, Name, EmailID, Type, Bio, psycopg2.Binary(pic), act, DOB, Country_Code, Number, Password))
            
        
        #cur.execute("INSERT INTO USER_PROFILE(User_ID, Name, EmailID, Type, Bio, Profile_Picture, Activity, DOB, Country_Code, Number, Password)" + "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (User_ID, Name, EmailID, Type, Bio, psycopg2.Binary(pic), '', DOB, Country_Code, Number, Password))

        conn.commit()
        print("data inserted successfullly")

        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


write('S3','yousha', 'yousha@gmail.com', 'Student', 'Hi', "C:/Users/Sravya Yepuri/Desktop/PESUVariance/UserActivity1.txt", "C:/Users/Sravya Yepuri/Desktop/PESUVariance/image1.jpg", '1991-09-12', 80, 12345, 'xyz123')
write('S4', 'sravya', 'sravya@gmail.com', 'Student', 'Hello', "C:/Users/Sravya Yepuri/Desktop/PESUVariance/UserActivity2.txt", "C:/Users/Sravya Yepuri/Desktop/PESUVariance/image2.jpg", '2001-09-12',80,762353,'xyz123')
write('I1','shrikar', 'shrikar@gmail.com', 'Student', 'Hey', "C:/Users/Sravya Yepuri/Desktop/PESUVariance/UserActivity3.txt", "C:/Users/Sravya Yepuri/Desktop/PESUVariance/image3.jpg", '1999-09-12',80,12382,'xyz123')
write('S2','ramya', 'ramya@gmail.com', 'Student', '', "C:/Users/Sravya Yepuri/Desktop/PESUVariance/UserActivity4.txt", "C:/Users/Sravya Yepuri/Desktop/PESUVariance/image4.jpg", '1991-09-12',80, 12332123,'xyz123')
write('I3','anjali', 'anjali@gmail.com', 'Instructor', 'Hi', "C:/Users/Sravya Yepuri/Desktop/PESUVariance/UserActivity5.txt", "C:/Users/Sravya Yepuri/Desktop/PESUVariance/image5.jpg", '2001-09-12',80,123456, 'xyz123')
write('I2','kruthika', 'kruthika@gmail.com', 'Instructor' , 'Hi', "C:/Users/Sravya Yepuri/Desktop/PESUVariance/UserActivity6.txt", "C:/Users/Sravya Yepuri/Desktop/PESUVariance/image6.jpg", '1998-09-12',80,1234567,'xyz123')
write('I4','anchala', 'anchala@gmail.com', 'Instructor', 'Hi', "C:/Users/Sravya Yepuri/Desktop/PESUVariance/UserActivity7.txt", "C:/Users/Sravya Yepuri/Desktop/PESUVariance/image7.jpg", '1995-09-12', 80, 273642, 'xyz123')
write('S1','srushti', 'srushti@gmail.com', 'Instructor', 'Hi', "C:/Users/Sravya Yepuri/Desktop/PESUVariance/UserActivity8.txt", "C:/Users/Sravya Yepuri/Desktop/PESUVariance/image8.jpg", '1999-09-12', 80, 1234323, 'xyz123')




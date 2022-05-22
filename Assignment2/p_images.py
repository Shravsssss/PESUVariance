#!/usr/bin/python
import psycopg2

def P_images(PI_postID):
    conn = None
    try:

        conn = psycopg2.connect(host ="localhost", database = "pesuvariance", user = "postgres", password = "YOUR PASSWORD")

        cur = conn.cursor()
        
        pic = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/pi%s.jpg" % PI_postID,'rb').read()
            
        cur.execute("INSERT INTO P_IMAGES(PI_postID, PI_Image)" + "VALUES(%s, %s)", (PI_postID, psycopg2.Binary(pic)))
        conn.commit()
        print("data inserted successfullly")

        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
P_images('1')
P_images('2')
P_images('3')
P_images('4')
P_images('5')
P_images('6')
P_images('7')
P_images('8')

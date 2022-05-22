#!/usr/bin/python
import psycopg2

def c_images(C_CompID):
    conn = None
    try:

        conn = psycopg2.connect(host ="localhost", database = "pesuvariance", user = "postgres", password = "YOUR PASSWORD")

        cur = conn.cursor()
        
        pic = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/ci%s.jpg" % C_CompID[1],'rb').read()
            
        cur.execute("INSERT INTO C_IMAGES(C_CompID, C_Image)" + "VALUES(%s, %s)", (C_CompID, psycopg2.Binary(pic)))
        conn.commit()
        print("data inserted successfullly")

        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
c_images('C1')
c_images('C2')
c_images('C3')
c_images('C4')
c_images('C5')
c_images('C6')
c_images('C7')
c_images('C8')

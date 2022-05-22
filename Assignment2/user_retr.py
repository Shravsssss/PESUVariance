#!/usr/bin/python
import psycopg2

def read():
    
    conn = psycopg2.connect(host ="localhost", database = "pesuvariance", user = "postgres", password = "YOUR PASSWORD")
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM USER_PROFILE;")
    
    record = cur.fetchone()
    
    open("C:\\Users\\Sravya Yepuri\\Desktop\\PESUVariance\\result_image.jpg", 'wb').write(record[5])
    
    cur.execute("SELECT * FROM USER_PROFILE;")
    
    f = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/UserActivity1_data.txt", 'w')

    for r in cur.fetchall():
        f.write(r[6])
    
    cur.close()
    
read()
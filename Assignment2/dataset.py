#!/usr/bin/python
import psycopg2
import os

def dataset(Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, Dateset_Date, Dataset_Time, dataset):
    conn = None
    try:
    
        conn = psycopg2.connect(host ="localhost", database = "pesuvariance", user = "postgres", password = "postgres")

        cur = conn.cursor()
        
        #for i in range(1,8):
        data = open(dataset, 'r').read()
        size = os.path.getsize(dataset);
            
        cur.execute("INSERT INTO DATASET (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, File, Size, Dateset_Date, Dataset_Time)" + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, data, size, Dateset_Date, Dataset_Time))
            
        cur.execute("SELECT * FROM DATASET;")

        f = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/result_Dataset_data.txt", 'w')

        for r in cur.fetchall():
            f.write(r[5])

        conn.commit()
        print("data inserted successfullly")

        cur.close()
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            

dataset('D1','S1','Covid-19','CC0: Public Domain','','2021-08-09','08:25:30',"C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset1.csv")
dataset('D2','S2','Stock Market','Apple','Stock Market Data','2021-03-01','08:45:10',"C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset2.csv")
dataset('D3','S1','Dengue Data Philippines','CC0: Public Domain','','2020-09-02','03:55:14',"C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset3.csv")
dataset('D4','S3','Housing Prices Dataset','UCLA','','2021-01-04','09:05:19',"C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset4.csv")
dataset('D5','S4','Company Acquisitions Data','Kaggle Source','','2019-05-19','12:20:12',"C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset5.csv")
dataset('D6','I1','Fuel Poverty','Cambridgeshire Research Group','The data includes estimates at lower super output area (LSOA) of households subject to high energy costs and low income (since 2011) and of households spending 10% or more of their income on fuel, for 2008 to 2012. All the data comes from DECC.','2021-09-13','13:45:39',"C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset6.csv")
dataset('D7','I2','GDP Data in USA','CC0: Public Domain','The purpose of this data set is to allow exploration between various types of data that is commonly collected by the US government across the states and the USA as a whole.','2020-10-29','06:15:31',"C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset7.csv")
dataset('D8','I3','Mental Health','CC BY-SA 4.0','This dataset is from a 2014 survey that measures attitudes towards mental health and frequency of mental health disorders in the tech workplace. ','2021-12-09','08:05:35',"C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset8.csv")



        
        #dataset2 = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset2.csv", 'r').read()
        #size2 = os.path.getsize("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset2.csv");
        
        #dataset3 = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset2.csv", 'r').read()
        #size3 = os.path.getsize("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset3.csv");
        
        #dataset4 = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset2.csv", 'r').read()
        #size4 = os.path.getsize("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset3.csv");        
        
        #dataset5 = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset2.csv", 'r').read()
        #size5 = os.path.getsize("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset3.csv");

        #dataset6 = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset2.csv", 'r').read()
        #size6 = os.path.getsize("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset3.csv");

        #dataset7 = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset2.csv", 'r').read()
        #size7 = os.path.getsize("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset3.csv");

        #dataset8 = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset2.csv", 'r').read()
        #size8 = os.path.getsize("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/dataset3.csv");


        #cur.execute("INSERT INTO DATASET (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, File, Size, Dateset_Date, Dataset_Time)" + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, dataset1, size1, Dateset_Date, Dataset_Time))
        
        #cur.execute("INSERT INTO DATASET (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, File, Size, Dateset_Date, Dataset_Time)" + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, dataset2, size2, Dateset_Date, Dataset_Time))
        
        #cur.execute("INSERT INTO DATASET (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, File, Size, Dateset_Date, Dataset_Time)" + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, dataset3, size3, Dateset_Date, Dataset_Time))
        
        #cur.execute("INSERT INTO DATASET (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, File, Size, Dateset_Date, Dataset_Time)" + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, dataset4, size4, Dateset_Date, Dataset_Time))
        
        #cur.execute("INSERT INTO DATASET (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, File, Size, Dateset_Date, Dataset_Time)" + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, dataset5, size5, Dateset_Date, Dataset_Time))

        #cur.execute("INSERT INTO DATASET (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, File, Size, Dateset_Date, Dataset_Time)" + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, dataset6, size6, Dateset_Date, Dataset_Time))

        #cur.execute("INSERT INTO DATASET (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, File, Size, Dateset_Date, Dataset_Time)" + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, dataset7, size7, Dateset_Date, Dataset_Time))

        #cur.execute("INSERT INTO DATASET (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, File, Size, Dateset_Date, Dataset_Time)" + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (Dataset_ID, Dataset_UserID, Dataset_Name, Dataset_Owner, Description, dataset8, size8, Dateset_Date, Dataset_Time))


        
        #cur.execute("SELECT * FROM DATASET;")

        #f = open("C:/Users/Sravya Yepuri/Desktop/PESUVariance/Assignment2/final/Dataset1_data.txt", 'w')

        #for r in cur.fetchall():
        #    f.write(r[6])
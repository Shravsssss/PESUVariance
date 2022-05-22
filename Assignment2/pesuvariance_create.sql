drop database pesuvariance;
create database pesuvariance;

\c pesuvariance;


CREATE TABLE USER_PROFILE (
User_ID VARCHAR(5) NOT NULL, 
Name VARCHAR(30) NOT NULL, 
EmailID VARCHAR(30) NOT NULL, 
Type VARCHAR(30) NOT NULL DEFAULT 'Student', 
Bio VARCHAR(60), 
Profile_Picture BYTEA,
Activity text DEFAULT NULL, 
DOB DATE NOT NULL CHECK (DOB BETWEEN '1960-01-01' AND '2004-01-01'), 
Country_Code INT NOT NULL, 
Number INT NOT NULL, 
Password VARCHAR(60) NOT NULL,
PRIMARY KEY (User_ID)) ;

CREATE TABLE LOGIN (
Login_ID VARCHAR(5) NOT NULL, 
Login_UserID VARCHAR(5) NOT NULL, 
Login_Username VARCHAR(30) NOT NULL, 
Login_Date DATE NOT NULL, 
Login_Time TIME NOT NULL, 
Login_Status VARCHAR(3) NOT NULL,
Password VARCHAR(60) NOT NULL,
UNIQUE (Login_Username),
PRIMARY KEY (Login_ID),
FOREIGN KEY (Login_UserID) REFERENCES USER_PROFILE(User_ID)) ;

CREATE TABLE DATASET (
Dataset_ID VARCHAR(5) NOT NULL, 
Dataset_UserID VARCHAR(5) NOT NULL, 
Dataset_Name VARCHAR(30) NOT NULL, 
Dataset_Owner VARCHAR(30) NOT NULL, 
Description VARCHAR(500), 
File TEXT NOT NULL, 
Size VARCHAR(10) NOT NULL, 
Dateset_Date DATE NOT NULL, 
Dataset_Time TIME NOT NULL,
PRIMARY KEY (Dataset_ID),
UNIQUE (Dataset_Name),
FOREIGN KEY (Dataset_UserID) REFERENCES USER_PROFILE(User_ID)) ;

CREATE TABLE DOWNLOADS (
Do_UserID VARCHAR(5) NOT NULL, 
Do_DatasetID VARCHAR(5) NOT NULL,
PRIMARY KEY (Do_UserID, Do_DatasetID),
FOREIGN KEY (Do_UserID) REFERENCES USER_PROFILE(User_ID),
FOREIGN KEY (Do_DatasetID) REFERENCES DATASET(Dataset_ID)) ;

CREATE TABLE QUIZ(
QUIZ_ID Varchar(5) NOT NULL,
Quiz_Name VARCHAR(10) NOT NULL,
No_Questions INT NOT NULL,
Complexity Varchar(10) DEFAULT 'Medium',
Quiz_date DATE NOT NULL DEFAULT CURRENT_DATE,
Quiz_time TIME NOT NULL,
Total_Score NUMERIC,
Primary Key(QUIZ_ID));

CREATE TABLE QUESTIONS(
Question_ID VARCHAR(5) NOT NULL,
Question_Desc Varchar(100) NOT NULL,
Q_Quiz_ID Varchar(5) NOT NULL,
PRIMARY KEY(Question_ID),
Foreign Key (Q_Quiz_ID) references QUIZ(QUIZ_ID));

CREATE TABLE ANSWERS(
A_Question_ID varchar(5) NOT NULL,
A_Answer_Key varchar(5) NOT NULL,
A_Answer_1 varchar (100) NOT NULL,
A_Answer_2 varchar (100) NOT NULL,
A_Answer_3 varchar (100) NOT NULL,
PRIMARY KEY(A_Question_ID), 
Foreign Key (A_Question_ID) references QUESTIONS(Question_ID));

CREATE TABLE COMPETITIONS(
C_Competition_id varchar(10) NOT NULL,
C_Competetion_name varchar(50) NOT NULL,
C_Requirements varchar(100) NOT NULL,
C_Description varchar(100) NOT NULL,
C_Rules varchar(100) NOT NULL,
C_Sponsors varchar(100),
C_No_of_entries INT,
C_Date DATE NOT NULL,
C_Time TIME NOT NULL,
C_Image BYTEA,
UNIQUE(C_Competition_id),
PRIMARY KEY(C_Competition_id));

CREATE TABLE LEADERBOARD(
L_Rank INT NOT NULL,
Submission_ID INT NOT NULL,
Execution_Speed FLOAT(3) NOT NULL,
Grade INT NOT NULL DEFAULT 0,
Test_Case_Passed INT NOT NULL DEFAULT 0,
L_CompetitionID VARCHAR(10) NOT NULL,
PRIMARY KEY (L_Rank),
UNIQUE (Submission_ID),
FOREIGN KEY (L_competitionID) REFERENCES COMPETITIONs(C_Competition_id));

CREATE TABLE POST(
Post_ID VARCHAR(5) NOT NULL,
Post_title VARCHAR(50) NOT NULL,
Post_desc VARCHAR(500) NOT NULL,
Post_owner VARCHAR(30) NOT NULL,
P_Date DATE NOT NULL,
P_Time TIME NOT NULL,
Upvotes INT DEFAULT 0,
P_userID VARCHAR(5) NOT NULL,
PRIMARY KEY (Post_ID),
FOREIGN KEY (P_userID) REFERENCES USER_PROFILE(User_ID));

CREATE TABLE COMMENT(
Comment_ID VARCHAR(5) NOT NULL,
Comment_desc VARCHAR(100) NOT NULL,
Comment_owner VARCHAR(30) NOT NULL,
Comment_Date DATE NOT NULL,
Comment_Time TIME NOT NULL,
C_userID VARCHAR(5) NOT NULL,
Superior_commentID VARCHAR(5) DEFAULT NULL,
C_postID VARCHAR(5) NOT NULL,
PRIMARY KEY(Comment_ID),
FOREIGN KEY(C_userID)  REFERENCES USER_PROFILE(User_ID),
FOREIGN KEY(Superior_commentID) REFERENCES COMMENT(Comment_ID),
FOREIGN KEY(C_postID) REFERENCES  POST(Post_ID));

CREATE TABLE HOSTED_BY(
hb_userID VARCHAR(5) NOT NULL,
hb_competitionID VARCHAR(5) NOT NULL,
PRIMARY KEY(hb_userID, hb_competitionID),
FOREIGN KEY(hb_userID) REFERENCES USER_PROFILE(User_ID),
FOREIGN KEY(hb_competitionID) REFERENCES competitions(C_Competition_id));

CREATE TABLE PARTICIPATED_BY(
pb_userID varchar(5) NOT NULL,
pb_competitionID varchar(5) NOT NULL,
participationID SERIAL NOT NULL,
PRIMARY KEY(pb_userID,pb_competitionID),
FOREIGN KEY(pb_userID) REFERENCES USER_PROFILE (User_ID),
FOREIGN KEY(pb_competitionID) REFERENCES COMPETITIONs(C_Competition_ID));

CREATE TABLE participates_in(
pb_userID varchar(5) NOT NULL,
pb_quizID varchar(5) NOT NULL,
PRIMARY KEY(pb_userID,pb_quizID),
FOREIGN KEY(pb_userID) references USER_PROFILE(User_ID),
FOREIGN KEY(pb_quizID) references Quiz(Quiz_ID));

CREATE TABLE Instructor(
I_QuizID varchar(5) NOT NULL,
Instructor_ID varchar(5) NOT NULL,
Primary Key(I_QuizID,Instructor_ID),
Foreign Key(I_QuizID) references Quiz(Quiz_ID),
Foreign Key(Instructor_ID) references USER_PROFILE(User_ID));

CREATE TABLE P_IMAGES(
PI_postID varchar(5) NOT NULL,
PI_Image BYTEA,
PRIMARY KEY(PI_postID,PI_IMAGE),
FOREIGN KEY(PI_PostID) references POST(Post_ID));

CREATE TABLE C_IMAGES(
C_CompID varchar(5) NOT NULL,
C_Image BYTEA,
PRIMARY KEY(C_CompID,C_image),
FOREIGN KEY(C_CompID) references Competitions(C_Competition_id));

CREATE TABLE C_Sponsors(
CS_CompID varchar(5) NOT NULL,
CS_Sponsors varchar(20) NOT NULL,
PRIMARY KEY(CS_compID,CS_Sponsors),
FOREIGN KEY(CS_CompID) references Competitions(C_Competition_id));
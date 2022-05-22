
\c pesuvariance;

INSERT INTO LOGIN(Login_ID,Login_UserID,Login_Username,Login_Date,Login_Time,Login_Status,Password)
VALUES ('1','S3','yousha','2021-09-12','08:25:30','IN','xyz123'),
('2','S4','sravya','2021-09-12','08:25:30','IN','xyz123'),
('3','I1','shrikar','2021-09-12','08:25:30','IN','xyz123'),
('4','S2','ramya','2021-09-12','08:25:30','IN','xyz123'),
('5','I3','anjali','2021-09-12','08:25:30','IN','xyz123'),
('6','I2','kruthika','2021-09-12','08:25:30','IN','xyz123'),
('7','I4','anchala','2021-09-12','08:25:30','IN','xyz123'),
('8','S1','srushti','2021-09-12','08:25:30','IN','xyz123');

INSERT INTO DOWNLOADS(Do_UserID,Do_DatasetID)
VALUES ('S1','D1'),('S2','D2'),('S1','D4'),('S3','D6'),('I4','D2'),('I2','D1'),('I3','D1'),('I4','D1');


INSERT INTO QUIZ(Quiz_ID,Quiz_Name,No_Questions,Complexity,Quiz_date,Quiz_time,Total_Score)
VALUES ('Q1','Python',3,'Hard','2021-07-23','02:30:34',10),
('Q2','Keras',3,'Easy','2021-07-23','02:30:34',10),
('Q3','ML',3,'','2021-07-23','02:30:34',10),
('Q4','SQL',3,'Hard','2021-07-23','02:30:34',10),
('Q5','Python',3,'Hard','2021-07-23','02:30:34',10),
('Q6','R',3,'Medium','2021-07-23','02:30:34',10),
('Q7','Algebra',3,'Hard','2021-07-23','02:30:34',10),
('Q8','Statistics',3,'Hard','2021-07-23','02:30:34',10);


INSERT INTO 
QUESTIONS(Question_ID, Question_Desc, Q_Quiz_ID) 
VALUES ('Qu1', 'What is probability?', 'Q8'),
('Qu2', 'What is mode?', 'Q8'),
('Qu3', 'What is mean?', 'Q8'),
('Qu4', 'A coin toss is an example of?', 'Q8'), 
('Qu5', 'What does sample space mean?', 'Q8'), 
('Qu6', 'What does hypotheses space mean?', 'Q8'),
('Qu7','Which is mostly used in Stats?', 'Q8'),
('Qu8', 'Which is more useful interpreting variances?', 'Q8');


INSERT INTO ANSWERS(A_Question_ID,A_Answer_Key,A_Answer_1,A_Answer_2,A_Answer_3)
VALUES ('Qu1', 'A1', 'how likely', 'sum', 'average'),
('Qu2', 'A2', 'Average', 'most common', 'middle'),
('Qu3', 'A3', 'most common', 'middle', 'average'),(
'Qu4', 'A1', 'Random', 'Biased', 'Mode'),
('Qu5', 'A1', 'Set of all possible outcomes or results of that experiment', 'Set of all possible samples', 'Set of all possible entities in the world'), 
('Qu6', 'A1',  'the set of all the possible legal hypothesis', 'Set of all possible illegal and legal hypotheses', 'Set of only illegal hypotheses'), 
('Qu7', 'A3', 'C', 'C++', 'R'), 
('Qu8', 'A3', 'Statutory', 'Testory', ' Chebyshev');


INSERT INTO Competitions(C_Competition_id,C_Competetion_name,C_Requirements,C_Description,C_Rules,C_Sponsors,C_No_of_entries,C_Date,C_Time, C_Image) 
VALUES ('C1','Battle','Python', 'Join to win', 'No plagiarism','PES',12,'2021-09-03','03:23:35',NULL),
('C2','ML JOURNEY','Python','Join to win', 'No plagiarism','PES',12,'2021-09-03','03:23:35',NULL),
('C3','Kaggle Playground','Python','Join to win', 'No plagiarism','PES',12,'2021-09-03','03:23:35',NULL),
('C4','Titanic Competition','Python','Join to win', 'No plagiarism','PES',12,'2021-09-03','03:23:35',NULL),
('C5','PESHACK','Python','Join to win', 'No plagiarism','PES',12,'2021-09-03','03:23:35',NULL),
('C6','DSHACK','Python','Join to win', 'No plagiarism','PES',12,'2021-09-03','03:23:35',NULL),
('C7','CompVision','Python','Join to win', 'No plagiarism','PES',12,'2021-09-03','03:23:35',NULL),
('C8','Decypher2','Python','Join to win', 'No plagiarism','PES',12,'2021-09-03','03:23:35',NULL);


INSERT INTO LEADERBOARD(L_Rank, Submission_ID, Execution_Speed, Grade, Test_Case_Passed, L_CompetitionID) 
VALUES(1,1,1234.12,10,10,'C1'),
(2,2,1457.89,9,9,'C1'),
(3,3,1479.99,8,8,'C1'),
(4,4,1500.12,7,7,'C1'),
(5,5,1534.62,6,6,'C1'),
(6,6,1554.72,5,5,'C1'),
(7,7,1621.33,4,4,'C1'),
(8,8,1680.55,3,3,'C1');


INSERT INTO
POST(Post_ID, Post_title, Post_desc, Post_owner, P_Date, P_Time, Upvotes, P_userID) 
VALUES ('1','Data Analytics','How to discover and treat outlier values?','srushti','08-03-20','12:43:21',4,'S1'),
('2','SQL','How to delete a table in SQL?','ramya','09-04-20','09:13:31',3,'S2'),
('3','Machine Learning','How do I stop overfitting?','yousha','19-04-20','12:43:21',5,'S3'),
('4','Artificial Intelligence','What is reward in reinforcement learning?','sravya','12-05-20','15:21:21',5,'S4'),
('5','Keras','How can I train keras models on a single machine?','shrikar','18-05-20','19:40:20',5,'I1'),
('6','R programming','What are the different data structures in R?','kruthika','20-06-20','19:43:21',7,'I2'),
('7','Statistics','How to calculate range and interquartile range?','anjali','30-09-20','11:44:22',2,'I3'),
('8','Python programming','What is pass in python?','anchala','07-01-21','13:11:31',3,'I4');


INSERT INTO
COMMENT(Comment_ID, Comment_desc, Comment_owner, Comment_Date, Comment_Time, C_userID, Superior_commentID, C_postID) 
VALUES ('1','treat using univariate method, multivariate meth, minkowski method','sravya','09-03-20','06:05:29','S4',NULL,'1' ),
('2','Yes. We can discover using box plot, z score etc ','shrikar','09-03-20','09:07:59','I1','1','1'),
('3','+1','anchala','10-05-20','13:54:22','I4',NULL,'2'),
('4','delete from table_name where condn','kruthika','10-05-20','16:05:39','I2','3','2'),
('5','Reduce it by lowering capacity of model to memorize training data','ramya','19-04-20','06:05:29','S2',NULL,'3'),
('6','using data parallelism and model parallelism','anjali','09-03-20','06:05:29','I3',NULL,'5' ),
('7','vector, list, matrix and dataframe','yousha','10-11-20','07:09:19','S3',NULL,'6'),
('8','Interpreter does not ignore a pass (null) statement','kruthika','09-02-21','12:05:29','I2',NULL,'8' );


INSERT INTO
HOSTED_BY(hb_userID, hb_competitionID) 
VALUES ('S1','C1'),
('S2','C2'),
('S3','C3'),
('S4','C4'),
('I1','C5'),
('I2','C6'),
('I3','C7'),
('I4','C8');


INSERT INTO PARTICIPATED_BY(pb_userID,pb_competitionID) 
VALUES ('S1', 'C1'),('S2', 'C1'),('S3', 'C3'),('S4', 'C1'),('S1', 'C3'),('S1', 'C2'),('S1', 'C4'),('S1', 'C6');


INSERT INTO PARTICIPATES_IN(pb_userID,pb_quizID) 
VALUES ('S1','Q1'),('S2','Q3'),('S3','Q4'),('S1','Q5'),('S4','Q1'),('S2','Q4'),('S4','Q2'),('S3','Q6');


INSERT INTO Instructor (I_QUIZID,INSTRUCTOR_ID) 
VALUES ('Q1','I1'),('Q2','I1'),('Q3','I3'),('Q4','I1'),('Q5','I1'),('Q6','I2'),('Q7','I4'),('Q8','I3');


INSERT INTO C_Sponsors(CS_CompID,CS_Sponsors) 
VALUES ('C1','IBM'),('C2','CISCO'),('C3','AXIS'),('C4','FB'),('C5','Quora'),('C6','Google'),('C7','IBM'),('C8','Visa');
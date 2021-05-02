USE [university];
DROP TABLE dbo.Grades;
DROP TABLE dbo.Courses;
DROP TABLE dbo.Teachers;
DROP TABLE dbo.Students;

USE [university];
DELETE dbo.Grades;
DELETE dbo.Courses;
DELETE dbo.Teachers;
DELETE dbo.Students;



USE [university];
INSERT INTO Students VALUES ('01', 'Aleksandra', 'Barska','s');
INSERT INTO Students VALUES ('02', 'Micha³', 'Sieczczyñski','michal');
INSERT INTO Students VALUES ('03', 'Olga', 'Kowalska','student');
INSERT INTO Students VALUES ('04', 'Michalina', 'Rynkowska','michalina');

INSERT INTO Courses VALUES ('Programming in Python', 6);
INSERT INTO Courses VALUES ('Databases', 4);
INSERT INTO Courses VALUES ('.NET', 5);
INSERT INTO Courses VALUES ('Physics', 3);

INSERT INTO Grades VALUES ('01', 'Databases', 5);
INSERT INTO Grades VALUES ('01', 'Programming in Python', 3);
INSERT INTO Grades VALUES ('01', '.NET', 2);
INSERT INTO Grades VALUES ('02', 'Databases', 5);
INSERT INTO Grades VALUES ('02', 'Programming in Python', 4);
INSERT INTO Grades VALUES ('02', '.NET', 3);

INSERT INTO Teachers VALUES('123','Jan', 'Kowalski','Master of ABC','t');

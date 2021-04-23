USE [university];
DROP TABLE dbo.Grades;
DROP TABLE dbo.Courses;
DROP TABLE dbo.Students;
DROP TABLE dbo.Teachers;

USE [university];
select * from Students;

USE [university];
select * from Grades;

USE [university];
delete dbo.Students;

USE [university];
delete dbo.Grades;

USE [university];
INSERT INTO Students VALUES ('12345678999', 'Aleksandra', 'Barska','s');
INSERT INTO Students VALUES ('12345678998', 'Olga', 'Rogowska','student');
INSERT INTO Students VALUES ('12345678997', 'Michalina', 'Rynkowska','michalina');

INSERT INTO Courses VALUES ('Programming_in_Python', 6);
INSERT INTO Courses VALUES ('Databases', 4);

INSERT INTO Grades VALUES ('12345678999', 'Databases', 5);
INSERT INTO Grades VALUES ('12345678999', 'Programming_in_Python', 5);

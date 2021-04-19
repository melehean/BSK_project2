class Grades_Table:
    def __init__(self, db):
        self.db = db

    def read_all(self):
        print("Read All")
        cursor = self.db.cursor();
        cursor.execute('select * from Grades')
        for row in cursor:
            print(f'row = {row}')
        print()

    def search_by_course_name(self, course_name):
        print('Search by Course Name')
        cursor = self.db.cursor();
        cursor.execute('select * from Grades where Course_Name = ?', course_name)
        for row in cursor:
            print(f'row = {row}')
        print()

    def search_by_student_pesel(self, student_pesel):
        print('Search by Student Pesel')
        cursor = self.db.cursor();
        cursor.execute('select * from Grades where Student_Pesel = ?', student_pesel)
        for row in cursor:
            print(f'row = {row}')
        print()

    def search_by_student_pesel_and_course_name(self,student_pesel, course_name):
        print('Search by Student Pesel and Course Name')
        cursor = self.db.cursor();
        cursor.execute('select * from Grades where Student_Pesel = ? and Course_Name = ?',
        student_pesel, course_name)
        for row in cursor:
            print(f'row = {row}')
        print()

    def insert(self, student_pesel, course_name, grade):
        print('Insert')
        cursor = self.db.cursor()
        cursor.execute('insert into Grades(Student_Pesel, Course_Name, Grade) values(?,?,?);',
        student_pesel, course_name, grade)
        cursor.commit()
        self.read_all()

    def update_grade(self, student_pesel, course_name, grade):
        print('Update')
        cursor = self.db.cursor()
        cursor.execute('update Grades set Grade = ? where Student_Pesel = ? and Course_Name = ?;',
        grade, student_pesel, course_name)
        cursor.commit()
        self.read_all()

    def delete(self, student_pesel, course_name):
        print('Delete')
        cursor = self.db.cursor()
        cursor.execute('delete from Grades where Student_Pesel = ? and Course_Name = ?;',
        student_pesel, course_name)
        cursor.commit()
        self.read_all()
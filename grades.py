class Grades_Table:
    def __init__(self, db):
        self.db = db

    def read_all(self):
        cursor = self.db.cursor()
        cursor.execute('select * from Grades')
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_course_name(self, course_name):
        cursor = self.db.cursor()
        cursor.execute('select * from Grades where Course_Name = ?', course_name)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_student_pesel(self, student_pesel):
        cursor = self.db.cursor()
        cursor.execute('select * from Grades where Student_Pesel = ?', student_pesel)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def search_by_student_pesel_and_course_name(self,student_pesel, course_name):
        cursor = self.db.cursor();
        cursor.execute('select * from Grades where Student_Pesel = ? and Course_Name = ?',
        student_pesel, course_name)
        result = []
        for row in cursor:
            result.append(f'{row}')
        return result

    def insert(self, student_pesel, course_name, grade):
        cursor = self.db.cursor()
        cursor.execute('insert into Grades(Student_Pesel, Course_Name, Grade) values(?,?,?);',
        student_pesel, course_name, grade)
        cursor.commit()
        self.read_all()

    def update_grade(self, student_pesel, course_name, grade):
        cursor = self.db.cursor()
        cursor.execute('update Grades set Grade = ? where Student_Pesel = ? and Course_Name = ?;',
        grade, student_pesel, course_name)
        cursor.commit()
        self.read_all()

    def delete(self, student_pesel, course_name):
        cursor = self.db.cursor()
        cursor.execute('delete from Grades where Student_Pesel = ? and Course_Name = ?;',
        student_pesel, course_name)
        cursor.commit()
        self.read_all()
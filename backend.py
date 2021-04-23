import pandas as pd

import connection
from students import Students_Table
import teachers
import courses
from grades import Grades_Table
import backend
import pop_ups
import os
import time
from datetime import datetime
import webbrowser


ROLES = ['Admin', 'Student', 'Teacher']
OPERATIONS = ['Create', 'Read', 'Update', 'Delete']
TABLES = ['Students', 'Teachers', 'Courses', 'Grades']
OPTIONS = [f'{op}_{t}' for op in OPERATIONS for t in TABLES]

# TODO:
# Decide with role has priviledges to which options
PRIVILEDGES = {}

class User():
    def __init__(self):
        self.login = None
        self.password = None
        self.role = None
        self.name = ''
        self.surname = ''
        self.pesel = ''

    def print(self):
        return f'{self.name} {self.surname}'

    def student_data(self):
        return f'Name: {self.name}\nSurname: {self.surname}\nPesel: {self.pesel[:-5]}*****'

    def extract_data_from_string(self, data):
        user = data.replace('\'','').replace('(', '').replace(')','').replace(' ','').split(',')
        self.pesel = user[0]
        self.name = user[1]
        self.surname = user[2]

# Getting 'database' of users - Admins, Student, Teachers
current_user = User()

admins_data_path = 'admins.csv'
admins = pd.read_csv(admins_data_path,usecols=['Login','Password'])
admins_logins_list = list(admins['Login'])
admins_pwds_list = list(admins['Password'])

students_data_path = 'students.csv'
students = pd.read_csv(students_data_path,usecols=['Login','Password'])
students_logins_list = list(students['Login'])
students_pwds_list = list(students['Password'])

teachers_data_path = 'teachers.csv'
teachers = pd.read_csv(teachers_data_path,usecols=['Login','Password'])
teachers_logins_list = list(teachers['Login'])
teachers_pwds_list = list(teachers['Password'])


def validate_login(login, password):
    if current_user.role == 'Admin':
        for i in range(len(admins['Login'])):
            if admins_logins_list[i] == login and admins_pwds_list[i] == password:
                current_user.login = admins_logins_list[i]
                current_user.password = admins_pwds_list[i]
                return pop_ups.PopUpMode.SUCCESS_LOG_IN
        return pop_ups.PopUpMode.ERROR_INVALID_INFORMATION

    elif current_user.role == 'Student':
        for i in range(len(students['Login'])):
            if students_logins_list[i] == login and students_pwds_list[i] == password:
                current_user.login = students_logins_list[i]
                current_user.password = students_pwds_list[i]
                return pop_ups.PopUpMode.SUCCESS_LOG_IN
        return pop_ups.PopUpMode.ERROR_INVALID_INFORMATION

    elif current_user.role == 'Teacher':
        for i in range(len(teachers['Login'])):
            if teachers_logins_list[i] == login and teachers_pwds_list[i] == password:
                current_user.login = teachers_logins_list[i]
                current_user.password = teachers_pwds_list[i]
                return pop_ups.PopUpMode.SUCCESS_LOG_IN
        return pop_ups.PopUpMode.ERROR_INVALID_INFORMATION


def validate_account_creation(login, password, role, repeat_password):
    new_user = pd.DataFrame([[login, password]], columns = ['Login', 'Password'])
    if login != "" and password == repeat_password:
        if login not in admins_logins_list and login not in students_logins_list and login not in teachers_logins_list:
            if role in ROLES:
                path = admins_data_path if role == 'Admin' else (students_data_path if role == 'Student' else teachers_data_path)
                new_user.to_csv(path, mode = 'a', header = False, index = False)
                return pop_ups.PopUpMode.SUCCESS_SIGN_IN
            else:
                return pop_ups.PopUpMode.ERROR_INVALID_ROLE
        else:
            return pop_ups.PopUpMode.ERROR_USER_EXISTS
    else:
        return pop_ups.PopUpMode.ERROR_INVALID_INFORMATION


def get_student_data():
    # TODO: add validation for non existing user in database ()
    db = connection.connect_to_db()
    users_list = Students_Table(db).search_by_app_login(current_user.login)
    db.close()
    user = users_list[0].replace('\'','').replace('(', '').replace(')','').replace(' ','').split(',')
    current_user.pesel = user[0]
    current_user.name = user[1]
    current_user.surname = user[2]


def update_student_data(surname):
    get_student_data()
    if surname:
        current_user.surname = surname
        db = connection.connect_to_db()
        Students_Table(db).update_surname(pesel=current_user.pesel, new_surname=surname)
        db.close()
        pop_ups.popUp(pop_ups.PopUpMode.SUCCESS_DATA_CHANGE)
    else:
        pop_ups.popUp(pop_ups.PopUpMode.ERROR_INVALID_INFORMATION)


def show_students():
    db = connection.connect_to_db()
    students = Students_Table(db).read_all()
    students_list = f'LIST OF STUDENTS - STATE ON {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n'
    iterator = 1
    for s in students:
        u = User()
        u.extract_data_from_string(s)
        students_list += f'{iterator}. {u.print()}\n'
        iterator += 1

    # pop_ups.students_list(students_list)
    current_directory = os.getcwd()
    students_list_file = f'{current_directory}/students_list.txt'

    f = open(students_list_file, "w")
    f.write(students_list)

    time.sleep(2)

    webbrowser.open(students_list_file)
    # os.system(f'notepad.exe {students_list_file}')


def show_grades():
    get_student_data()
    db = connection.connect_to_db()
    grades = Grades_Table(db).search_by_student_pesel(current_user.pesel)
    db.close()

    students_grades = f''
    for g in grades:
        grade_info = g.replace('\'','').replace('(', '').replace(')','').replace(' ','').split(',')
        students_grades += f'{grade_info[1]} -> {grade_info[2]}/5\n'
    
    pop_ups.show_grades(students_grades)




# ---------------------------------------------

def main():
    db = connection.connect_to_db()
    # do some stuff
    db.close()

def execute_operation(db, operation):
    print("Execute")
    cursor = db.cursor()
    cursor.execute(operation)


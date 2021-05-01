# External imports
import pandas as pd
import os
import time
from datetime import datetime
import webbrowser

# Internal imports
from students import Students_Table
from teachers import Teachers_Table
from courses import Courses_Table
from grades import Grades_Table
import connection
import teachers
import courses
import backend
import pop_ups
import gui


# Class responsible for storing currently logged in user's data/info
class User():
    def __init__(self):
        self.login = None
        self.password = None
        self.role = None
        self.name = ''
        self.surname = ''
        self.pesel = ''
        self.degree = ''

    def print(self):
        return f'{self.name} {self.surname}'

    def user_data(self):
        text = f'Name: {self.name}\nSurname: {self.surname}'
        text = f'{text}\nPesel: {self.pesel[:-5]}*****' if self.role == 'Student' else text
        text = f'{text}\nDegree: {self.degree}' if self.role == 'Teacher' else text
        return text

    def extract_data_from_string(self, data):
        user = data.replace('(\'', '').replace('\')','').split("\', \'")
        self.pesel = user[0]
        self.name = user[1]
        self.surname = user[2]


# ----------------------- USERS LISTS -----------------------

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

# Defined in application roles and priviledges
ROLES = ['Admin', 'Student', 'Teacher']
OPERATIONS = ['Create', 'Read', 'Update', 'Delete']
TABLES = ['Students', 'Teachers', 'Courses', 'Grades']
OPTIONS = [f'{op}_{t}' for op in OPERATIONS for t in TABLES]
PRIVILEDGES = {}


# ----------------------- VALIDATION -----------------------

# Handle and validate correct login
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

# Handle and validate correct account creation
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


# ----------------------- STUDENT'S MENU -----------------------

# Return currently logged in student data
def get_student_data():
    db = connection.connect_to_db()
    users_list = Students_Table(db).search_by_app_login(current_user.login)
    db.close()
    if users_list:
        user = users_list[0].replace('(\'', '').replace('\')','').split("\', \'")
        current_user.pesel = user[0]
        current_user.name = user[1]
        current_user.surname = user[2]
        pop_ups.currentUserInfo()
    else:
        print('User does not exist')
        pop_ups.popUp(pop_ups.PopUpMode.ERROR_USER_DOES_NOT_EXIST)
        gui.StudentScreen().logout()

# Handle student's surname update
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

# Return list of all registered in database studetns
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

    current_directory = os.getcwd()
    students_list_file = f'{current_directory}/students_list.txt'
    f = open(students_list_file, "w+")
    f.write(students_list)
    time.sleep(1)
    webbrowser.open(students_list_file)

# Handle showing student's grade showup
def show_grades(pesel):
    db = connection.connect_to_db()
    grades = Grades_Table(db).search_by_student_pesel(pesel)
    db.close()

    if grades:
        students_grades = f'Student <{pesel[:-5]}*****> scored:\n'
        for g in grades:
            grade_info = g.replace('(\'', '').replace(')', '').replace('\'', '').split(", ")
            print(grade_info)
            students_grades += f'{grade_info[1]} -> {grade_info[2]}/5\n'

        pop_ups.show_grades(students_grades)
    else:   # no grades yet
        pop_ups.show_grades(f'Student <{pesel[:-5]}*****> has got\nno grades yet')


# ----------------------- TEACHER'S MENU -----------------------

# Return currently logged in student data
def get_teacher_data():
    db = connection.connect_to_db()
    users_list = Teachers_Table(db).search_by_app_login(current_user.login)
    db.close()
    if users_list:  # user does not exist in database
        user = users_list[0].replace('(\'', '').replace('\')','').split("\', \'")
        current_user.pesel = user[0]
        current_user.name = user[1]
        current_user.surname = user[2]
        current_user.degree = user[3]
        pop_ups.currentUserInfo()
    else:
        print('User does not exist')
        pop_ups.popUp(pop_ups.PopUpMode.ERROR_USER_DOES_NOT_EXIST)
        gui.TeacherScreen().logout()

def add_grade(pesel, course_name, grade):
    db = connection.connect_to_db()
    students = Students_Table(db).read_all()
    courses = Courses_Table(db).read_all()

    if pesel in str(students):
        if course_name in str(courses):
            Grades_Table(db).insert(pesel, course_name, grade)
            pop_ups.popUp(pop_ups.PopUpMode.SUCCES_GRADE_ADDITION)
        else:
            pop_ups.popUp(pop_ups.PopUpMode.ERROR_INVALID_COURSE_NAME)
    else:
        pop_ups.popUp(pop_ups.PopUpMode.ERROR_INVALID_STUDENT_NUMBER)
    
    db.close()

# ----------------------- ADMIN'S MENU -----------------------

def execute_query(query):
    db = connection.connect_to_db()
    query_result = execute(db, query)
    db.close()

    result = extract_query_result(query, query_result)

    current_directory = os.getcwd()
    date = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    query_result_file = f'{current_directory}/query_result_{date}.txt'
    f = open(query_result_file, "w+")
    f.write(result)
    time.sleep(1)
    webbrowser.open(query_result_file)


def execute(db, operation):
    cursor = db.cursor()
    cursor.execute(operation)
    result = []
    for row in cursor:
        result.append(f'{row}')
    return result


def extract_query_result(query, query_result):
    result = f'QUERY:\n{query}\n\nRESULT:\n'
    for row in query_result:
        row = row.replace('(','').replace(')','').replace('\'','').split(', ')
        for element in row:
            result += f'{element} '
        result += f'\n'
    
    return result

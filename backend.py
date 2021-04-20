import pandas as pd

import connection
import students
import teachers
import courses
import grades
import backend
import pop_ups

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


# ---------------------------------------------

def main():
    db = connection.connect_to_db()
    # do some stuff
    db.close()

def execute_operation(db, operation):
    print("Execute")
    cursor = db.cursor()
    cursor.execute(operation)


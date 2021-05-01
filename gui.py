# External imports
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

# Internal imports
from pop_ups import PopUpMode, popUp
import backend
import pop_ups


# ----------------------- ACCOUNT MANAGEMENT -----------------------

# Class responsible for choosing user role
class roleLoginScreen(Screen):
    def click_admin(self):
        backend.current_user.role = 'Admin'

    def click_student(self):
        backend.current_user.role = 'Student'
    
    def click_teacher(self):
        backend.current_user.role = 'Teacher'


# Class responsible for handling logging in
class loginScreen(Screen):
    login = ObjectProperty(None)
    password = ObjectProperty(None)

    # Change screen content to menu depending on logged user (role: Student/Teacher/Admin)
    def login_btn_clicked(self):
        action_result = backend.validate_login(login=self.login.text, password=self.password.text)
        if action_result == PopUpMode.SUCCESS_LOG_IN:
            user_role = backend.current_user.role.lower()
            screen_manager.current = f'{user_role}_screen'
            popUp(PopUpMode.SUCCESS_LOG_IN)
            self.login.text = ''
            self.password.text = ''
        else:
            popUp(action_result)
            self.login.text = ''
            self.password.text = ''


# Class responsible for handling signing up and validating entered user's credentials
class signupScreen(Screen):
    login = ObjectProperty(None)
    password = ObjectProperty(None)
    repeat_password = ObjectProperty(None)
    role = ObjectProperty(None)

    # Button handling new account creation
    def create_account_btn_clicked(self):
        action_result = backend.validate_account_creation(login=self.login.text,
                                                          password=self.password.text,
                                                          role=self.role.text,
                                                          repeat_password=self.repeat_password.text)
        if action_result == PopUpMode.SUCCESS_SIGN_IN:
            user_role = backend.current_user.role.lower()
            screen_manager.current = f'{user_role}_screen'
            popUp(PopUpMode.SUCCESS_SIGN_IN)
        else:
            popUp(action_result)
            self.login.text = ''
            self.password.text = ''
            self.repeat_password.text = ''
            self.role.text = ''


# ----------------------- STUDENT'S MENU -----------------------

# Class responsible for handling student's menu
class StudentScreen(Screen):
    # Show currently logged student's information (name, surname, pesel)
    def show_student_info(self):
        backend.get_student_data()

    # Show list of all students (open list additionally in separate notepad
    # window and save list in *.txt file)
    def show_students(self):
        backend.show_students()

    # Show currently logged student's grades in popup window
    def show_grades(self):
        backend.get_student_data()
        backend.show_grades(backend.current_user.pesel)

    # Handle user logout
    def logout(self):
        backend.current_user = backend.User()
        screen_manager.current = 'role_login_screen'


# Class responsible for handling student's surname change
class StudentDataScreen(Screen):
    new_surname = ObjectProperty(None)

    # Handle student surname update
    def save_student_info(self):
        backend.update_student_data(surname=self.new_surname.text)
        self.new_surname.text = ''


# ----------------------- TEACHER'S MENU -----------------------

# Class responsible for handling teacher's menu
class TeacherScreen(Screen):

    # Show currently logged teacher's information (name, surname, pesel, surname)
    def show_teacher_info(self):
        backend.get_teacher_data()

    # Show list of all students (open list additionally in separate notepad
    # window and save list in *.txt file)
    def show_students(self):
        backend.show_students()

    # Handle user logout
    def logout(self):
        backend.current_user = backend.User()
        screen_manager.current = 'role_login_screen'


# Class responsible for handling showing student's grades
class StudentsGradesScreen(Screen):
    student_pesel = ObjectProperty(None)

    def show_student_grades(self):
        backend.show_grades(self.student_pesel.text)
        self.student_pesel.text = ''


# Class responsible for handling adding new grade
class AddStudentGradeScreen(Screen):
    pesel = ObjectProperty(None)
    course = ObjectProperty(None)
    grade = ObjectProperty(None)

    def add_grade(self):
        backend.add_grade(self.pesel.text, self.course.text, self.grade.text)
        self.pesel.text = ''
        self.course.text = ''
        self.grade.text = ''


# ----------------------- ADMIN'S MENU -----------------------

class AdminScreen(Screen):

    # Handle user logout
    def logout(self):
        backend.current_user = backend.User()
        screen_manager.current = 'role_login_screen'


class AdminTypeQueryScreen(Screen):
    query = ObjectProperty(None)
    # Handle typing query directly from text input field and executing it
    def execute_query(self):
        print('ADMIN - type query')
        backend.execute_query(self.query.text)



# Class responsible for handling admin choosing query options
class AdminPanelScreen(Screen):
    table = ObjectProperty(None)
    crud_operation = ObjectProperty(None)

    def handle_table_choosing(self, instance, value, chosen_table):
        if value == True:
            self.table = chosen_table
            print(f'Chosen table: {self.table}')

    def handle_CRUD_operation_choosing(self, instance, value, chosen_crud_operation):
        if value == True:
            self.crud_operation = chosen_crud_operation
            print(f'Chosen CRUD operation: {self.crud_operation}')
    
    def submit(self):
        if self.table and self.crud_operation:
            execute = f'{self.crud_operation}_{self.table}'
            print(f'Chosen configuration = {execute}')

            # TODO:
            # Handle showing new screen depending on chosen configuration
            # execute query/show/delete etc.
            # screen_manager.current = 

    def logout(self):
        backend.current_user = backend.User()
        screen_manager.current = 'role_login_screen'
        popUp(PopUpMode.SUCCESS_LOGOUT)


# ----------------------- APPLICATION LAYOUT -----------------------


# Setting application layout (layout is in the external file)
kv = Builder.load_file('ApplicationLayout.kv')


# Class responsible for managing all screeens
class screenManager(ScreenManager): 
    pass


# Create and add new screens to the screen manager
screen_manager = ScreenManager()
screen_manager.add_widget(roleLoginScreen(name='role_login_screen'))
screen_manager.add_widget(loginScreen(name='login_screen'))
screen_manager.add_widget(signupScreen(name='signup_screen'))
screen_manager.add_widget(StudentScreen(name='student_screen'))
screen_manager.add_widget(StudentDataScreen(name='student_data_screen'))
screen_manager.add_widget(TeacherScreen(name='teacher_screen'))
screen_manager.add_widget(AdminPanelScreen(name='admin_panel_screen'))
screen_manager.add_widget(StudentsGradesScreen(name='students_grades_screen'))
screen_manager.add_widget(AddStudentGradeScreen(name='add_student_grade_screen'))
screen_manager.add_widget(AdminScreen(name='admin_screen'))
screen_manager.add_widget(AdminTypeQueryScreen(name='admin_type_query'))

# Class responsible for handling application start up
class DBManagementApplicationMain(App): 
    def build(self):
        return screen_manager
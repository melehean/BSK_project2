from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.app import App
from kivy.lang import Builder

from pop_ups import PopUpMode, popUp
import backend
import pop_ups


# Class responsible for choosing user logging role
class roleLoginScreen(Screen):

    def click_admin(self):
        backend.current_user.role = 'Admin'

    def click_student(self):
        backend.current_user.role = 'Student'
    
    def click_teacher(self):
        backend.current_user.role = 'Teacher'

# Class responsible for handling loging in
class loginScreen(Screen):
    login = ObjectProperty(None)
    password = ObjectProperty(None)

    def login_btn_clicked(self):
        print(backend.current_user.role)
        action_result = backend.validate_login(login=self.login.text, password=self.password.text)
        print(action_result)
        if action_result == PopUpMode.SUCCESS_LOG_IN:
            user_role = backend.current_user.role.lower()
            screen_manager.current = f'{user_role}_screen'
            popUp(PopUpMode.SUCCESS_LOG_IN)
        else:
            popUp(action_result)
            self.login.text = ""
            self.password.text = ""

# Class responsible for handling signing up and validating entered user's credentials
class signupScreen(Screen):
    login = ObjectProperty(None)
    password = ObjectProperty(None)
    repeat_password = ObjectProperty(None)
    role = ObjectProperty(None)

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


class AdminScreen(Screen):
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


class StudentScreen(Screen):
    pass

class TeacherScreen(Screen):
    pass


# Setting application layout
kv = Builder.load_file('ApplicationLayout.kv')

# Class responsible for managing all screeens
class screenManager(ScreenManager): 
    pass


screen_manager = ScreenManager()
screen_manager.add_widget(roleLoginScreen(name='role_login_screen'))
screen_manager.add_widget(loginScreen(name='login_screen'))
screen_manager.add_widget(signupScreen(name='signup_screen'))
screen_manager.add_widget(StudentScreen(name='student_screen'))
screen_manager.add_widget(TeacherScreen(name='teacher_screen'))
screen_manager.add_widget(AdminScreen(name='admin_screen'))

# Class responsible for handling application start up
class DBManagementApplicationMain(App): 
    def build(self):
        return screen_manager
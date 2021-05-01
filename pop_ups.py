# External imports
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import enum

# Internal imports
import backend


# Custom class with Enum type - all possible popup types
class PopUpMode(enum.Enum):
    ERROR_INVALID_INFORMATION = 0
    SUCCESS_LOG_IN = 1
    SUCCESS_SIGN_IN = 2
    SUCCESS = 3
    ERROR_UNKNOWN_USER = 4
    ERROR_USER_EXISTS = 5
    ERROR_INVALID_ROLE = 6
    SUCCESS_LOGOUT = 7
    SUCCESS_DATA_CHANGE = 8
    ERROR_USER_DOES_NOT_EXIST = 9
    ERROR_INVALID_STUDENT_NUMBER = 10
    ERROR_INVALID_COURSE_NAME = 11
    SUCCES_GRADE_ADDITION = 12

# Classes required in order to define their layout in ApplicationLayout.kv file
class errorInvalidInformation(FloatLayout): 
    pass

class successLogIn(FloatLayout): 
    pass

class successSignIn(FloatLayout): 
    pass

class success(FloatLayout):
    pass

class errorUnknownUser(FloatLayout):
    pass

class errorUserExists(FloatLayout):
    pass

class errorInvalidRole(FloatLayout):
    pass

class successLogout(FloatLayout):
    pass

class successDataChange(FloatLayout):
    pass

class errorUserDoesNotExist(FloatLayout):
    pass

class errorInvalidStudentNumber(FloatLayout):
    pass

class erorrInvalidCourseName(FloatLayout):
    pass

class successGradeAddition(FloatLayout):
    pass


# Handle showing currently logged student
def currentUserInfo():
    user = backend.current_user
    user_text = user.user_data()

    popup = Popup(
            title ='User information',
            content = Label(text=user_text),
            size_hint=(.5,.5), size=(100, 100)
        )
    popup.open()


def show_grades(grades):
    popup = Popup(
            title ='Grades',
            content = Label(text=grades),
            size_hint=(.5,.5), size=(100, 100)
        )
    popup.open()


def popUp(mode, extra_info=None):
    show = None
    info = 'INFO INFO'
    if mode.value == 0:
        info = 'ERROR'
        show = errorInvalidInformation()
    elif mode.value == 1:
        info = 'INFO'
        show = successLogIn()
    elif mode.value == 2:
        info = 'INFO'
        show = successSignIn()
    elif mode.value == 3:
        info = 'INFO'
        show = success()
    elif mode.value == 4:
        info = 'ERROR'
        show = errorUnknownUser()
    elif mode.value == 5:
        info = 'ERROR'
        show = errorUserExists()
    elif mode.value == 6:
        info = 'ERROR'
        show = errorInvalidRole()
    elif mode.value == 7:
        info = 'INFO'
        show = successLogout()
    elif mode.value == 8:
        info = 'INFO'
        show = successDataChange()
    elif mode.value == 9:
        info = 'ERRO'
        show = errorUserDoesNotExist()
    elif mode.value == 10:
        info = 'ERRO'
        show = errorInvalidStudentNumber()
    elif mode.value == 11:
        info = 'ERRO'
        show = erorrInvalidCourseName()
    elif mode.value == 12:
        info = 'INFO'
        show = successGradeAddition()

    window = Popup(title = info, content = show, size_hint = (0.5, 0.4))
    window.open()

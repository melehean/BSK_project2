from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import backend
import enum

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


def currentUserInfo():
    user = backend.current_user
    user_text = user.student_data()

    popup = Popup(
            title ='Student information',
            content = Label(text=user_text),
            size_hint=(.5,.5), size=(100, 100)
        )
    popup.open()


def show_grades(grades):
    popup = Popup(
            title ='Student\'s grades',
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

    window = Popup(title = info, content = show,
                   size_hint = (0.5, 0.4)) 
    window.open()

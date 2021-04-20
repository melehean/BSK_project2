from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
import enum

class PopUpMode(enum.Enum):
    ERROR_INVALID_INFORMATION = 0
    SUCCESS_LOG_IN = 1
    SUCCESS_SIGN_IN = 2
    SUCCESS = 3
    ERROR_UNKNOWN_USER = 4
    ERROR_USER_EXISTS = 5
    ERROR_INVALID_ROLE = 6


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
    
    window = Popup(title = info, content = show,
                   size_hint = (0.5, 0.4)) 
    window.open()

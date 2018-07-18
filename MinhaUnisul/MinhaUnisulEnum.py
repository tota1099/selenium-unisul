from enum import Enum


class Columns(Enum):
    WORK_NAME = 3
    WORK_GRADE = 5
    DISCIPLINE = 0


class Buttons(Enum):
    USER_FIELD_ID = "userid"
    PASSWORD_FIELD_ID = "pwd"
    ACCESS_BUTTON_ID = "subEnviar"
    ERROR_LOGIN_ID = "login-error"
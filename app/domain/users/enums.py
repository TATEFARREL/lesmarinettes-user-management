from enum import Enum

class Role(str, Enum):
    ADMIN = "ADMIN"
    STAFF = "STAFF"

class StaffKind(str, Enum):
    TEACHER = "TEACHER"
    ACCOUNTANT = "ACCOUNTANT"
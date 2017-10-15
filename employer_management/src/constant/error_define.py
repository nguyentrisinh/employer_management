from ..infrastructures import ApiErrorMessage


class ErrorDefine:
    def __init__(self):
        pass

    # Error Default: 9999

    # Error Auth: 10xx
    LOGIN_FAIL = ApiErrorMessage('login fail', 1000)
    INVALID_TOKEN = ApiErrorMessage('Invalid token', 1001)
    USER_INACTIVE = ApiErrorMessage('User inactive or deleted', 1002)
    TOKEN_EXPIRED = ApiErrorMessage('Token has expired', 1003)
    USER_NOT_FOUND = ApiErrorMessage('User not found', 1004)
    USER_ALREADY_EXISTS = ApiErrorMessage('User have already existed', 1005)
    MISSING_TOKEN = ApiErrorMessage('Missing token', 1006)

    # Error Department: 11xx
    DEPARTMENT_NOT_FOUND = ApiErrorMessage('Department not found', 1100)

    # Error Employer: 12xx
    EMPLOYER_ALREADY_EXITS = ApiErrorMessage('Employer already exists', 1200)
    EMPLOYER_NOT_FOUND = ApiErrorMessage('Employer not found', 1201)
    EMPLOYER_TYPE_ERROR = ApiErrorMessage('Employer type error', 1202)

    # Error Full-time Salary: 13xx
    FULL_TIME_SALARY_EXIST = ApiErrorMessage('Full-time salary exist', 1300)

    # Error Part-time salary: 14xx
    PART_TIME_SALARY_EXIST = ApiErrorMessage('Part-time salary exist', 1400)

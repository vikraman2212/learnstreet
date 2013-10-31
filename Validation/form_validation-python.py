""" Rules:
Username:
    1. Username Should be minimum 5 characters long.
    2. No Space, no Special Characters (i.e., must be alphanumeric).
Email:
    1. Valid Email Address.
        = valid characters + '@' + more valid chars + '.' + yet more valid chars
Phone:
    1. Valid US Phone Number(10 digits: 123-454-7890, (123) 454-7890, (123)+454 7890)
Password:
    1. Password length should be minimum 6 characters long.
    2. Password should not be same as Username.
    
"""
import re
def username_validation(name):
    "REPLACE THIS CODE WITH YOUR VALIDATION METHOD"
    regex_name = "^[a-zA-Z0-9_]+$"
    if re.match(regex_name,name) and len(name) >= 5:
        return True

def email_validation(email):
    regex_email = "^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$"
    "REPLACE THIS CODE WITH YOUR VALIDATION METHOD"
    if re.match(regex_email,email):
        return True
    


def phone_validation(phone):
    regex_phone = "(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$"
    "REPLACE THIS CODE WITH YOUR VALIDATION METHOD"
    if re.match(regex_phone,phone):
        return True

def password_validation(password, uname):
    "REPLACE THIS CODE WITH YOUR VALIDATION METHOD"
    regex_password = "^[a-zA-Z0-9@#?*%]+$"
    length = len(password)
    if length >= 6 and length < 30:
        if re.match(regex_password, password):
            return True
        else:
            return False
    return False
            


def conpassword_validation(conpass, res):
    "REPLACE THIS CODE WITH YOUR VALIDATION METHOD"
    if len(conpass) == 0:
        return False
    elif conpass != res:
        return False
    else:
        return True
  

#Name: Lakshmi Prabha
#Program : Write a python code using lambda function to validate the Regular expression for the following
"""
a. Email Address
b. Mobile numbers of Bangladesh
c. Telephone numbers of USA
d. 16 character alpha-numeric password composed of alphabets of Upper case, Lower case, Special Characters and Numbers.

"""
#Version: 1
#Pragramming language: Python
#Python Version: 3.12.0

import re

def validate_email(email):
    return bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email))

def validate_bangladesh_mobile_number(number):
    return bool(re.match(r'^\+8801[1-9]\d{8}$', number))

def validate_usa_telephone_number(number):
    return bool(re.match(r'^\+1-\d{3}-\d{3}-\d{4}$', number))

def validate_password(password):
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$', password))

# Example usage:
email_input = input("Enter an email address: ")
print("Valid email address." if validate_email(email_input) else "Invalid email address.")

mobile_input = input("Enter a Bangladesh mobile number: ")
print("Valid Bangladesh mobile number." if validate_bangladesh_mobile_number(mobile_input) else "Invalid Bangladesh mobile number.")

telephone_input = input("Enter a USA telephone number: ")
print("Valid USA telephone number." if validate_usa_telephone_number(telephone_input) else "Invalid USA telephone number.")

password_input = input("Enter a 16-character alpha-numeric password: ")
print("Valid password." if validate_password(password_input) else "Invalid password.")

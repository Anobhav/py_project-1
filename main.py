import login
import signup
import exception_handling
from Operations import Operations

print("Welcome to Banking Management System")

try:
    user_type = int(input("Enter 1 if you're an existing user or 2 if you're a new user: "))
except ValueError:
    print("Please enter 1 or 2, alphabets are not allowed")
    exit()

if not exception_handling.user_type_input(user_type):
    exit()

username = None

if user_type == 1:
    uname = input("Enter your username: ")
    pwd = input("Enter your password: ")
    username = login.lg(uname, pwd)
    if not username:
        exit()
else:
    username = signup.sg()
    if not username:
        exit()

# Start operations
user_ops = Operations(username)

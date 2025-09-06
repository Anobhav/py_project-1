import json

def sg():
    """CLI Signup function"""
    print("Please enter the following information to open your online banking account")

    username = input("Enter your username: ")
    if username.isdigit():
        print("Username can't be only digits")
        return None

    phone_no = input("Enter your phone number: ")
    if not phone_no.isdigit() or len(phone_no) != 10:
        print("Invalid phone number")
        return None

    email = input("Enter your email address: ")
    if "@" not in email:
        print("Invalid email address")
        return None

    password = input("Set a password: ")
    special_chars = "!@#$%^&*()-+?_=,<>/"
    if not any(c in special_chars for c in password):
        print("Password must contain at least one special character")
        return None

    # Load existing data
    with open("Bank_Data.json", "r") as f:
        data = json.load(f)

    if "users" not in data:
        data["users"] = {}

    if username in data["users"]:
        print("Username already exists")
        return None

    # Add new user
    data["users"][username] = {
        "password": password,
        "balance": 0,
        "transactions": []
    }

    with open("Bank_Data.json", "w") as f:
        json.dump(data, f, indent=4)

    print(f"Account created successfully for {username}!")
    return username

def add_user(username, password):
    """GUI Signup function (simplified, only username & password)"""
    with open("Bank_Data.json", "r") as f:
        data = json.load(f)

    if "users" not in data:
        data["users"] = {}

    if username in data["users"]:
        raise ValueError("Username already exists")

    special_chars = "!@#$%^&*()-+?_=,<>/"
    if not any(c in special_chars for c in password):
        raise ValueError("Password must contain at least one special character")

    data["users"][username] = {
        "password": password,
        "balance": 0,
        "transactions": []
    }

    with open("Bank_Data.json", "w") as f:
        json.dump(data, f, indent=4)

    return username

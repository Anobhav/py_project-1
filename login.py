import json

def lg(username, password):
    with open("Bank_Data.json", "r") as f:
        data = json.load(f)

    users = data.get("users", {})
    if username in users and password == users[username]["password"]:
        print(f"Welcome {username}, login successful")
        return username
    else:
        print("Username or password incorrect")
        return None

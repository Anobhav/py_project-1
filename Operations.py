import json

class Operations:
    def __init__(self, username):
        self.username = username
        self.show_menu()

    def show_menu(self):
        while True:
            print(f"\nHi {self.username}! Choose an operation:")
            print("1. Deposit Money\n2. Withdraw Money\n3. Check Balance\n4. Change Account Details\n5. Exit")
            try:
                opr = int(input("Enter your operation: "))
            except ValueError:
                print("Invalid input! Enter a number.")
                continue
            self.switch_case(opr)

    def switch_case(self, opr):
        match opr:
            case 1:
                self.deposit()
            case 2:
                self.withdraw()
            case 3:
                self.check_balance()
            case 4:
                self.change_details()
            case 5:
                print("Exiting... Goodbye!")
                exit()
            case _:
                print("Invalid input, try again")

    def deposit(self):
        try:
            amount = int(input("Enter amount to deposit: "))
            if amount < 0:
                print("Deposit amount can't be negative")
                return
        except ValueError:
            print("Invalid amount!")
            return

        with open("Bank_Data.json", "r") as f:
            data = json.load(f)

        if self.username in data["users"]:
            data["users"][self.username]["balance"] += amount
            data["users"][self.username]["transactions"].append({"type": "deposit", "amount": amount})
            with open("Bank_Data.json", "w") as f:
                json.dump(data, f, indent=4)
            print(f"Amount {amount} deposited successfully!")
        else:
            print("User not found!")

    def withdraw(self):
        with open("Bank_Data.json", "r") as f:
            data = json.load(f)

        if self.username in data["users"]:
            try:
                amount = int(input("Enter amount to withdraw: "))
                if amount < 0 or amount > data["users"][self.username]["balance"]:
                    print("Invalid withdraw amount!")
                    return
            except ValueError:
                print("Invalid input!")
                return

            data["users"][self.username]["balance"] -= amount
            data["users"][self.username]["transactions"].append({"type": "withdraw", "amount": amount})
            with open("Bank_Data.json", "w") as f:
                json.dump(data, f, indent=4)
            print(f"Amount {amount} withdrawn successfully!")
        else:
            print("User not found!")

    def check_balance(self):
        with open("Bank_Data.json", "r") as f:
            data = json.load(f)
        if self.username in data["users"]:
            print(f"Your account balance is: {data['users'][self.username]['balance']}")
        else:
            print("User not found!")

    def change_details(self):
        print("To change account details, please contact the admin physically.")

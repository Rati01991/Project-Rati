# def create_user_data_file(file_name):
#     try:
#         with open(file_name, "w", encoding="utf-8") as file:
#             print("File opened successfully.")
#             file.write("Rati:1000.0\n")
#             file.write("Paata:2000.0\n")
#         print(f"User data file '{file_name}' created successfully.")
#     except Exception as e:
#         print("An error occurred while creating the user data file:", e)

# # ====================================
# create_user_data_file("user_data.txt")



# class ATM:
#     def __init__(self, user_data_file):
#         self.user_data_file = user_data_file
#         self.user_data = self.load_user_data()

#     def load_user_data(self):
#         try:
#             with open(self.user_data_file, "r", encoding="utf-8") as file:
#                 user_data = {}
#                 for line in file:
#                     username, balance = line.strip().split(":")
#                     user_data[username] = float(balance)
#                 return user_data
#         except FileNotFoundError:
#             print(f"User data file '{self.user_data_file}' not found.")
#             return {}

#     def save_user_data(self):
#         with open(self.user_data_file, "w", encoding="utf-8") as file:
#             for username, balance in self.user_data.items():
#                 file.write(f"{username}:{balance}\n")

#     def check_balance(self, username):
#         return self.user_data.get(username, "User not found")

#     def deposit(self, username, amount):
#         if username in self.user_data:
#             self.user_data[username] += amount
#             self.save_user_data()
#             return f"Deposit of ${amount} successful. Current balance: ${self.user_data[username]}"
#         else:
#             return "User not found"

#     def withdraw(self, username, amount):
#         if username in self.user_data:
#             if amount <= self.user_data[username]:
#                 self.user_data[username] -= amount
#                 self.save_user_data()
#                 return f"Withdrawal of ${amount} successful. Current balance: ${self.user_data[username]}"
#             else:
#                 return "Insufficient funds"
#         else:
#             return "User not found"

# def main():
#     atm = ATM("user_data.txt")
#     while True:
#         print("\nOptions:")
#         print("1. Check Balance")
#         print("2. Deposit")
#         print("3. Withdraw")
#         print("4. Exit")

#         choice = input("Enter your choice: ")
#         if choice == "1":
#             username = input("Enter username: ")
#             print("Current balance:", atm.check_balance(username))
#         elif choice == "2":
#             username = input("Enter username: ")
#             amount = float(input("Enter amount to deposit: $"))
#             print(atm.deposit(username, amount))
#         elif choice == "3":
#             username = input("Enter username: ")
#             amount = float(input("Enter amount to withdraw: $"))
#             print(atm.withdraw(username, amount))
#         elif choice == "4":
#             print("Thank you for using the ATM. Goodbye!")
#             atm.save_user_data()
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

##Updated project of ATM.

import csv
from datetime import datetime

class ATM:
    def __init__(self, user_data_file):
        self.user_data_file = user_data_file
        self.user_data = self.load_user_data()

    def load_user_data(self):
        try:
            with open(self.user_data_file, "r", encoding="utf-8") as file:
                user_data = {}
                csv_reader = csv.reader(file)
                next(csv_reader)
                for row in csv_reader:
                    username, balance = row
                    user_data[username] = float(balance)
                return user_data
        except FileNotFoundError:
            print(f"User data file '{self.user_data_file}' not found.")
            return {}

    def save_user_data(self):
        with open(self.user_data_file, "w", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["Username", "Balance"]) 
            for username, balance in self.user_data.items():
                csv_writer.writerow([username, balance])

    def check_balance(self, username):
        return self.user_data.get(username, "User not found")

    def deposit(self, username, amount):
        if username in self.user_data:
            self.user_data[username] += amount
            self.save_transaction(username, amount, "Deposit")
            self.save_user_data()
            return f"Deposit of ${amount} successful. Current balance: ${self.user_data[username]}"
        else:
            return "User not found"

    def withdraw(self, username, amount):
        if username in self.user_data:
            if amount <= self.user_data[username]:
                self.user_data[username] -= amount
                self.save_transaction(username, amount, "Withdrawal")
                self.save_user_data()
                return f"Withdrawal of ${amount} successful. Current balance: ${self.user_data[username]}"
            else:
                return "Insufficient funds"
        else:
            return "User not found"

    def register_user(self, username):
        if username in self.user_data:
            return "Username already exists. Please choose a different username."
        else:
            self.user_data[username] = 0  # Set initial balance to 0
            self.save_user_data()
            return "User registration successful."

    def transfer(self, from_user, to_user, amount):
        if from_user in self.user_data and to_user in self.user_data:
            if amount <= self.user_data[from_user]:
                self.user_data[from_user] -= amount
                self.user_data[to_user] += amount
                self.save_transaction(from_user, amount, "Transfer to " + to_user)
                self.save_transaction(to_user, amount, "Transfer from " + from_user)
                self.save_user_data()
                return f"Transfer of ${amount} from {from_user} to {to_user} successful."
            else:
                return "Insufficient funds"
        else:
            return "One or both users not found"

    def save_transaction(self, username, amount, transaction_type):
        transaction_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("transaction_history.csv", "a", newline='', encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([username, amount, transaction_type, transaction_date])

def main():
    atm = ATM("user_data.csv")
    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Register User")
        print("5. Transfer Money")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            print("Current balance:", atm.check_balance(username))
        elif choice == "2":
            username = input("Enter username: ")
            amount = float(input("Enter amount to deposit: $"))
            print(atm.deposit(username, amount))
        elif choice == "3":
            username = input("Enter username: ")
            amount = float(input("Enter amount to withdraw: $"))
            print(atm.withdraw(username, amount))
        elif choice == "4":
            username = input("Enter new username: ")
            print(atm.register_user(username))
        elif choice == "5":
            from_user = input("Enter username to transfer from: ")
            to_user = input("Enter username to transfer to: ")
            amount = float(input("Enter amount to transfer: $"))
            print(atm.transfer(from_user, to_user, amount))
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            atm.save_user_data()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
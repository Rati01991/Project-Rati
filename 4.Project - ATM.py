def create_user_data_file(file_name):
    try:
        with open(file_name, "w", encoding="utf-8") as file:
            print("File opened successfully.")
            file.write("Rati:1000.0\n")
            file.write("Paata:2000.0\n")
        print(f"User data file '{file_name}' created successfully.")
    except Exception as e:
        print("An error occurred while creating the user data file:", e)

# ====================================
create_user_data_file("user_data.txt")



class ATM:
    def __init__(self, user_data_file):
        self.user_data_file = user_data_file
        self.user_data = self.load_user_data()

    def load_user_data(self):
        try:
            with open(self.user_data_file, "r", encoding="utf-8") as file:
                user_data = {}
                for line in file:
                    username, balance = line.strip().split(":")
                    user_data[username] = float(balance)
                return user_data
        except FileNotFoundError:
            print(f"User data file '{self.user_data_file}' not found.")
            return {}

    def save_user_data(self):
        with open(self.user_data_file, "w", encoding="utf-8") as file:
            for username, balance in self.user_data.items():
                file.write(f"{username}:{balance}\n")

    def check_balance(self, username):
        return self.user_data.get(username, "User not found")

    def deposit(self, username, amount):
        if username in self.user_data:
            self.user_data[username] += amount
            self.save_user_data()
            return f"Deposit of ${amount} successful. Current balance: ${self.user_data[username]}"
        else:
            return "User not found"

    def withdraw(self, username, amount):
        if username in self.user_data:
            if amount <= self.user_data[username]:
                self.user_data[username] -= amount
                self.save_user_data()
                return f"Withdrawal of ${amount} successful. Current balance: ${self.user_data[username]}"
            else:
                return "Insufficient funds"
        else:
            return "User not found"

def main():
    atm = ATM("user_data.txt")
    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

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
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



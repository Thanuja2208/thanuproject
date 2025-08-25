class ATM:
    def __init__(self):
        self.accounts = {
            "123456": {"pin": "1234", "balance": 1000},
            "987654": {"pin": "5678", "balance": 500},
        }

    def authenticate(self, account_number, pin):
        if account_number in self.accounts and self.accounts[account_number]["pin"] == pin:
            return True
        return False

    def check_balance(self, account_number):
        return self.accounts[account_number]["balance"]

    def withdraw(self, account_number, amount):
        if self.accounts[account_number]["balance"] >= amount:
            self.accounts[account_number]["balance"] -= amount
            return True
        return False

    def deposit(self, account_number, amount):
        self.accounts[account_number]["balance"] += amount
        return True


def main():
    atm = ATM()
    print("Welcome to the ATM!")

    account_number = input("Enter your account number: ")
    pin = input("Enter your PIN: ")

    if atm.authenticate(account_number, pin):
        while True:
            print("\n--- ATM Menu ---")
            print("1. Balance Inquiry")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Choose option: ")

            if choice == "1":
                print("Balance:", atm.check_balance(account_number))
            elif choice == "2":
                amount = float(input("Enter deposit amount: "))
                atm.deposit(account_number, amount)
                print("Deposit Successful!")
            elif choice == "3":
                amount = float(input("Enter withdrawal amount: "))
                if atm.withdraw(account_number, amount):
                    print("Withdrawal Successful!")
                else:
                    print("Insufficient Balance!")
            elif choice == "4":
                print("Thank you for using ATM. Goodbye!")
                break
            else:
                print("Invalid option. Try again.")
    else:
        print("Authentication Failed. Invalid Account or PIN.")


main()

class BankAccount:

    def __init__(self, account_holder, balance=0):
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}")

    def withdraw(self, amount):

        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient Balance")

    def get_balance(self):
        return self.__balance

    def display_account(self):
        print(f"Account Holder: {self.__account_holder}")
        print(f"Balance: ₹{self.__balance}")
from person import Person
from bank_account import BankAccount

print("===== Person Demo =====")

person = Person("Deepu", 32)

person.introduce()

person.set_age(33)

print("Updated Age:", person.get_age())


print("\n===== Bank Account Demo =====")

account = BankAccount("Deepu", 10000)

account.display_account()

account.deposit(5000)

account.withdraw(3000)

print("Current Balance:", account.get_balance())
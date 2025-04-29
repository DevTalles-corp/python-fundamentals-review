
class BankAccount:
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance  # Encapsulación

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Saldo insuficiente o monto inválido.")

    def check_balance(self):
        return f"Saldo actual: ${self.__balance}"


account = BankAccount("Ricardo", 1000)  # Abstracción

account.deposit(500)
# account.withdraw(700)

print(account.check_balance())

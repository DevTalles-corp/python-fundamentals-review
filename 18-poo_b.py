from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, owner, initial_balance):
        self.owner = owner
        self.__balance = initial_balance  # Encapsulación

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def _get_balance(self):
        return self.__balance

    def _set_balance(self, new_balance):
        self.__balance = new_balance

    @abstractmethod
    def withdraw(self, amount):
        pass  # Polimorfismo

    def check_balance(self):
        return f"Saldo actual: ${self.__balance}"


class SavingAccount(BankAccount):  # Herencia
    def withdraw(self, amount):
        penalty = amount * 0.05
        total = amount + penalty
        if total <= self._get_balance():
            self._set_balance(self._get_balance() - total)
        else:
            print("Fondos insuficientes en la cuenta de ahorro")


class PayrollAccount(BankAccount):  # Herencia
    def withdraw(self, amount):
        if amount <= self._get_balance():
            self._set_balance(self._get_balance() - amount)
        else:
            print("Fondos insuficientes en la cuenta de nómina")


savings = SavingAccount("Ricardo", 1000)
payroll = PayrollAccount("Ricardo", 1000)

savings.withdraw(100)
payroll.withdraw(100)

print("Cuenta de ahorro: ", savings.check_balance())
print("Cuenta de nómina: ", payroll.check_balance())

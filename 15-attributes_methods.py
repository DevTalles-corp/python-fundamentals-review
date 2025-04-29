
class Person:
    species = "Humano"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._energy = 100
        self.__password = "1234"

    def work(self):
        return f"{self.name} está trabajando duro."

    def _waste_energy(self, quantity):
        self._energy -= quantity
        return self._energy

    def __generate_password(self):
        return f"$${self.name}{self.age}$$"


person1 = Person("Ricardo", 29)
person2 = Person("Fernando", 16)

print(person1.work())
print(person1._waste_energy(10))
# print(person1.__generate_password())
print(person2.work())

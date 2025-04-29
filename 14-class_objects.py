
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        return f"{self.name} está trabajando duro."


person1 = Person("Ricardo", 29)
person2 = Person("Fernando", 16)

print(person1.work())
print(person2.work())

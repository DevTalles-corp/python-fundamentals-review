
class Person:
    species = "Humano"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

    @staticmethod
    def is_older(age):
        return age >= 18


person1 = Person("Ricardo", 29)
person2 = Person("Fernando", 35)

print(person1.species)
print(person2.species)

Person.change_species("Reptiliano")

print(person1.species)
print(person2.species)

print(Person.is_older(20))
print(person1.is_older(person1.age))

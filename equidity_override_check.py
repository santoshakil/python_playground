class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)
p2 = Person("John", 36)

print(p1 == p2)  # False


class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


p3 = Person2("John", 36)
p4 = Person2("John", 36)

print(p3 == p4)  # True

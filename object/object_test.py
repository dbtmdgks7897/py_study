from animal import Animal
from cat import Cat
from dog import Dog

Animal.hello()

print()

a = Animal(12)
b = Cat("나옹", 5)
c = Dog(age = 7)

a.eat()
b.eat()
c.eat()

print()

a.get_age()
b.get_age()
c.get_age()



print()

Animal.get_count()
Cat.get_count()
Dog.get_count()
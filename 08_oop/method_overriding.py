# Method overriding: Animal -> Dog / Cat

class Animal:
    def sound(self):
        print("Some animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow!")

for animal in (Animal(), Dog(), Cat()):
    animal.sound()

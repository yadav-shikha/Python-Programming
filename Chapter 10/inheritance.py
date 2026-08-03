# Without Inheritance
class Animal:
    def eat(self):
        print('Eating')
class Dog:
    def eat(self):
        print('Eating')      
#   with inheritance


class Animal:
    def eat(self):
        print('Eating')
class Dog(Animal):
    pass
d1 = Dog()
d1.eat()


# 
class Person:
    def speak(self):
        print('Speaking')
class Student(Person):
    pass
s1 = Student()
s1.speak()        


class Animal:
    def eat(self):
        print('Eating')
class Dog(Animal):
    def bark(self):
        print('Dog bark')
d1 = Dog()
d1.eat()
d1.bark()

# Method Overriding


class Animal:
    def sound(self):
        print('Animal Sound')

class Dog(Animal):
    def sound(self):
        print('bark')
d1 = Dog()
d1.sound()


# 🤔 Ab Problem

# Maan lo Parent ka method bhi chalana hai aur Child ka bhi.
class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        super().sound()     # Parent ka method
        print("Bark bark")       # Child ka method


d1 = Dog()

d1.sound()


class Person:
    def show(self):
        print('I am a person')
class Student(Person):
    def show(self):
        super().show()
        print('I am a student')       

s1 = Student()
s1.show()         

class Animal:
    def eat(self):
        print('Eating')
class Dog(Animal):
    def eat(self):
        super().eat()
        print('Dog is eating') 
d1 = Dog()
d1.eat()               
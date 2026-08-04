# instance method 
class Person:
    def __init__(self):
        print('person created')
Person()       

class Student:
    school = 'abc school'
    @classmethod
    def show_school(cls):
        print(cls.school)
Student.show_school()        

class Car:
    @staticmethod
    def welcome():
        print('Welcome to python')
Car.welcome()        



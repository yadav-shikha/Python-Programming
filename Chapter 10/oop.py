class Student:
    def __init__(self):
        print('Student Created')
        self.name = 'Shikha',
        self.age = 23

s1 = Student()
# s2 = Student()
# s3 = Student()
print(s1.name,s1.age)
# print(s)


class Student1:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def study(self):
        print(self.name ,'is studying')

s2 = Student1('Shikha',23)
s3 = Student1('Saurabh',34)
print(s2.name, s2.age)    
print(s3.name, s3.age)    

s2.study()
s3.study()


class Car:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def start(self):
        print(self.brand , "started")
    def stop(self):
        print(self.brand,"stopped")    
c1 = Car("BMW","Black")
c2 = Car("Audi","White")
print(c1.brand)
print(c2.brand,c2.color)

c1.start()
c2.stop()


class Student:
    pass
s1 = Student()
class Car:
    pass
c1 = Car()
print(c1)
class Mobile:
    pass
m1 = Mobile()
m2 = Mobile()
m3 = Mobile()
print(m1)
print(m2)
print(m3)
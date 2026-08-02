# name = "Shikha"
# age = 25
# course = "Python"

# name2 = "Rahul"
# age2 = 20
# course2 = "Java"

# name3 = "Aman"
# age3 = 23
# course3 = "C++"
# Step 4: Class Kya Hoti Hai?
class Student:
    pass
# Step 5: Object Kya Hota Hai?
s1 = Student()
# Step 6: Ek se jyada object
s2 = Student()
s3 = Student()

# Step 7: Class ke andar Data kaise rakhte hain?
# constructor
class Student:
    def __init__(self):
        print('Student created')

s1 = Student()
print(s1)
# Step 8: init ka use
class Student:
    # Step 9: self kya hota hai?
    def __init__(self):
        self.name = 'shikha'
        self.age = 23
s1 = Student()
print(s1.name)
print(s1.age)        

# Step 10: Hardcoding nahi karenge

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    # Step 11: Methods
    def study(self):
        print(f"{self.name} is studying")
s1 = Student('shivay',2)
print(s1.name)
print(s1.age)           
s2 = Student('shivanya',2)
print(s2.name)
s1.study()



# Ab Next Topic
# Class Variable
class Student:
    school = 'Abc school'
    def __init__(self,name):
        self.name = name
s1 = Student('Dimpal')
s2 = Student('Preyasi')
print(s1.name, s1.school)
print(s2.name, s2.school)

class Student:
    school = 'Abc school'
    def __init__(self,name):
        self.name = name
        Student.school = 'xyz school'
        s1.school = 'pqr school'
 
s1 = Student('Dimpi')
s2 = Student('Priyu')
print(s1.name, s1.school)
print(s2.name, s2.school)
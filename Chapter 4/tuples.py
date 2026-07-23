fruits = ('Apple','Banana','Grapes','litchi')
print(fruits)
print(len(fruits))
# indexing
print(fruits[0])
print(fruits[-2])
print(fruits.index('Grapes'))
# slicing
print(fruits[1:3])
print(fruits[:3])
print(fruits[0:])
# type
print(type(fruits))
num = (5)
print(type(num))
num2 = (5,)
print(type(num2))
# tuple unpacking
student = ('shikha',23,'Python Programming')
name , age, course = student
print(name)
print(age)
print(course)
# Tuple Methods & Advanced Concepts
numbers = (0,10,20,30,20,60,30)
print(numbers.count(20))
print(student+numbers)
c = 'python'
print(c*3)
print("Banana" in fruits)
print("Avokado" is not fruits)
for i in numbers:
    print(i)
nested = (
    ('shikha',23),
    ('anjali',22),
    ('peeyush',26)
)    
print(nested[0][0])
# sorted
print(sorted(numbers))
# reverse order
print(sorted(numbers, reverse=True))
print(min(numbers))
print(max(numbers))
print(any(numbers))
print(all(numbers))
# Q1. Tuple immutable hai, phir data kaise change karenge?
lst = list(numbers)
lst[0] = 96
print(lst)
print(numbers)
tup = tuple(lst)
print(tup)
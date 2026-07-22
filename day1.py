print('Hello world!')
# takes input from user
# name = input('Enter your name : ')
# print("Hello "+name+" welcome!")

# x,y = input('Inter two numbers : ').split()
# print("x = ",x,"y = ",y)
# p = 10
# print(p)
# p = 'shikha'
# print(p)

# operator
# arithmatic operator
# n1 = 40
# n2 = 18
# print(n1+n2)
# print(n1-n2)
# print(n1*n2)
# print(n1/n2)
# print(n1//n2)
# print(n1%n2)
# print(n1**n2)

# comparison operator
# print(n1>n2)
# print(n1<n2)
# print(n1==n2)
# print(n1>=n2)
# print(n1<=n2)
# print(n1!=n2)

x = True
y = False
# print(x and y)
# print(x or y)
# print(not x)

# Identity Operators

a = 10
b = 20
c = a
# print(c is not a)
# print(c is a)
# print(a is b)

# Menbership Operator
# mylist = [10,21,22,85]
# if (a not in mylist):
    # print('a is not present in given list')
# else:
    # print('a is present in given list')    


# Ternary Operator
# res = 'big' if a>b else 'small'
# print(res)
   
# conditionals statement
number = 11
if number>10:
    print('number is greater then 10')   


# if else
if number <10:
    print('Number is less then 10')
else:
    print('Number is greater than 10')    

# if elif else
if number ==0:
   print('Number is zero')
elif number>10:
    print('number is greater than 10')   
else:
    print('number is less than 10')    

# nested if else
age = 2
isID = True
if age >18:
    if isID==True:
        print('you can vote')
    else:
        print('you can not vote')    
else:
    print('your age less')        

# match case
number = 1
match number:
    case 1:
        print('number one') 
    case 2:
        print('number two')   
    case 3:
        print('number 3')
    case _:
        print('INvalid number')         
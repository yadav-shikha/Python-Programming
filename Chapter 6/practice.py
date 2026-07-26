# 1. Write a program to find the greatest of four numbers entered by the user.
n1 = int(input('Enter Your First Number : '))
n2 = int(input('Enter Your Second Number : '))
n3 = int(input('Enter Your Third Number : '))
n4 = int(input('Enter Your Fourth Number : '))
if n1>n2 and n1>n3 and n1>n4:
    print(f"N1 : {n1} is greatest")
elif n2>n1 and n2>n3 and n2>n4:
    print(f"N2 : {n2} is greatest")
elif n3>n1 and n3>n2 and n3>n4:
    print(f"N3 : {n3} is greatest")
else:
    print(f"N4 : {n4} is greatest")


#  2. Write a program to find out whether a student has passed or failed if it requires a total of
# 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an
# input from the  user
mark1 = int(input('Enter Your First Number : '))
mark2 = int(input('Enter Your Second Number : '))
mark3 = int(input('Enter Your Third Number : '))
percentage = (100*(mark1+mark2+mark3))/100
if percentage>=40 and mark1>=33 and mark2>=33 and mark3>33:
    print('Pass')
else :
    print('Fail')    
    

# 3. A spam comment is defined as a text containing following keywords: “Make a lot of
# money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams


# 4. Write a program to find whether a given username contains less than 10 characters or not.
name = input('Enter your name : ')
if len(name)>=10:
    print('More than 10 character')
else:
    print('Less than 10 character')    

# 5. Write a program which finds out whether a given name is present in a list or not.
nameList = ['Shikha','Anjali','Saurabh','Shivay']
if name in nameList:
    print('present in list')    
else:
    print('Not present in list')    

# 6. Write a program to calculate the grade of a student from his marks from the following    
# scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F
mark = 58
if mark>=90 and mark<=100:
    print('Excellent')
elif mark>=80:
    print('A') 
elif mark>=70:
    print('B')   
elif mark>=60:
    print('C')   
elif mark>=50:
    print('D')   
elif mark<50:
    print('Fail')   
else:
    print('Invalid input')     

# 7. Write a program to find out whether a given post is talking about “Harry” or not.
post = 'Harry is a good teacher'
if 'Harry' in post:
    print('Talking')
else : 
    print('Not')    
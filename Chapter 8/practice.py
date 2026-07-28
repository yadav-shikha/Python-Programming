# 1. Write a program using functions to find greatest of three numbers.
def findGreatest(a,b,c):
    if a>b and a>c:
        print('a is greatest')
    elif b>a and b>c:
        print('b is greatest')
    elif c>a and c>b:
        print('c is greatest')
    else:
        print('Invalid arguments')  
findGreatest(5,4,8)                  

# 2. Write a python program using function to convert Celsius to Fahrenheit.

# 3. How do you prevent a python print() function to print a new line at the end.
print('a')
print('b')
print('c',end='')
print('d',end='')
print('e')


# 4. Write a recursive function to calculate the sum of first n natural numbers.
'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = 1 + 2 + 3 + 4.... n -1 + n
sum(n) = sum(n-1) + n
'''

def sum(n):
    if n==1:
        return 1
    return sum(n-1)+n
print(sum(5))
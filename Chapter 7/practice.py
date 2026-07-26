# 1. Write a program to print multiplication table of a given number using for loop.
number = int(input('Enter your number : '))
for i in range(1,11):
    print(f"{number}*{i}={number*i}")


# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
l = ["Harry", "Soham", "Sachin", "Rahul"]   
for i in l:
    if i.startswith('S'):
        print(f"Hello {i}")

# 3. Attempt problem 1 using while loop.
num = 10
j = 1
while j<=10:
    print(f"{num}*{j} = {num*j}")
    j +=1


# 4. Write a program to find whether a given number is prime or not.


# 5. Write a program to find the sum of first n natural numbers using while loop
sum = 0
n = 3
for i in range(1,n+1):
    sum += i
print(sum)    

# 6. Write a program to calculate the factorial of a given number using for loop.
fact = 1
# number = 3
for i in range(1,6):
    fact = fact*i
print(fact)


# 7. Write a program to print the following star pattern.
# *
# ***
# ***** for n = 3

for i in range(1,6,2):
    print('*'*i)


# 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3
for i in range(1,4):
    print('*'*i)


# 9. Write a program to print the following star pattern.
# * * *
# *   * for n = 3
# * * *
# 10. Write a program to print multiplication table of n using for loops in reversed order.
num = 3
for i in range(10,0,-1):
    print(num*i)
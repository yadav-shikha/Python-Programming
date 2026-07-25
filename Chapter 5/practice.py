# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
dis = {
    'Madad' : 'Help',
    'Achha' : 'Good',
    'Kitab' : 'Book',
    'Kursi' : 'Chair'
}
# inp = input('Enter Hindi Word : ')
# res = dis.get(inp)
# print(res)

# 2. Write a program to input eight numbers from the user and display all the unique numbers
# (once)
# n1, n2, n3, n4, n5, n6, n7, n8 = input("Enter 8 numbers: ").split()

# numbers = set()

# numbers.add(int(n1))
# numbers.add(int(n2))
# numbers.add(int(n3))
# numbers.add(int(n4))
# numbers.add(int(n5))
# numbers.add(int(n6))
# numbers.add(int(n7))
# numbers.add(int(n8))

# print(numbers)

# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
new_set = {18,'18'}
print(new_set)

# 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') 
print(len(s))

# 5. s = {}
# What is the type of 's'?
print(type(s))

# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as value and
# use key as their names. Assume that the names are unique.
fav_lang = {}

name, language = input("Enter name and language: ").split()
fav_lang[name] = language

name, language = input("Enter name and language: ").split()
fav_lang[name] = language

name, language = input("Enter name and language: ").split()
fav_lang[name] = language

name, language = input("Enter name and language: ").split()
fav_lang[name] = language

print(fav_lang)

# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
# 8. If languages of two friends are same; what will happen to the program in problem 6?
6
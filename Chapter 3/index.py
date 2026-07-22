# string
str1 = 'Helo World!'
print(str1)
str2 = "Helo Python"
print(str2)
str3 = '''Helo , 
welcome to my shikshase acedamy
Thanks
'''
print(str3)
# indexing
print(str1[0])
print(str1[9])
# Slicing with Skip Value
word = 'Amazing'
print(word[1:3])
print(word[1:8:2])
print(word[-1])
print(word[-5:-1])
# string methods
sen = ' i lovE pytHon '
print(len(sen))
print(sen.upper())
print(sen.lower())
print(sen.capitalize())
print(sen.title())
print(sen.startswith('I'))
print(sen.endswith('on'))
print(sen.swapcase())
print(sen.strip())
print(sen.lstrip())
print(sen.rstrip())
print(sen.find('on'))
print(sen.count('a'))
print(sen.replace('pytHon','JavaScript'))
print(sen.split())
print('123'.isalpha())
print('123'.isdigit())
print('S@12'.isalnum())
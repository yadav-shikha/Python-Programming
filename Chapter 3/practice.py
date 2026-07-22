# Write a python program to display a user entered name followed by Good Afternoon using input() function.
name = input('Enter your name : ')
msg = "Good Afternoon!"
print(f"{msg}  {name}")

# Write a program to fill in a letter template given below with name and date. 
letter = ''' Dear <|Name|>, You are selected! <|Date|> '''
print(letter.replace('<|Name|>','Shikha').replace('<|Date|>','10 July'))

# Write a program to detect double space in a string.
str = "Hello  Python!"
print(str)
print(str.find('  '))
# Replace the double space from problem 3 with single spaces
print(str.replace('  ',' '))
# Write a program to format the following letter using escape sequence characters. 
letter1 = "Dear Harry,\n\tthis python course is nice.\nThanks"
print(letter1)
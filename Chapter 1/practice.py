
# Write a program to print twinkle twinkle little star poem in python.
print('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the trav'ller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.

In the dark blue sky you keep,
And often thro' my curtains peep,
For you never shut your eye,
Till the sun is in the sky.

'Tis your bright and tiny spark,
Lights the trav'ller in the dark:
Tho' I know not what you are,
Twinkle, twinkle, little star.


''')

# print the table of 5 
print(5*1)
print(5*2)
print(5*3)
print(5*4)
print(5*5)
print(5*6)
print(5*7)
print(5*8)
print(5*9)
print(5*10)

# install a external module and use it  perform to operation of your interest
import pyttsx3
print("pyttsx3 installed successfully")

engine = pyttsx3.init()
engine.say ('Hello Shikha welcome to python3')
engine.runAndWait()
engine.say("""Twinkle, twinkle, little star.
hello""") #multiline ka code speech me nhi convert ho paya
engine.runAndWait()

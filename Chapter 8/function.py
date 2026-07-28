def greet():
    print('Hello')
greet()
greet()    

# 4. Function with Parameters
def greet(name):
    print(f"Hello {name}")
greet('Shikha')
greet('Shivay')    

# 7. Return Statement
def add(a,b):
    return a+b
result = add(5,6)
print(result)
# Print vs Return
# print : Ye sirf screen par dikhata hai.
# return :Ye value wapas bhejta hai.  Is value ko kahin bhi use kar sakte hain.
print(result*5)


# 8. Default Parameter
def greet(name="shikha"):
    print(f"Hello {name}")
greet()
greet('SHivay')    


# Local variable
def demo():
    x = 10
    print(x)

demo()

# Global Variable
x = 10

def demo():
    print(x)

demo()

print(x)

# 11. Function Calling Another Function
def another():
    greet()
    print('Welcome')

another()    
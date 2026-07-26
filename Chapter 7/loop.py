# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
# print("Hello")
for i in range(5):
    print('Hello')


# while loop
i = 1
while i<=5:
    print(i)
    i =i+1

# infinite loop
# while True:
#     print('Shikha')    


# for loop
for i in range(2,11,2):
    print(i)

# Loop through list
list = ['Banana','Apple','Mango']
i = 0
while i<len(list) :
    print(list[i])
    i +=1

# Using for loop
for fruit in list:
    print(fruit)

# break    
for i in range(10):
    if i==5:
        break
    print(i)

# continue
i =0
while i<10 :
    i = i+1
    if i==6:
        continue
    print(i)   

# pass  
name = ['shikha','saurabh','anjali']
for i in name:
    pass
print('Done')

# 12. else with Loop
for i in name:
    print(i)
else:
    print('Loop Finished')    
file = open('demo.txt','r')
data = file.read()
print(data)
file.close()

f = open('demo1.txt','w')
f.write('Helo Python')
# f.close()

f1 = open('demo1.txt','a')
f1.write('\nwelcome')
f1.close()


f2 = open('demo.txt','r')
print(f2.readline())
data = f2.readlines()
print(data)

f2.close()

with open('demo1.txt','a') as f:
    f.write(' Shikha yadav')
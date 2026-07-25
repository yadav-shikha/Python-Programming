sets = {5,10,10,40,20,36,30,20}
print(sets)
print(len(sets))
# print(sets[0])
sets.remove(10)
print(sets)
sets.pop()
print(sets)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A|B)
print(A&B)
print(A^B)
print(A-B)
dist = {
    'name' : 'shikha',
    'age' : 20,
    'course' : 'python'
}
print(dist)
print(type(dist))
print(dist["name"])
dist["name"] = "Dimpal"
print(dist)

print(len(dist))
print(dist.get('name'))
print(dist['name'])
# print(dist.get('city'))
# print(dist['city'])
print(dist.keys())
print(dist.values())
print(dist.items())
dist.update({'city':'Luckhnow'})
print(dist)
dist.pop('age')
print(dist)
dist.popitem()
print(dist)
new_dist = dist.copy()
print(new_dist)
dist.clear()
print(dist)
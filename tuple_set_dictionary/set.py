x = {1,2,3,5}
y ={'apple','banana','mango'}
z = {1,2,36,5,6,1,2,35,5,3}

print(x)
print(y)
print(z)
print(type(z))


a = [1,2,3,4,6,5]
b = (2,2,3,4,1,8,9)

a_set = set(a)
b_set = set(b)
print(a,a_set)
print(b,b_set)

#set values cannot be indexed or sliced

for i in a_set:
    print(i,end='')

print(set())

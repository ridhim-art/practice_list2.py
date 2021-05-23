a = {1,2,3,4,5,6,8,7}
b={1,2,3,4}
c={6,7,8,9}
d ={5,6,7,8,9}
e ={11,22,33}

e.add('apple')
c.remove(9)
d.update(1,85,96,63,55,23,5)
e.pop()

print(a)
print(b)
print(c)
print(d)
print(e)

print(a.issubset(c),'a is superset of c')
print(a.issubset(d),'a is superset of d')

if b.issubset(a):
    print("b is a subset of a")
else :
    print("b is no subset of a")

if e.issubset(d):
    print("e is a subset of d")
else :
    print("e is no subset of d")

if a.isdisjoint(e):
    print("a or e me koi rista nahi")
else:
    print("a and e are connected")        

if b.isdisjoint(d):
    print("b or d me koi rista nahi")
else:
    print("b and d are connected")        

#union ,take  every unique values from the set

print('union')
print(a.union(d))
print(a|d)

print('difference')
print(a.difference(d))
print(a-d)

print('interection')
print(a.intersection(d))
print(a&d)

print('symmetric differece')
print(a.symmetric_difference(d))
print(a ^ d)







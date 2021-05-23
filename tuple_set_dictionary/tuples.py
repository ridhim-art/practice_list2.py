x = (1,2,3,4) #tuples
y = 12,85,96,23  #called tuples

print(x)
print(y)
print(type(x))
print(type(y))

# list to couple conversion

a = [1,2,3,4]
at = tuple(a)
print(a,at)

name = 'ridhi'
namet = tuple(name)
print('string =>',name,'tuple =>',namet)

a = 1
b =2
c = 3
d = a,b,c
print(d)

#function
#count
#index
a = (1,2,8,38,5,9,5,89,9,6,1,2,95,99)
print("counting all 3s = ",a.count(3))
print("insex of 23 =",a.index(23))

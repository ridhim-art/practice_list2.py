#datatypes => python has  9 basics datatypes refers to a class written in python ,in which

#integer (int)

a = 1
b = 258924
c = +2382
d = -2589

print (type(a),type(b),type(c),type(d))

#flot
a = 1.1
b = -3.22255
c = .2358555
d = 1.2e-10

print(type(a),type(b),type(c),type(d))

#bool
a = True
b = False
c =a and b
d = a or b

print(type(a),type(b),type(c),type(d))

#string-(str)

a ='apple'
b = "basket"
c = ''' good evening'''
d = """hi
we
are
the
string
"""

print(type(a),type(b),type(c),type(d))


#nonetype
a = None
b = None
print(type(a),type(b))
z = None
print (z)

#data - structure
#list

a = [1,2,3,4,5,6]

print (type(a))

#tuple

a =(1,2,3,4,5,6)
b = 1,2,5,3
print(type(a),type(b))

#set

a = {1,2,3,4,5}
b = {1,52,8,5,96,2,656,55,8}
print(type(a),type(b))

#dict
d = {"name ": 'apple','price':200}
c = {1:1000,2:2000,3:3000}
print(type(c),type(d))

#progamatically  check  type-
a = 10
out = isinstance(a,int)
print("is an integer => ",out)

out = isinstance(a,float)
print("is a float => ",out)

price = input('enter the price of mouse you bought:')


print(isinstance(price,int))
print(isinstance(price,float))
print(isinstance(price,str))
#input is always a string
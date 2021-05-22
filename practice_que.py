# wap to find those numbers which are divisible by 7 and multiple of 5,between 1500 and 2700(both include)

for i in range(1500,2701):
    if i%7==0 and i%5==0:
       print(i)

#wap to count the numbers of even and odd numbers from a series

evencount = 0
oddcount = 0

for i in range(1,50):
    if i%2 ==0:
        evencount += 1
    else:
        oddcount += 1
print ("even numbers in the list :",evencount)
print ("odd numbers in the list:",oddcount)            

#wap to get the fibonacci series between 0 to 50. 

x,y = 0,1

while y<50:
    print(y)
    x,y = y,x+y

#wap that accepts a word from the user and reverse it.

name = input('enter the name :')

for char in range(len(name) -1,-1,-1):
    print(name[char],end = " ")
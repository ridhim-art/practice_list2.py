# wap to create a list of 50 prime numbers 

numr = 1000
l = 1
print("prime numbers:",end=' ')

for n in range(1,numr):
    if l == 50:
        break
    else:
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            print(n,end=' ')
            l+=1

# wap to create a list of names and then remove names that contain 'a' or 'o' char
names = ['DIVYA SRIVASTAVA ','AYUSHI VERMA','VAIBHAV SHRIMALI','HARSHIST TRIPATHI','NIKHIL JAISWAL','RIDHI MISHRA']

for char in names:
    print(char)
    for c in char:
        print(c)
        if (c=='a' or c=='o'):
            names.remove(char)

print(names)

# wap to create a nested list using user input,the length of list depends upon the  user
l=int(input('enter the length of nested list'))
nested=[]
for i in range(1):
    nested.append([])
    k= int(input('enter the range of list {}'.format(i)))
    for j in range(k):
        nested[i].append(j)
print(nested)



#wap to genrate a list of cricaters entered  by user only if the first letter of the name is capital.the size will depend upon user.
a= int(input('enter the total no of list you want to create '))
print('now enter the names of the criketrs one by one')
c=[]
for i in range(a):
    name=input()
    if name==name.title():
        c.append(name)
print(c)                     
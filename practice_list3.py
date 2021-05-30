#write a function to calculate area and parimeter of a rectangle.
def area_rectangle(a,b):
    area= a*b
    print('area of rectangle is ',area)

def perimeter_rectangle(a,b):
    p=2*(a+b)
    print('perimeter of rectangle is',p)

area_rectangle(4,6) 
perimeter_rectangle(3,9)

#write a function to calculate area and circumference of a circle.
def area_circle(r):
    area=3.14*r*r
    print('area of circle is',area)

def circumference_circle(r):
    c=2*3.14*r
    print('circumference of circle is',c)

area_circle(12)
circumference_circle(22)

# write a function to tell user if he/she is able  to vote or not.(consider minimum age of voting to be 18.)

def vote_elligible(a):
    if a>18 or a==18:
        print('congrats,you are elligible for vote')
    else:
        print('sorry,you cant vote')

vote_elligible(11)
vote_elligible(28)


#write a function "perfect()" that determines if perameter number is a perfect number.use this function in a program that determine and prints all the perfect numbers between 1 and 1000.

def perfect(a):
    l=[]
    for i in range(1,a):
        if (a%i == 0):
            print(i)
            l.append(i)
    if sum(l) == a:
        print(a,'is aa perfect no')
        l.append(a)
    else:
        print(a,'is not a perfect no')
    print('all perfect no are',l)

perfect(6)
perfect(12)

print('printing all perfect no in between 1 and 1000')
for i in range(1,1000):
    perfect(i)

#write a function  to find factorial of a numberbut also store the factorials calculated in a dictionary as
# done i  the fibonacci series example.

def factorial(a):
    f=1
    for i in range(1,a+1):
        f = f*1
    print('factorial of ',a,'is',f)
    return f

factorial(7)
fact={}
print('factorial of number from10 to 100')
for i in range(10,100):
    m = factorial(i)
    fact[i] = m 
print(fact)            

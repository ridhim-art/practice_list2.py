for i in range(1,102,10):
    print(str(i).ljust(5),str(i**2).rjust(10),str(1**3).rjust(10),str(i**4).rjust(10))

for i in range(1,15,2):
    print(i*'O')

for i in range(1,15,2):
    print((i*'O').rjust(15))

for i in range(1,15,2):
    print((i*'O').center(15))
            

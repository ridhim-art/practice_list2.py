def get_speed(dis, time):
    speed = dis/time
    print(f'the speed is {speed}')

#colling
get_speed(1000,40)

distance = 2000
time = 100
get_speed(distance,time)

get_speed(dis=250,time=100)
get_speed(time=100,dis=10000)

 #get_speed(200)


def pythagoras(perpendicular:int,base:int):
    hyp = (perpendicular**2+ base**2)**.5
    print(f'p={perpendicular},b={base} => h ={hyp}')

pythagoras(3,4)
pythagoras(23,34)    
class Mobile:
    def __init__(self,name,price,camera):
        self.name = name
        self.price = price
        self.camera = camera

if  __name__ == "__main__":
    m1 = Mobile('oppo',10000,32+64) 
    m2 = Mobile('vivo',10000,32+16)   

    
    print(m1.camera)
    print(m1.price)
    print(m2.camera)
    print(m1.price)

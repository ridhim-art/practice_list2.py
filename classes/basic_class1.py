# example of a simple class
class Fooditem:
    pass

# properties and behaviour

class cat:
     
     breed = 'persian'

class product:
    def help():
        print('this is class under costruction ')

####### creation object########
# object =  classmates()

maggi = Fooditem()
roti = Fooditem()
name = 'ajay'

print(type(name))
print(type(maggi))

billu = cat()
tommy = cat()

print(billu,tommy)
print(billu.breed)
print(tommy.breed)

keybord =  product()
monitor =  product()

product.help()
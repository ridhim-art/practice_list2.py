name = "alexis"

def who():
    print('who i am')
    print(f'i am {name}')

def what():
    print('what are you?')
    name = 'god king'
    print(f'I am {name}')


def update_name():
    global name
    print('old name',name)
    name = "alexander"
    print('new name',name)

who()

print('global variable =>',name)
what() 
print('global variable =>',name)


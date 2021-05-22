#question_1

msg = 'remove all the vowels from the msg '
vowels = ['a','e','i','o','u']
for i in msg:
    if i in vowels:
        msg = msg.replace(i,'')
print(msg)

#question_2
a = 0
for i in msg:
    if i in vowels:
        a+=1
print('number of all the vowels in the msg -->',1)
print(msg)        
msg = 'The more that you read, the more things you will know. The more you learn, the more places you’ll go!”'
msg2 = 'The more you give away the happier you become.’'

words = msg.split()
print(words)
print(len(words))

words2 = msg2.split('-')
print(words)
print(len(words2))

msg = "apple,banana,pasta,cheese,butter"
words = msg.split(',',3)
print(words)


msg = "apple,banana,pasta,cheese,butter"
words = msg.rplit(',',3)
print(words)
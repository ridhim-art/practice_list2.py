msg = "hello i'm learing python"

author_idx = msg.find('author')
print('author word starts at',author_idx)

and_idx = msg.find('and')
print('and occurs at index',and_idx)


and_idx = msg.find('and')
print('and occurs at index',and_idx)

and_idx = msg.find('and',10)
print('and occurs at index',and_idx)

and_idx = msg.rfind('and')
print('and occurs at index',and_idx)

and_idx = msg.index('and')
print('and occurs at index',and_idx)

writer_idx = msg.find('writer')
print('writer occurs at index',writer_idx)


deep = input("What is the Answer to the Great Question of Life... the Universe... and Everything?" ).lower().strip()
if deep=='42':
    print('Yes')
elif deep=='Forty Two':
    print('Yes')
elif deep=='forty-two':
    print('Yes')
elif deep=='forty two':
    print('Yes')
elif deep=='FoRty TwO':
    print('Yes')
else:
    print('No')
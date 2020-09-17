name=input('Enter your name :')
age=int (input('Enter your age :'))
profession=input('Enter your profession :')
retiring=int (input('Enter your retiring age :'))
yearsleft=retiring-age
print('Hello {0}, your age now is {1}. You will have to retire from{2}, {3} years from now.'.format(name,age,profession,yearsleft))
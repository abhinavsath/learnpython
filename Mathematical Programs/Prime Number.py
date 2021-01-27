num=int (input('Enter a number between 2 and 10.'))
if num > 10 or num<2:
    print('This is a number off limits. Retry again.')
else:
    if num%2 == 0 and num>2:
        print('Is not a prime number')
    elif num%3 == 0 and num!= 3:
        print('Is not a prime number')
    else:
        print('Is a prime number')

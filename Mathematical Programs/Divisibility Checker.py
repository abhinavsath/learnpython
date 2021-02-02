#Program to check whether a number is divisible by a number or not
a=int(input('Enter a number'))
b=int(input('Enter a number by which the number should be divided'))
if a%b==0:
    print ('Your number', a,' is divisible by',b)
else:
    print ('Your number', a,'is not divisible by',b)

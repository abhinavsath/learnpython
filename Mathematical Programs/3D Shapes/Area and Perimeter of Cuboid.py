Length=int(input('Enter a Length measure'))
Breadth=int(input('Enter a Breadth measure'))
Height=int(input('Enter a Height measure'))
p=4*(Length+Breadth+Height)
print ('Perimeter of the Cuboid is', p)
LB=Length*Breadth
LH=Length*Height
BH=Breadth*Height
a=2*(LB+LH+BH)
print ('Surface Area of the Cuboid is', a)
al=2*Height*(Length+Breadth)
d1=int(input('Enter the length of Diagonal 1'))
d2=int(input('Enter the length of Diagonal 2'))
ar=0.5*d1*d2
print ('Area of Rhombus is ', ar)
peri=input('Do you wish to find the perimeter of the Rhombus?')
if peri=='Yes':
    s=int(input('Enter the side of the Rhombus'))
    p=4*s
    print ('Perimeter of the Rhombus is ', p)
elif peri=='yes':
    s=int(input('Enter the side of the Rhombus'))
    p=4*s
    print ('Perimeter of the Rhombus is ', p)
elif peri=='Y':
    s=int(input('Enter the side of the Rhombus'))
    p=4*s
    print ('Perimeter of the Rhombus is ', p)
elif peri=='y':
    s=int(input('Enter the side of the Rhombus'))
    p=4*s
    print ('Perimeter of the Rhombus is ', p)
elif peri=='YES':
    s=int(input('Enter the side of the Rhombus'))
    p=4*s
    print ('Perimeter of the Rhombus is ', p)
elif peri=='No':
    print ('OK.')
    exit()
elif peri=='no':
    print ('OK.')
    exit()
elif peri=='N':
    print ('OK.')
    exit()
elif peri=='n':
    print ('OK.')
    exit()
elif peri=='NO':
    print ('OK.')
    exit()
elif peri=='Stop':
    exit()
elif peri=='stop':
    exit()
elif peri=='STOP':
    exit()
else:
    for p in peri:
        print ('Sorry. That is an invalid command.')
        peri=input('Do you wish to find the perimeter of the Rhombus?')

    
    
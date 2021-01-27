ques=input('Do you wish to find the Volume of Cube by 2D Method or via Side Method?')
if ques=='2D':
    print ('OK.')
    ba=int(input('Enter the Base Area of the Cube'))
    Height=int(input('Enter a Height measure'))
    v=ba*Height
    print ('Volume of the Cube is', v)
elif ques=='2d':
    print ('OK.')
    ba=int(input('Enter the Base Area of the Cube'))
    Height=int(input('Enter a Height measure'))
    v=ba*Height
    print ('Volume of the Cube is', v)
elif ques=='Base Area Method':
    print ('OK.')
    ba=int(input('Enter the Base Area of the Cube'))
    Height=int(input('Enter a Height measure'))
    v=ba*Height
    print ('Volume of the Cube is', v)
elif ques=='base area method':
    print ('OK.')
    ba=int(input('Enter the Base Area of the Cube'))
    Height=int(input('Enter a Height measure'))
    v=ba*Height
    print ('Volume of the Cube is', v)
elif ques=='Base Area':
    print ('OK.')
    ba=int(input('Enter the Base Area of the Cube'))
    Height=int(input('Enter a Height measure'))
    v=ba*Height
    print ('Volume of the Cube is', v)
elif ques=='Side':
    side=int(input('Enter the measure of the Side'))
    v=side**3
    print ('Volume of the Cube is', v)
elif ques=='side':
    side=int(input('Enter the measure of the Side'))
    v=side**3
    print ('Volume of the Cube is', v)
elif ques=='Side Method':
    side=int(input('Enter the measure of the Side'))
    v=side**3
    print ('Volume of the Cube is', v)
elif ques=='side method':
    side=int(input('Enter the measure of the Side'))
    v=side**3
    print ('Volume of the Cube is', v)
elif ques=='s':
    side=int(input('Enter the measure of the Side'))
    v=side**3
    print ('Volume of the Cube is', v)
elif ques=='SIDE':
    side=int(input('Enter the measure of the Side'))
    v=side**3
    print ('Volume of the Cube is', v)
else:
    for q in range (0,50):
        if ques != '2D' or '2d' or 'Base Area Method' or 'base area method' or 'Base Area' or 'Side' or 'side' or 'Side Method' 'side method' or 's' or 'SIDE':
            ques=input('Do you wish to find the Volume of Cube by 2D Method or via 3D Method?')   
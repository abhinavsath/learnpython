ques=input('Do you wish to find the Volume of Cuboid by 2D Method or via 3D Method?')
if ques=='2D':
    print ('OK.')
    ba=int(input('Enter the Base Area of the Cuboid'))
    Height=int(input('Enter a Height measure'))
    v=ba*Height
    print ('Volume of the Cuboid is', v)
elif ques=='2d':
    print ('OK.')
    ba=int(input('Enter the Base Area of the Cuboid'))
    Height=int(input('Enter a Height measure'))
    v=ba*Height
    print ('Volume of the Cuboid is', v)
elif ques=='Base Area Method':
    print ('OK.')
    ba=int(input('Enter the Base Area of the Cuboid'))
    Height=int(input('Enter a Height measure'))
    v=ba*Height
    print ('Volume of the Cuboid is', v)
elif ques=='base area method':
    print ('OK.')
    ba=int(input('Enter the Base Area of the Cuboid'))
    Height=int(input('Enter a Height measure'))
    v=ba*Height
    print ('Volume of the Cuboid is', v)
elif ques=='Base Area':
    print ('OK.')
    ba=int(input('Enter the Base Area of the Cuboid'))
    Height=int(input('Enter a Height measure'))
    v=ba*Height
    print ('Volume of the Cuboid is', v)
elif ques=='3D':
    Length=int(input('Enter a Length measure'))
    Breadth=int(input('Enter a Breadth measure'))
    Height=int(input('Enter a Height measure'))
    v=Length*Breadth*Height
    print ('Volume of the Cuboid is', v)
elif ques=='3d':
    Length=int(input('Enter a Length measure'))
    Breadth=int(input('Enter a Breadth measure'))
    Height=int(input('Enter a Height measure'))
    v=Length*Breadth*Height
    print ('Volume of the Cuboid is', v)
elif ques=='Length-Breadth-Height Method':
    Length=int(input('Enter a Length measure'))
    Breadth=int(input('Enter a Breadth measure'))
    Height=int(input('Enter a Height measure'))
    v=Length*Breadth*Height
    print ('Volume of the Cuboid is', v)
elif ques=='length-breadth-height method':
    Length=int(input('Enter a Length measure'))
    Breadth=int(input('Enter a Breadth measure'))
    Height=int(input('Enter a Height measure'))
    v=Length*Breadth*Height
    print ('Volume of the Cuboid is', v)
elif ques=='length breadth height method':
    Length=int(input('Enter a Length measure'))
    Breadth=int(input('Enter a Breadth measure'))
    Height=int(input('Enter a Height measure'))
    v=Length*Breadth*Height
    print ('Volume of the Cuboid is', v)
elif ques=='Length Breadth Height':
    Length=int(input('Enter a Length measure'))
    Breadth=int(input('Enter a Breadth measure'))
    Height=int(input('Enter a Height measure'))
    v=Length*Breadth*Height
    print ('Volume of the Cuboid is', v)
else:
    for q in range (0,50):
        if ques != '2D' or '2d' or 'Base Area Method' or 'base area method' or 'Base Area' or '3D' or '3d' or 'Length-Breadth-Height Method' 'length-breadth-height method' or 'length breadth height method' or 'Length Breadth Height':
            ques=input('Do you wish to find the Volume of Cuboid by 2D Method or via 3D Method?')   
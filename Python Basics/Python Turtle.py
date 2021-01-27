import turtle #Importing Turtle from PC Library     
turtle.shape('turtle') #Giving the shape 'Turtle' to the PC
turtle.setup(500,500) #Setting the size of the Window
turtle.turtlesize(3, 3, 2)#Setting the size of the Turtle
turtle.Screen().bgcolor('#AED9E4')#Setting the background of the Window
turtle.color('#49CD43')#Setting the colour of the Turtle.
#Colouring works in Hexa-Decimal Calculator (I used 'https://htmlcolorcodes.com/')
question=input ('Do you want to move the Turtle right, left, top or bottom? Else, do you want to quit?')
if question=='right':
    print ('OK.')
    turtle.forward(200)
    for ques in question:
        while question=='right':
          question=input ('Do you want to move the Turtle right, left, top or bottom? Else, do you want to quit?')
if question=='left':
    print ('OK.')
    turtle.back(200)
    for ques in question:
        while question=='left':
            question=input ('Do you want to move the Turtle right, left, top or bottom? Else, do you want to quit?')                      
if question=='top':
    print ('OK.')
    turtle.left(90)
    turtle.forward(200)
    for ques in question:
        while question=='top':
          question=input ('Do you want to move the Turtle right, left, top or bottom? Else, do you want to quit?')
if question=='bottom':
    print ('OK.')
    turtle.right(180)
    turtle.forward(200)
    for ques in question:
        while question=='bottom':
          question=input ('Do you want to move the Turtle right, left, top or bottom? Else, do you want to quit?')
if question=='stop':
    exit()
    



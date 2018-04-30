#This program calculate shapes

print("INSTRUCTION: Select a shape [triangle = 1, circle = 2, square = 3]")
      

shape=int(input("enter a shape "))
if      (shape == 1):
        b = input("base? ")
        h = input("height? ")
        Area = 0.5*b*h
        print(Area)
        
elif    (shape == 2):
        r = input("radius? ")
        Area = 3.142*r**2
        print (Area)

if      (shape == 3):
        l = input("lenght? ")
        Area = l**2
        print(Area)

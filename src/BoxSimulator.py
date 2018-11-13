###Tristan Jordan
###October, 13
###This program draws a box depending on given dimensions
def box():
    print('Welcome to Box Simulator 2016!')
    w=int(input("What do you want the length of your box to be?"))
    l=int(input("What do you want the width of your box to be?"))
    k=input("What keyboard character do you want to use for the box?")
    rw=(w-4)
    print(k*w)
    while (l-2)>0:
        print(k,(rw*' '),k)
        l=l-1
    print(k*w)
    print("Enjoy!")
box()

#Created by Tristan Jordan
#09/08/16
#this program will give the area of a circle based on the diameter
def area():
    d= int(input("What is the diameter of your circle in Centimeters?"))
    r= (d/2)
    a= (3.14*(r**2))
    print((a),("Centimeters"))
    area()
area()

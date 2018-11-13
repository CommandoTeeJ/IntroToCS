###Created by Tristan Jordan
###November 1
###This program will output a sphere's are and volume via the radius
import math
def spherearea(r):
    a=(4*math.pi*r*r)
    print("The area is: ",a)
def spherevolume(r):
    fr=(4/3)
    v=(fr*math.pi*r*r*r)
    print("The volume is: ",v)
def main():
    r=int(input("What is the radius? "))
    spherearea(r)
    spherevolume(r)
main()

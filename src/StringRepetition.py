#Created by Tristan Jordan
#09/08/16
#this program will take a string an repeat it a number of times
def stringrep():
    string=input("What would you like to be repeated?")
    times=int(input("How many times would you like the string to be repeated?"))
    print(string*times)
    stringrep()
stringrep()

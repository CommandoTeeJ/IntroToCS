###!= means if the two numbers aren't equal then the statement is true
###== means if the two numbers are equal then it is true
###> means it is true if the first number is greater than the second
###< means it is true if the first number is less than the second


#Tristan Jordan
#09/8/16
#This program will decide whether someone is valid based on their age
def age():
    userage= int(input("How old are you?"))
    if userage < 18:
        print("Not Valid")
    else:
        print("Valid")
    age()
age()

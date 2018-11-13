import random
###comes up with responses for unfavorable guests###
def randobad():
    x= random.randint(1,5)
    if x==1:
        print("Access Denied")
    elif x==2:
        print("Be Gone")
    elif x==3:
        print("Please Leave")
    elif x==4:
        print("Incorrect")
    elif x==5:
        print("Error")
###responses for good guests###
def randogood():
    y= random.randint(1,3)
    if y==1:
        print("You're pretty cool!")
    elif y==2:
        print("Dude I like your style!")
    elif y==3:
        print("Please come back!")
###main process
def user():
    username=input("Whats ya name?    ")
    if username=="Leeroy":
        randobad()
    elif username=="Karl":
        randobad()
    elif username=="Tristan":
        randogood()
    else: print("At least you ain't Leeroy or Karl")
    user()
user()

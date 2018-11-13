###Created By Tristan Jordan
###October, 18
###This Program Counts the length of a string
def lengththing():
    s=input("Enter a sentence: ")
    c=len(s)
    sp=s.split()
    spc=len(sp)
    print(c,' Characters ',spc,' Words ')
    lengththing()
lengththing()

###Created by Tristan Jordan
###October, 18
###This Program Will Make Acronyms
def acros():
    f=" "
    l=0
    w=0
    p=0
    t=input("What would you like to make into an acronym?")
    c=t.title()
    r=c.split()
    z=len(r)
    while z>0:
        l=r[0+p]
        q=l[0]
        f=f+q
        z=z-1
        p=p+1
    print(f)
    acros()
acros()

def ShowNumbers():
    num=int(input("enter"))
    i=0
    while i<=num:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i+=1
ShowNumbers()
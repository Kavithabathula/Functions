def fun():
    num=int(input("enter"))
    a=[1,2,3,4,5,6,7,8,9]
    i=0
    while i<len(a):
        if num==a[i]:
            print("true")
        else:
            print("false")
        i+=1
fun()
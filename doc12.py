def a_q():
    a=[120,340,560,4050,570]
    i=0
    d=0
    while i<len(a):
        b=str(a[i])
        c=""
        j=0
        while j<len(b):
            if b[j]!=0:
                c=c+b[j]
            j+=1
        d.append(int(c))
        i+=1
    print(d)
    print(a[i])
a_q()
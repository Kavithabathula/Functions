# def string_reverse(str1):   
#     rstr1 = ''
#     index = len(str1)
#     while index > 0:
#         rstr1 += str1[ index - 1 ]
#         index = index - 1
#     return rstr1
# print(string_reverse('1234abcd'))


def fun(rev):
    a=""
    i=0
    while i>len(a):
        a=rev[i]
        i-=1
    return(a)
print(fun("1234abcd"))
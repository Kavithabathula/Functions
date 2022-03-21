def pattern(number):
    if number == 1:
        return 1
    else:
        return pattern(number-1) + 3
print(pattern(6))


# i=0
# while i<=10:
#     n=int(input("enter"))
#     if n<3:
#         print("smaller",n)
#     else:
#         print("bigger",n)
#     i+=1
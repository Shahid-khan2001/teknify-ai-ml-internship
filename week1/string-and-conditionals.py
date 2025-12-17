a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number: "))
# a b c d
if (a == 0 and b == 0 and c == 0 and d ==0):
    print("please enter valid numbers")

else:
    if (a>b and a>c and a>d):
        print("a is the greatest number", a)
    elif(b>c and b>d):
        print("b is the greatest number", b)
    elif(c>a and c>d):
        print("c is the greatest number", c)
    else:
        print("d is the greatest number", d)
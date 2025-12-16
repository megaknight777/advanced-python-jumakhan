a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))

if a<b and b<c:
    print(c-a)

elif a<b and b>c:
    print(b-a)

elif c<b and b>a:
    print(b-c)

elif c<b and b<a:
    print(a-c)

elif a>b and b<c:
    print(a-b)

elif a>b and b>c:
    print(a-c)

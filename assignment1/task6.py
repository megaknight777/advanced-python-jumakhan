a=int(input("First number: "))
b=int(input("Second number: "))
c=input("What operation: [+, -, *, /] ")
if c=="+":
   print(a+b)
elif c=="-":
   print(a-b)
elif c=="*":
   print(a*b)
elif c=="/":
    print(a/b)
else:
   print("Invalid operation")

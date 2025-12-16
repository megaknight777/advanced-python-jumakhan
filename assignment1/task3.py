num=float(input("enter xx.xx number: "))
integer_part=int(num)
fractional_part=num-integer_part
a=integer_part * 0.01
b=fractional_part * 100
print(round(a+b, 2))

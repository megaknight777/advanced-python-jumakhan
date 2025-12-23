# The equation for fifth-graders is a string five characters long.
# The second character is either a '+' (plus) or '-' (minus),
# and the fourth character is an '=' (equal) sign.
# Of the first, third, and fifth characters, exactly two are digits from 0 to 9,
# and one is the letter x, representing the unknown.
# You are required to write a program that will solve this equation for x.

# i:x+5=7 ; o:2
# i:3-x=9 ; o:-6

s = input() # Вводим строку целиком, например "3-x=9"

# Разбираем строку на части
# a[0] +/-[1] b[2] =[3] c[4]
# s[0] - первое число/x
# s[1] - знак (+ или -)
# s[2] - второе число/x
# s[3] - всегда знак равно =
# s[4] - ответ/x (индекс 3 пропускаем, там всегда '=')

# ВАРИАНТ 1: Если x стоит в самом конце (например, "2+3=x")
if s[4] == 'x':
    num1 = int(s[0])
    num2 = int(s[2])
    if s[1] == '+':
        print(num1 + num2)
    else:
        print(num1 - num2)

# ВАРИАНТ 2: Если x стоит первым (например, "x+5=7")
elif s[0] == 'x':
    num2 = int(s[2])
    res = int(s[4])
    # Если было x + 5 = 7, то x = 7 - 5
    if s[1] == '+':
        print(res - num2)
    # Если было x - 5 = 7, то x = 7 + 5
    else:
        print(res + num2)

# ВАРИАНТ 3: Если x стоит посередине (например, "8-x=3")
elif s[2] == 'x':
    num1 = int(s[0])
    res = int(s[4])
    # Если 5 + x = 7, то x = 7 - 5
    if s[1] == '+':
        print(res - num1)
    # Если 8 - x = 3, то x = 8 - 3
    else:
        print(num1 - res)

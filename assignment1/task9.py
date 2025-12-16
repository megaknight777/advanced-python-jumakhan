number = 123420
number_to_string = str(number)

# Разрезаем вручную
first_half = number_to_string[:3]  # "123"
second_half = number_to_string[3:] # "420"

# Считаем сумму первой половины через знакомый тебе цикл
sum1 = 0
for char in first_half:
    sum1 += int(char)

# Считаем сумму второй половины
sum2 = 0
for char in second_half:
    sum2 += int(char)

# Сравниваем
if sum1 == sum2:
    print("Lucky!")
else:
    print("Not lucky")

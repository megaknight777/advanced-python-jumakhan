# the substrings and cyclic shifts task one

# substrings это как самые близкие соседи, а не соседей не берем:
# "abcd" = "a","ab","abc","abcd","b","bc","bcd","c","cd","d"

# cyclic shifts это полный круг по буквам, каждый символ превращается в самый конец, пока они не вернутся
# в исходное состояние:
# "abcd" = "abcd", "bcda", "cdab", "dabc", "abcd"


# ## !!! является ли строка s2 циклическим сдвигом строка s1?
# s1 = "abcde"
# s2 = "cdeab"
# if len(s1) == len(s2) and s2 in (s1 + s1): # (s1+s1)="abcdeabcde" это содержит в себе абсолютно все возможные
#     # циклические сдвиги исходной строки s1 как подстроки
#     print(f"'{s2}' - циклический сдвиг '{s1}'") # Вывод: 'cdeab' - циклический сдвиг 'abcde'
# else:
#     print(f"'{s2}' - не является циклическим сдвигом '{s1}'")


# ## !!! циклический сдвиг как работает и отображается
# s = "abcd"
# shifts_list = [] #это пустой список для хранение строк
# n = len(s) # n=4
#
# print(f"--- Циклические сдвиги для '{s}' (Возвращение в исходное положение) ---")
#
# for i in range(n): #for i in range(4), цикл for будет повторять свой код 4 раза,
# и на каждой интерации переменная i ,будет принимать след значение из этой последовательности
#     # s[i:] берет часть с текущего индекса до конца #s[1:]=bcd
#     # s[:i] берет часть с начала до текущего индекса #s[:1]=a
#     shifted_s = s[i:] + s[:i] #s[1:]+s[:1]=bcd+a=bcda
#     shifts_list.append(shifted_s) #shifts_list=bcda
##               .append -> добавляет новый элемент в конец спска
#     print(f"Сдвиг {i+1}: {shifted_s}") #=bcda
#
# print(f"Полный цикл: {shifts_list}")


# ## !!! отображение подстрок (substrings)
# s = "abcd"
# substrings_list = []
#
# print(f"--- Подстроки для '{s}' (Все возможные соседи) ---")
#
# for i in range(len(s)):       # i = начальный индекс (0, 1, 2, 3)
#     for j in range(i + 1, len(s) + 1): # j = конечный индекс (i+1 до 4)
#         substring = s[i:j]
#         substrings_list.append(substring)
#         print(f"Подстрока: {substring}")
#
# print(f"Все подстроки: {substrings_list}")


## # task 2
a = input()  # Считываем a
b = input()  # Считываем b

b_len = len(b)
a_len = len(a)

# 1. Генерируем все уникальные сдвиги (как в твоем коде)
b_shifts = set()
for i in range(b_len):
    shift = b[i:] + b[:i]
    b_shifts.add(shift)

count = 0

# 2. Проходимся по строке 'a' с "окошком" размером с 'b'
# Мы идем от 0 до того момента, пока "окно" помещается в строку
for i in range(a_len - b_len + 1):
    # Вырезаем кусочек (подстроку) из a
    sub = a[i: i + b_len]

    # Проверяем, есть ли этот кусочек в нашем списке сдвигов
    if sub in b_shifts:
        count += 1

print(count)

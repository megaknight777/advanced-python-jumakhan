# 1. Считываем две строки
s1 = input()
s2 = input()

# 2. Сравниваем их отсортированные версии
# sorted("BABA") превратится в ['A', 'A', 'B', 'B']
if sorted(s1) == sorted(s2):
    print("YES")
else:
    print("NO")

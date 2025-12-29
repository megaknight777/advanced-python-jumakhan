# Задание 6.

# 1. Напишите программу для нахождения наибольшего общего делителя (НОД) 
# и наименьшего общего кратного (НОК) двух натуральных чисел.
# НОК(A, B) = (A*B)/НОД(A,B). Используйте подпрограмму алгоритма Евклида для определения НОД.

# 2. Напишите программу для вычисления площади выпуклого четырехугольника, 
# если известны длины четырех сторон и диагонали.

import math
def euclid_gcd(a, b):
    """Находит НОД (GCD) по алгоритму Евклида"""
    while b != 0:
        a, b = b, a % b
    return a

def heron_area(s1, s2, s3):
    """
    Считает площадь треугольника по формуле Герона.
    Принимает длины трех сторон.
    """
    p = (s1 + s2 + s3) / 2
    
    val = p * (p - s1) * (p - s2) * (p - s3)
    
    if val < 0:
        return 0 # Невозможный треугольник
        
    return math.sqrt(val)

def solve_gcd_lcm():
    print("\n=== ЧАСТЬ 1: НОД и НОК (GCD & LCM) ===")
    try:
        num1 = int(input("Введите первое натуральное число: "))
        num2 = int(input("Введите второе натуральное число: "))
        
        if num1 <= 0 or num2 <= 0:
            print("Числа должны быть натуральными (больше 0).")
            return

        # 1. Находим НОД (GCD)
        gcd_val = euclid_gcd(num1, num2)
        
        # 2. Находим НОК (LCM) по формуле: (A * B) / GCD
        # Используем // для целочисленного деления
        lcm_val = (num1 * num2) // gcd_val
        
        print(f"НОД (GCD): {gcd_val}")
        print(f"НОК (LCM): {lcm_val}")
        
    except ValueError:
        print("Ошибка: введите целые числа.")


def solve_quadrilateral_area():
    print("\n=== ЧАСТЬ 2: Площадь четырехугольника ===")
    print("Представьте четырехугольник со сторонами A, B, C, D и диагональю L.")
    print("Диагональ делит его на два треугольника: (A, B, L) и (C, D, L).")
    
    try:
        # Ввод данных
        a = float(input("Сторона A: "))
        b = float(input("Сторона B: "))
        c = float(input("Сторона C: "))
        d = float(input("Сторона D: "))
        diag = float(input("Диагональ: "))
        
        # Логика: Сумма площадей двух треугольников
        # Треугольник 1: стороны a, b, diag
        area1 = heron_area(a, b, diag)
        
        # Треугольник 2: стороны c, d, diag
        area2 = heron_area(c, d, diag)
        
        total_area = area1 + area2
        
        if area1 == 0 or area2 == 0:
            print("\nВнимание: С такими сторонами треугольник построить нельзя!")
        else:
            print(f"\nПлощадь 1-го треугольника: {area1:.2f}")
            print(f"Площадь 2-го треугольника: {area2:.2f}")
            print(f"--> Общая площадь четырехугольника: {total_area:.2f}")

    except ValueError:
        print("Ошибка: введите числа.")

def main():
    solve_gcd_lcm()
    print("-" * 30)
    solve_quadrilateral_area()

if __name__ == "__main__":
    main()

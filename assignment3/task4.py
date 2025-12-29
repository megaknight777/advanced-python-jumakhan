# Задание 4.

# 1. Даны две дроби A/B и C/D (A, B, C, D — натуральные числа). 
# Напишите программу для деления дроби на дробь. 
# Ответ должен быть несократимой дробью. 
# Используйте подпрограмму алгоритма Евклида для определения наибольшего общего делителя (НОД).

# 2. Дана окружность (xa)² + (yb)² = R² и точки Р(р1, р2), F(f1, f1), L(l1,l2). 
# Найдите и отобразите на экране, сколько точек лежит внутри окружности. 
# Проверка на принадлежность точки к окружности должна выполняться в виде процедуры.


# --- ИНСТРУМЕНТЫ (ФУНКЦИИ) ---

def euclid_gcd(n, m):
    """
    Алгоритм Евклида для поиска НОД (GCD).
    Находит самое большое число, на которое делятся и n, и m.
    """
    while m != 0:
        # Стандартная формула: (a, b) -> (b, a % b)
        n, m = m, n % m
    return n

def check_point_inside(x, y, center_a, center_b, radius_sq):
    """
    Проверяет, лежит ли точка (x, y) внутри круга.
    Возвращает True или False.
    radius_sq - это радиус в квадрате (чтобы не считать корни лишний раз).
    """
    # Формула: (x-a)^2 + (y-b)^2
    distance_squared = (x - center_a)**2 + (y - center_b)**2
    
    # Если расстояние меньше радиуса (в квадрате), значит точка внутри
    if distance_squared < radius_sq:
        return True
    else:
        return False

# --- ЗАДАЧА 1: ДРОБИ ---
def solve_fractions():
    print("\n=== ЧАСТЬ 1: Деление дробей (A/B) / (C/D) ===")
    try:
        # Ввод данных
        print("Введите первую дробь A/B:")
        A = int(input("  A: "))
        B = int(input("  B: "))
        print("Введите вторую дробь C/D:")
        C = int(input("  C: "))
        D = int(input("  D: "))
        
        if B == 0 or D == 0 or C == 0:
            print("Ошибка: Деление на ноль невозможно!")
            return

        # 1. Логика деления: (A*D) / (B*C)
        res_numerator = A * D   # Новый числитель
        res_denominator = B * C # Новый знаменатель
        
        # 2. Сокращение дроби через Алгоритм Евклида
        common_divisor = euclid_gcd(res_numerator, res_denominator)
        
        # Делим на НОД. Используем // для целочисленного деления
        final_num = res_numerator // common_divisor
        final_den = res_denominator // common_divisor
        
        print(f"\nРезультат деления: {res_numerator}/{res_denominator}")
        print(f"После сокращения (Несократимая дробь): {final_num}/{final_den}")
        
    except ValueError:
        print("Пожалуйста, вводите целые числа.")

# --- ЗАДАЧА 2: КРУГ ---
def solve_circle_points():
    print("\n=== ЧАСТЬ 2: Точки в круге ===")
    
    # 1. Параметры круга
    print("Параметры круга (x-a)^2 + (y-b)^2 = R^2")
    a = float(input("  Введите центр a: "))
    b = float(input("  Введите центр b: "))
    r = float(input("  Введите радиус R: "))
    
    # Сразу возведем радиус в квадрат, чтобы сравнивать быстрее
    r_squared = r ** 2
    
    points_inside = 0
    
    # 2. Проверка точек P, F, L
    # Используем цикл, чтобы не писать один и тот же код 3 раза
    point_names = ['P', 'F', 'L']
    
    for name in point_names:
        print(f"Координаты точки {name}:")
        px = float(input("  x: "))
        py = float(input("  y: "))
        
        # Вызов процедуры проверки
        is_inside = check_point_inside(px, py, a, b, r_squared)
        
        if is_inside:
            print(f"  -> Точка {name} ВНУТРИ круга.")
            points_inside += 1
        else:
            print(f"  -> Точка {name} СНАРУЖИ (или на границе).")
            
    print(f"\nВсего точек внутри круга: {points_inside}")

# --- MAIN ---
def main():
    solve_fractions()
    print("-" * 30)
    solve_circle_points()

if __name__ == "__main__":
    main()

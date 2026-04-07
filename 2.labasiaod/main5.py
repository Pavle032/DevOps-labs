import time

# СПОСОБ 1: Обычный (цикл)
def power_simple(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

# СПОСОБ 2: Быстрый (рекурсия)
def power_fast(base, exp):
    if exp == 0:
        return 1
    
    if exp % 2 == 0:
        half = power_fast(base, exp // 2)
        return half * half
    else:
        return base * power_fast(base, exp - 1)

# Функция для замера времени выполнения
def measure_time(func, base, exp):
    start = time.perf_counter()
    result = func(base, exp)
    end = time.perf_counter()
    return result, end - start

# Тестирование с замером времени
print("=" * 50)
print("СРАВНЕНИЕ АЛГОРИТМОВ ВОЗВЕДЕНИЯ В СТЕПЕНЬ")
print("=" * 50)

# Тест 1: 2^10
base, exp = 2, 10
res_simple, time_simple = measure_time(power_simple, base, exp)
res_fast, time_fast = measure_time(power_fast, base, exp)

print(f"\n{base}^{exp} = {res_simple}")
print(f"Обычный метод: {time_simple:.10f} сек")
print(f"Быстрый метод: {time_fast:.10f} сек")
print(f"Разница: {abs(time_simple - time_fast):.10f} сек")

# Тест 2: 2^20
base, exp = 2, 20
res_simple, time_simple = measure_time(power_simple, base, exp)
res_fast, time_fast = measure_time(power_fast, base, exp)

print(f"\n{base}^{exp} = {res_simple}")
print(f"Обычный метод: {time_simple:.10f} сек")
print(f"Быстрый метод: {time_fast:.10f} сек")
print(f"Разница: {abs(time_simple - time_fast):.10f} сек")

# Тест 3: 2^100 (для наглядности разницы)
base, exp = 2, 100
res_simple, time_simple = measure_time(power_simple, base, exp)
res_fast, time_fast = measure_time(power_fast, base, exp)

print(f"\n{base}^{exp} = {res_simple}")
print(f"Обычный метод: {time_simple:.10f} сек")
print(f"Быстрый метод: {time_fast:.10f} сек")
print(f"Разница: {abs(time_simple - time_fast):.10f} сек")

# Тест 4: 2^1000 (очень большая степень)
base, exp = 2, 1000
res_simple, time_simple = measure_time(power_simple, base, exp)
res_fast, time_fast = measure_time(power_fast, base, exp)

print(f"\n{base}^{exp} (только время, число огромное):")
print(f"Обычный метод: {time_simple:.6f} сек")
print(f"Быстрый метод: {time_fast:.6f} сек")
print(f"Быстрее в {time_simple/time_fast:.1f} раз!")

print("\n" + "=" * 50)
print("Анализ результатов:")
print("=" * 50)
print("• Обычный метод (цикл): делает exp умножений → O(n)")
print("• Быстрый метод (рекурсия): использует подход 'разделяй и властвуй' → O(log n)")
print("• Для больших степеней разница становится ОГРОМНОЙ!")
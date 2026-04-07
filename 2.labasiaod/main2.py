import time

def fact_cycle(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fact_rec(n):
    if n <= 1:
        return 1
    return n * fact_rec(n - 1)

# Функция для точного замера времени
def measure_time(func, n, iterations=10000):
    """Запускает функцию iterations раз и возвращает среднее время"""
    # Прогрев (чтобы исключить накладные расходы)
    for _ in range(1000):
        func(n)
    
    # Замер
    start = time.perf_counter()
    for _ in range(iterations):
        func(n)
    end = time.perf_counter()
    
    return (end - start) / iterations  # среднее время на один вызов

print("СРАВНЕНИЕ ФАКТОРИАЛОВ (среднее время на 1 вызов)")
print("=" * 60)
print(f"{'n':<6} {'Цикл (сек)':<15} {'Рекурсия (сек)':<18} {'Разница':<10}")
print("-" * 60)

for n in [5, 10, 20, 100, 500, 1000]:
    # Для больших n уменьшаем количество итераций
    iterations = 1000 if n > 100 else 10000
    
    # Пропускаем рекурсию для 1000 (она упадет)
    if n <= 500:
        rec_time = measure_time(fact_rec, n, iterations)
    else:
        rec_time = float('inf')
    
    cycle_time = measure_time(fact_cycle, n, iterations)
    
    # Форматируем вывод
    cycle_str = f"{cycle_time:.2e}" if cycle_time < 0.001 else f"{cycle_time:.8f}"
    rec_str = f"{rec_time:.2e}" if rec_time < 0.001 else f"{rec_time:.8f}"
    
    print(f"{n:<6} {cycle_str:<15} {rec_str:<18} ", end="")
    
    if n <= 500:
        ratio = rec_time / cycle_time
        print(f"в {ratio:.1f} раз рекурсия медленнее")
    else:
        print("рекурсия не работает")
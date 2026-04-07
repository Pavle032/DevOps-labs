import random

def multiply_random(n):
    # Базовый случай: если число стало большим, останавливаемся
    if n > 1000:
        return n
    
    # Умножаем на случайное число от 2 до 5
    coef = random.randint(2, 5)
    print(f"{n} × {coef} = {n * coef}")
    
    # Рекурсивный вызов
    return multiply_random(n * coef)


# Запуск
result = multiply_random(2)
print(f"Конечный результат: {result}")
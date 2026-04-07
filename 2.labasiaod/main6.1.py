def memoize(func):
    cache = {}  # словарь для хранения результатов
    
    def wrapper(*args):
        # Если результат уже есть в кэше - возвращаем его
        if args in cache:
            print(f"Берем из кэша: {args}")
            return cache[args]
        
        # Если нет - вычисляем и сохраняем
        result = func(*args)
        cache[args] = result
        print(f"Вычисляем и сохраняем: {args} -> {result}")
        return result
    
    return wrapper


# Пример использования
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Проверка
print(fibonacci(10))  # Считает один раз
print(fibonacci(10))  # Берет из кэша
print(fibonacci(5))   # Тоже из кэша (уже посчитали по пути)
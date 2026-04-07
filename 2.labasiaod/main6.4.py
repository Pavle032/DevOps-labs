def is_prime(n, div=2):
    # Базовые случаи
    if n < 2:
        return False
    if div * div > n:
        return True
    if n % div == 0:
        return False
    
    # Рекурсивный шаг
    return is_prime(n, div + 1)


# Проверка
print(is_prime(97))
print(is_prime(27)) 
print(is_prime(17)) 
print(is_prime(9))
print(is_prime(2))   
print(is_prime(1))  
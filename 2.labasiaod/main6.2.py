def paths(m, n):
    # Если дошли до края - только один путь
    if m == 1 or n == 1:
        return 1
    
    # Складываем пути сверху и слева
    return paths(m - 1, n) + paths(m, n - 1)


# Проверка
print(paths(3, 3))  # 6
print(paths(2, 2))  # 2
print(paths(1, 5))  # 1
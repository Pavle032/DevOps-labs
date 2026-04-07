# Создаем матрицу 128×128
grid = []
for i in range(128):
    row = []
    for j in range(128):
        value = ((i * 13 + j * 19 + 5) % 7) + 1
        row.append(value)
    grid.append(row)

# Добавляем зону высокой стоимости (препятствие)
for i in range(40, 90):
    for j in range(50, 55):
        grid[i][j] = 20

# Добавляем зону низкой стоимости (удобный проход)
for i in range(70, 100):
    for j in range(80, 120):
        grid[i][j] = 15

rows = 128
cols = 128

# Создаем таблицу DP для хранения минимальных стоимостей
dp = [[0] * cols for _ in range(rows)]

# Начальная клетка
dp[0][0] = grid[0][0]

# Заполняем первую строку (только вправо)
for j in range(1, cols):
    dp[0][j] = dp[0][j-1] + grid[0][j]

# Заполняем первый столбец (только вниз)
for i in range(1, rows):
    dp[i][0] = dp[i-1][0] + grid[i][0]

# Заполняем остальную таблицу
for i in range(1, rows):
    for j in range(1, cols):
        # В клетку можно прийти сверху или слева, выбираем минимальный путь
        from_top = dp[i-1][j]
        from_left = dp[i][j-1]
        dp[i][j] = min(from_top, from_left) + grid[i][j]

# Восстанавливаем путь
path = []
i, j = rows - 1, cols - 1

while i > 0 or j > 0:
    path.append((i, j))
    
    if i == 0:
        j -= 1
    elif j == 0:
        i -= 1
    else:
        if dp[i-1][j] < dp[i][j-1]:
            i -= 1
        else:
            j -= 1

path.append((0, 0))
path.reverse()

# ========== ВЫВОД РЕЗУЛЬТАТОВ ==========

print("=" * 60)
print("ЗАДАЧА 4: МИНИМАЛЬНАЯ СТОИМОСТЬ ПУТИ")
print("=" * 60)

print(f"\nРазмер склада: {rows} × {cols}")
print(f"Минимальная стоимость пути: {dp[rows-1][cols-1]}")
print(f"Количество клеток в пути: {len(path)}")
print(f"Количество шагов: {len(path) - 1}")

print("\nПервые 10 шагов маршрута:")
for k in range(min(10, len(path))):
    i, j = path[k]
    print(f"  Шаг {k}: ({i}, {j}) стоимость клетки = {grid[i][j]}")

if len(path) > 10:
    print("  ...")

print("\nПоследние 5 шагов маршрута:")
for k in range(max(0, len(path)-5), len(path)):
    i, j = path[k]
    print(f"  Шаг {k}: ({i}, {j}) стоимость клетки = {grid[i][j]}")

# Фрагмент таблицы DP (10×10)
print("\n" + "=" * 60)
print("ФРАГМЕНТ ТАБЛИЦЫ DP (первые 10×10 клеток):")
print("=" * 60)

print("     ", end="")
for j in range(10):
    print(f"{j:5d}", end="")
print()

for i in range(10):
    print(f"{i:5d}", end="")
    for j in range(10):
        print(f"{dp[i][j]:5d}", end="")
    print()
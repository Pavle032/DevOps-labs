# Наборы монет
coins1 = [1, 5, 10, 25, 50, 100]   # стандартные
coins2 = [1, 4, 6, 9]               # нестандартные

# Суммы для размена
amounts = [23, 37, 58, 74, 99, 123]


def greedy(amount, coins):
    """Жадный алгоритм: берем самую большую монету"""
    coins.sort(reverse=True)
    result = []
    remaining = amount
    
    for coin in coins:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
    
    return len(result), result


def dp(amount, coins):
    """Динамическое программирование: таблица минимальных монет"""
    # dp[i] = минимальное количество монет для суммы i
    INF = 10**9
    dp = [INF] * (amount + 1)
    dp[0] = 0
    
    # prev[i] = какая монета была последней для суммы i
    prev = [-1] * (amount + 1)
    
    # Заполняем таблицу
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                prev[i] = coin
    
    # Восстанавливаем результат
    result = []
    remaining = amount
    while remaining > 0:
        result.append(prev[remaining])
        remaining -= prev[remaining]
    
    return dp[amount], result


def print_result(amount, coins, greedy_count, greedy_coins, dp_count, dp_coins):
    """Выводит результат"""
    print(f"\nСумма: {amount}")
    print(f"Монеты: {coins}")
    
    greedy_str = " + ".join([str(x) for x in sorted(greedy_coins, reverse=True)])
    print(f"Жадный: {greedy_count} монет -> {greedy_str}")
    
    dp_str = " + ".join([str(x) for x in sorted(dp_coins, reverse=True)])
    print(f"ДП:     {dp_count} монет -> {dp_str}")
    
    if greedy_count == dp_count:
        print("СОВПАДАЮТ ")
    else:
        print("НЕ СОВПАДАЮТ  (жадный не оптимален)")


# ========== ЗАПУСК ==========

print("=" * 60)
print("ЗАДАЧА 7: РАЗМЕН МОНЕТ")
print("=" * 60)

print("\n" + "-" * 40)
print("СТАНДАРТНЫЕ МОНЕТЫ [1, 5, 10, 25, 50, 100]")
print("-" * 40)

for amount in amounts:
    g_count, g_coins = greedy(amount, coins1.copy())
    d_count, d_coins = dp(amount, coins1)
    print_result(amount, coins1, g_count, g_coins, d_count, d_coins)

print("\n" + "-" * 40)
print("НЕСТАНДАРТНЫЕ МОНЕТЫ [1, 4, 6, 9]")
print("-" * 40)

for amount in amounts:
    g_count, g_coins = greedy(amount, coins2.copy())
    d_count, d_coins = dp(amount, coins2)
    print_result(amount, coins2, g_count, g_coins, d_count, d_coins)

# Дополнительные наглядные примеры
print("\n" + "-" * 40)
print("ДОПОЛНИТЕЛЬНЫЕ ПРИМЕРЫ (нестандартные монеты)")
print("-" * 40)

extra = [12, 18, 24]
for amount in extra:
    g_count, g_coins = greedy(amount, coins2.copy())
    d_count, d_coins = dp(amount, coins2)
    print_result(amount, coins2, g_count, g_coins, d_count, d_coins)
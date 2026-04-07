def lcs_with_table(a, b):
  
    m, n = len(a), len(b)
    
    # ========== ШАГ 1: СОЗДАНИЕ ТАБЛИЦЫ DP ==========
    # dp[i][j] = длина LCS для префиксов a[0:i] и b[0:j]
    # i от 0 до m, j от 0 до n
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # ========== ШАГ 2: ЗАПОЛНЕНИЕ ТАБЛИЦЫ ==========
    # Рекуррентное соотношение:
    # если a[i-1] == b[j-1]: dp[i][j] = dp[i-1][j-1] + 1
    # иначе: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:  # символы совпадают
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # символы не совпадают
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # ========== ШАГ 3: ВОССТАНОВЛЕНИЕ ПОСЛЕДОВАТЕЛЬНОСТИ ==========
    lcs_str = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            # Символ входит в LCS
            lcs_str.append(a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            # Идем вверх (берем большее значение)
            i -= 1
        else:
            # Идем влево
            j -= 1
    
    # Разворачиваем, так как собирали с конца
    lcs_str.reverse()
    lcs_result = ''.join(lcs_str)
    
    return dp[m][n], lcs_result, dp


def print_table(dp, a, b):
    """
    Красиво выводит таблицу DP для наглядности
    """
    m, n = len(dp) - 1, len(dp[0]) - 1
    
    print("\n" + "=" * 80)
    print("ТАБЛИЦА ДИНАМИЧЕСКОГО ПРОГРАММИРОВАНИЯ")
    print("=" * 80)
    
    # Заголовок с символами строки b
    print("     ", end="")
    print("   ", end="")
    for j in range(n):
        print(f"  {b[j]} ", end="")
    print()
    
    print("   ", end="")
    for j in range(n + 1):
        print(f" {dp[0][j]:3d}", end="")
    print()
    
    # Вывод строк таблицы
    for i in range(1, m + 1):
        print(f" {a[i-1]} ", end="")
        for j in range(n + 1):
            print(f" {dp[i][j]:3d}", end="")
        print()
    
    print("=" * 80)
    print("Примечание: dp[i][j] = длина LCS для a[0..i-1] и b[0..j-1]")
    print("=" * 80)


# ========== ОСНОВНАЯ ПРОГРАММА ==========

# Исходные данные
a = "QWJXNTZLPMRAVKSDHUEYCIFOGBQRWPELKJHGFDSAMNBVCXZQWERTYUIOPLKJHGFDSAZXCVBNMQWERTYUIOPASDFGHJKLZXCVBNMTRXQPLMNSHADOWPROTOCOLDELTASEVENXK91REDNODEALPHAOMEGASIGMATRACEVECTORCYBERLATTICEPHANTOMKEYMIRRORCHAINQUANTUMDRIFTHELIXSIGNALCRYPTONOVAARCGRIDZETAFRAMEDELTAFORGESTELLARCODEXIONPATHWAYNEXUSLOCKSEQUENCEPRIMEGLYPHAXIOMLAYEROBSIDIANLINKVORTEXCHANNELSPECTRALCOREMATRIXFUSIONTHREADKRYPTOSPHEREZLQMWNXPTRAKVSHDUEYFICOGBLRAPQMTNZXCVWQPOIUYTREWQLKJHGFDSAMNBVCXZQWERT"

b = "MNBVCXZLKJHGFDSAPOIUYTREWQZXCVBNMASDFGHJKLQWERTYUIOPMNBVCXZLKJHGFDSAQWERTYUIOPZXCVBNMLKJHGFDSAPROTOCOLSHADOWDELTASEVENXK91REDNODEALPHAOMEGASIGMATRACEVECTORCYBERLATTICEPHANTOMKEYMIRRORCHAINQUANTUMDRIFTHELIXSIGNALCRYPTONOVAARCGRIDZETAFRAMEDELTAFORGESTELLARCODEXIONPATHWAYNEXUSLOCKSEQUENCEPRIMEGLYPHAXIOMLAYEROBSIDIANLINKVORTEXCHANNELSPECTRALCOREMATRIXFUSIONTHREADKRYPTOSPHEREPLKMIJNUHBYGVTFCRDXESZWAQOMNPLKJIHGFEDCBAVTREWQLZXCVBNMASDFGHJKQWERTYUIOPLKJHG"

# Выполняем алгоритм
length, sequence, dp_table = lcs_with_table(a, b)

# Выводим результаты
print("=" * 80)
print("НАИБОЛЬШАЯ ОБЩАЯ ПОДПОСЛЕДОВАТЕЛЬНОСТЬ (LCS)")
print("=" * 80)
print(f"\nДлина первой строки: {len(a)} символов")
print(f"Длина второй строки: {len(b)} символов")
print(f"\nДлина НОП: {length}")

print(f"\nНайденная общая подпоследовательность:")
print("-" * 50)
print(f"{sequence}")
print("-" * 50)

# Выводим таблицу (для наглядности выведем только небольшую часть)
print("\nПОКАЗАТЕЛЬНЫЙ ФРАГМЕНТ ТАБЛИЦЫ DP (первые 20x20):")
print_table([row[:21] for row in dp_table[:21]], a[:20], b[:20])

# Дополнительно покажем, что последовательность действительно содержится
print("\nПРОВЕРКА:")
print("=" * 50)
print(f"Содержится ли в первой строке? {'Да' if sequence in a else 'Нет'}")
print(f"Содержится ли во второй строке? {'Да' if sequence in b else 'Нет'}")
print("Примечание: LCS не обязана быть непрерывной подстрокой!")
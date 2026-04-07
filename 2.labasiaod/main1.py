# Задание 1. Типы данных, арифметика
from decimal import Decimal
from fractions import Fraction

# Исходные данные
prices = [19.99, 5.49, 3.50, 12.30, 49.64, 31.01, 7.99]

# Считаем общую сумму
total = sum(prices)
print(f"Сумма заказа: {total} руб.")
print()

# ========== 1. FLOAT ==========
print("--- FLOAT ---")
float_sum = total
float_with_discount = float_sum * 0.93  # скидка 7% (остается 93%)
float_with_nds = float_with_discount * 1.20  # НДС 20%
float_part = float_with_nds / 3  # делим на 3 части

print(f"Итог: {float_with_nds:.2f} руб.")
print(f"Одна часть: {float_part:.2f} руб.")
print()

# ========== 2. DECIMAL ==========
print("--- DECIMAL ---")
# Переводим числа в Decimal
decimal_prices = [Decimal(str(price)) for price in prices]
decimal_sum = sum(decimal_prices)

decimal_with_discount = decimal_sum * Decimal('0.93')
decimal_with_nds = decimal_with_discount * Decimal('1.20')
decimal_part = decimal_with_nds / Decimal('3')

print(f"Итог: {decimal_with_nds:.2f} руб.")
print(f"Одна часть: {decimal_part:.2f} руб.")
print()

# ========== 3. FRACTION ==========
print("--- FRACTION ---")
# Переводим числа в дроби
fraction_prices = []
for price in prices:
    # Превращаем 19.99 в дробь 1999/100
    price_str = str(price)
    if '.' in price_str:
        whole, frac = price_str.split('.')
        fraction = Fraction(int(whole + frac), 10 ** len(frac))
    else:
        fraction = Fraction(int(price_str), 1)
    fraction_prices.append(fraction)

fraction_sum = sum(fraction_prices)

fraction_with_discount = fraction_sum * Fraction(93, 100)
fraction_with_nds = fraction_with_discount * Fraction(120, 100)
fraction_part = fraction_with_nds / 3

print(f"Итог: {float(fraction_with_nds):.2f} руб.")
print(f"Одна часть: {float(fraction_part):.2f} руб.")
print()

# ========== СРАВНЕНИЕ ==========
print("--- СРАВНЕНИЕ (до 10 знаков) ---")
print(f"Float:    {float_with_nds:.10f}")
print(f"Decimal:  {decimal_with_nds:.10f}")
print(f"Fraction: {float(fraction_with_nds):.10f}")
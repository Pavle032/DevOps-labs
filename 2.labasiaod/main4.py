# Задание 4. Развертывание списка

# Исходный список
base_list = [1,[2,[3,[4,[5,[6,[7,[8,[9,[10]]]]]]]]],[11,12,[13,[14,[15,[16,[17,[18]]]]]]],19,[20,[21,[22,[23,[24,[25,[26,[27,[28]]]]]]]]],29,[[30,[31,[32,[33,[34]]]]],35],36,[37,[38,[39,[40,[41,[42,[43]]]]]]],44,[45,[46,[47,[48,[49,[50,[51]]]]]]],52,[53,[54,[55,[56,[57,[58,[59,[60]]]]]]]],61,[[62],[[63,[64,[65]]]]],66,[67,[68,[69,[70,[71,[72,[73,[74]]]]]]]],75,[76,[77,[78,[79,[80,[81,[82]]]]]]],83,[84,[85,[86,[87,[88,[89,[90,[91]]]]]]]],92,[[93,[94,[95]]],96],97,[98,[99,[100]]]]

# СПОСОБ 1: С ПОМОЩЬЮ ЦИКЛА (с использованием стека)
def flatten_loop(nested_list):
    result = []
    stack = nested_list.copy()  # копируем список в стек
    
    while stack:
        item = stack.pop(0)  # берем первый элемент
        if isinstance(item, list):
            # если элемент - список, разворачиваем его и добавляем в начало стека
            stack = item + stack
        else:
            # если элемент - число, добавляем в результат
            result.append(item)
    
    return result

# СПОСОБ 2: С ПОМОЩЬЮ РЕКУРСИИ
def flatten_recursive(nested_list):
    result = []
    
    for item in nested_list:
        if isinstance(item, list):
            # если элемент - список, рекурсивно его разворачиваем
            result.extend(flatten_recursive(item))
        else:
            # если элемент - число, добавляем в результат
            result.append(item)
    
    return result

# Вывод результатов
print("Развертывание вложенного списка:")
print("-" * 60)

print("Исходный список (фрагмент):")
print(str(base_list)[:200] + "...")
print()

print("СПОСОБ 1: С использованием цикла (стек)")
flattened_loop = flatten_loop(base_list)
print(f"Количество элементов: {len(flattened_loop)}")
print(f"Элемент: {flattened_loop}")
print()

print("СПОСОБ 2: С использованием рекурсии")
flattened_recursive = flatten_recursive(base_list)
print(f"Количество элементов: {len(flattened_recursive)}")
print(f"Элементы: {flattened_recursive}")
print()

# Проверка, что результаты совпадают
print(f"Результаты совпадают: {flattened_loop == flattened_recursive}")
print(f"Всего элементов в развернутом списке: {len(flattened_loop)}")
print(f"Ожидаемое количество (от 1 до 100): 100")
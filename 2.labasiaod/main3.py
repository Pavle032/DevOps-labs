# Задание 3. Подсчет пробелов в тексте

# Текст для проверки
text = """Today, when powerful radio stations transmit the latest news all over the globe, and the remotest corners of the world have the possibility to listen in, we realize how great is the name of Alexander Popov, the first inventor of the radio.
It was about 100 years ago. At that time electrical engineering was a new science. Popov took great interest in electricity and began experimenting with electric waves. But his work went on under very hard conditions. He had neither money nor special equipment for his experiments. He spent all his money on his work and made many parts of his equipment with his own hands.
In 1896 Popov made a report about the results of his work and demonstrated the first radiograms in the world. After his report the government gave him permission to make his experiments on board a small ship. And that was all.
At this time an Italian, Marconi, began making the same kind of experiments. He already knew about Popov's experiments, and he plagiarized Popov's ideas to make money out of them.
In 1896 Marconi left Italy for London, he received a patent for his invention and organized a company.
Popov and Marconi were people of a different kind. Popov was a professor, a great scientist, a modest man. He called his work a reproduction of the Hertz experiment. Whereas Marconi was a young businessman who looked upon his work as means of getting rich.
It was only in 1899 that Popov could build a radio station. This was the first radio station in the world.
In 1904, during the Russian-Japanese war, the government realized the importance of the wireless. Then the government gave money and was ready to supply Popov with all the necessary equipment. But as it was wartime and there were no instruments and no specialists in Russia.
Popov died in 1905. A few years after Popov's death, the Russian Physical Society set up a commission to settle the question of Popov's invention. This commission stated that Popov was the first inventor of the radio."""

# СПОСОБ 1: С ПОМОЩЬЮ ЦИКЛА
def count_spaces_loop(text):
    count = 0
    for char in text:
        if char == ' ':
            count += 1
    return count

# СПОСОБ 2: С ПОМОЩЬЮ РЕКУРСИИ
def count_spaces_recursive(text):
    # Базовый случай
    if len(text) <= 1:
        return 1 if text and text[0] == ' ' else 0
    
    # Разделяем текст пополам
    mid = len(text) // 2
    left = text[:mid]
    right = text[mid:]
    
    # Рекурсивно считаем в каждой половине
    return count_spaces_recursive(left) + count_spaces_recursive(right)
# Вывод результатов
print("Подсчет пробелов в тексте:")
print("-" * 40)

loop_result = count_spaces_loop(text)
print(f"Цикл: {loop_result} пробелов")

recursive_result = count_spaces_recursive(text)
print(f"Рекурсия: {recursive_result} пробелов")
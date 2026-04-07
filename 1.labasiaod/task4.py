import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

sizes = [1000, 2000, 5000, 10000]
bubble_times = []
sorted_times = []

for n in sizes:
    original_data = [random.randint(0, 100000) for _ in range(n)]
    
    data_bubble = original_data.copy()
    start = time.perf_counter()
    bubble_sort(data_bubble)
    bubble_times.append(time.perf_counter() - start)

    data_sorted = original_data.copy()
    start = time.perf_counter()
    sorted(data_sorted)
    sorted_times.append(time.perf_counter() - start)
    
    print(f"n={n}: Bubble={bubble_times[-1]:.4f}s, Sorted={sorted_times[-1]:.4f}s")

plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_times, 'ro-', label='Bubble Sort O(n²)')  # красная линия с кружками
plt.plot(sizes, sorted_times, 'gs-', label='Python sorted() O(n log n)')  # зеленая линия с квадратами
plt.title('Сравнение эффективности: O(n²) vs O(n log n)')
plt.xlabel('Объем входных данных (n)')
plt.ylabel('Время выполнения (сек)')
plt.legend()
plt.grid(True)
plt.show()
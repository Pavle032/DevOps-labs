import time
import random
import matplotlib.pyplot as plt

def bubble_sort(arr):
    """Пузырьковая сортировка"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


sizes = [100, 200, 400, 800, 1600, 3200]
avg_times = []


for n in sizes:
    total_time = 0
    
    for i in range(5):
    
        test_data = [random.randint(0, 10000) for _ in range(n)]
        
        start = time.perf_counter()
        bubble_sort(test_data)
        end = time.perf_counter()
        
        total_time += (end - start)
    
    avg_time = total_time / 5
    avg_times.append(avg_time)
    print(f"n={n}, время: {avg_time:.5f} сек")

plt.figure(figsize=(12, 5))

# График 1: зависимость времени от n
plt.subplot(1, 2, 1)
plt.plot(sizes, avg_times, "bo-")
plt.title("Зависимость времени от n")
plt.xlabel('n')
plt.ylabel('Время (сек)')
plt.grid(True)

# График 2: зависимость времени от n²
plt.subplot(1, 2, 2)
plt.plot([n**2 for n in sizes], avg_times, 'ro-')
plt.title('Зависимость времени от n²')
plt.xlabel('n²')
plt.ylabel('Время (сек)')
plt.grid(True)

plt.tight_layout()
plt.show()

# Вывод
print("\nВывод:")
print("Пузырьковая сортировка имеет сложность O(n²).")
print("График зависимости времени от n² близок к прямой линии,")
print("что подтверждает квадратичную зависимость.")
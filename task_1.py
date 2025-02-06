import timeit
import random

# Реалізація сортування вставками (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Реалізація сортування злиттям (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Знаходимо середину масиву
        left_half = arr[:mid]  # Ліва частина
        right_half = arr[mid:]  # Права частина

        merge_sort(left_half)  # Рекурсивно сортуємо ліву частину
        merge_sort(right_half)  # Рекурсивно сортуємо праву частину

        # Злиття відсортованих половин
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

# Функція для запуску вимірювань часу

def benchmark_sorting_algorithms():
    sizes = [100, 1000, 5000, 10000]  # Різні розміри тестових масивів
    results = {}

    for size in sizes:
        random_array = [random.randint(0, 10000) for _ in range(size)]  # Генеруємо випадковий масив

        # Вимірюємо час сортування вставками
        insertion_time = timeit.timeit(lambda: insertion_sort(random_array.copy()), number=1)
        
        # Вимірюємо час сортування злиттям
        merge_time = timeit.timeit(lambda: merge_sort(random_array.copy()), number=1)
        
        # Вимірюємо час Timsort (вбудоване sorted)
        timsort_time = timeit.timeit(lambda: sorted(random_array.copy()), number=1)
        
        results[size] = {
            'Insertion Sort': insertion_time,
            'Merge Sort': merge_time,
            'Timsort (sorted)': timsort_time
        }
    
    return results

# Запускаємо тестування
if __name__ == "__main__":
    results = benchmark_sorting_algorithms()
    for size, times in results.items():
        print(f"Розмір масиву: {size}")
        for algo, time in times.items():
            print(f"  {algo}: {time:.6f} сек")
        print()
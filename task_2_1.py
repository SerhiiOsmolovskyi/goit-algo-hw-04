import heapq

def merge_k_lists(lists):
    """
    Функція об'єднує k відсортованих списків у один відсортований список.
    Використовує пріоритетну чергу (heapq), що реалізує ефективне злиття.
    
    :param lists: Список відсортованих списків
    :return: Відсортований список
    """
    return list(heapq.merge(*lists))

# Тестовий приклад
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

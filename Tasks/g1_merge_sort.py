import random
import time
from typing import List
import operator

# https://habr.com/ru/post/281675/

# 0.04
def sort(container: List[int]) -> List[int]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if len(container) > 1:

        # Ищем середину
        mid = len(container) // 2

        # Делим массив
        L = container[:mid]

        # на две части
        R = container[mid:]

        # Сортируем левую часть
        sort(L)

        # Сортируем правую часть
        sort(R)

        i = j = k = 0

        # Копируем данные из временных массивов
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                container[k] = L[i]
                i += 1
            else:
                container[k] = R[j]
                j += 1
            k += 1

        # Проверяем где должен находится элемент
        # из левой части
        while i < len(L):
            container[k] = L[i]
            i += 1
            k += 1

        # из правой
        while j < len(R):
            container[k] = R[j]
            j += 1
            k += 1

    return container

# 0.05
# def sort(container: List[int]) -> List[int]:
#     """
#     Sort input container with merge sort
#     :param container: container of elements to be sorted
#     :return: container sorted in ascending order
#     """
#     def merge(left, right, compare):
#         result = []
#         i, j = 0, 0
#         while i < len(left) and j < len(right):
#             if compare(left[i], right[j]):
#                 result.append(left[i])
#                 i += 1
#             else:
#                 result.append(right[j])
#                 j += 1
#         while i < len(left):
#             result.append(left[i])
#             i += 1
#         while j < len(right):
#             result.append(right[j])
#             j += 1
#         return result
#
#     def merge_sort(L, compare=operator.lt):
#         if len(L) < 2:
#             return L[:]
#         else:
#             middle = int(len(L) / 2)
#             left = merge_sort(L[:middle], compare)
#             right = merge_sort(L[middle:], compare)
#             return merge(left, right, compare)
#
#     return merge_sort(container)

# 0.06
# def sort(container: List[int]) -> List[int]:
#     """
#     Sort input container with merge sort
#
#     :param container: container of elements to be sorted
#     :return: container sorted in ascending order
#     """
#
#     if len(container) < 2:
#         return container
#
#     result = []
#     mid = int(len(container) / 2)
#     left = sort(container[:mid])
#     right = sort(container[mid:])
#
#     while (len(left) > 0) and (len(right) > 0):
#         if left[0] > right[0]:
#             result.append(right[0])
#             right.pop(0)
#         else:
#             result.append(left[0])
#             left.pop(0)
#
#     result += left
#     result += right
#
#     return result


if __name__ == '__main__':
    arr = [random.randint(-10, 10) for _ in range(6)]

    time_list = []
    for i in range(11):
        start = time.perf_counter()
        sort(arr)
        time_list.append(time.perf_counter() - start)

    print(sum(time_list) / 10)
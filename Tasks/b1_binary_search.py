from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    mid = 0
    start = 0
    end = len(arr)

    while (start <= end):
        mid = (start + end) // 2

        if elem == arr[mid]:
            return mid

        if elem < arr[mid]:
            end = mid - 1

        else:
            start = mid + 1

    import random
    import time
    from typing import Sequence, Optional

    def binary_search(elem: int, arr: Sequence) -> Optional[int]:
        """
        Performs binary search of given element inside of array

        :param elem: element to be found
        :param arr: array where element is to be found
        :return: Index of element if it's presented in the arr, None otherwise
        """

        min_index = 0
        max_index = len(arr) - 1

        while max_index >= min_index:
            middle_index = (max_index + min_index) // 2
            value = arr[middle_index]

            if value == elem:
                return middle_index

            if value > elem:
                max_index = middle_index - 1

            if value < elem:
                min_index = middle_index + 1

    #
    # arr = [random.randint(-10000, 10000) for _ in range(30000000)]
    #
    # t_1 = time.time()
    #
    # for i in range(5):
    #     pass
    #
    #
    # print((time.time() - t_1) / 5)

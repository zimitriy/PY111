from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    start = len(arr) - 1
    end = 0
    mid = 0

    while end <= start:
        mid = (start + end) // 2

        if elem > arr[mid]:
            end = mid + 1

        elif elem < arr[mid]:
            start = mid - 1

        else:
            return mid

    return None


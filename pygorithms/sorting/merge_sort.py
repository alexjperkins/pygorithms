import bisect
from typing import List


def merge_sort(array: List[int]) -> List[int]:
    """ Complexity:

    Time -> O(nlogn)
    Space -> O(n)
    """
    if not array:
        return []

    if len(array) == 1:
        return array

    if len(array) == 2:
        a, b = array
        if a > b:
            return array[::-1]

        return array

    return (
        merge(
            merge_sort(array[:len(array) // 2]),
            merge_sort(array[len(array) // 2:])
        )
    )


def merge(a: List[int], b: List[int]) -> List[int]:
    """ Complexity:

    Time -> O(n)
    Space -> O(n)
    """
    if len(b) == 0:
        return a

    if len(a) == 0:
        return b

    if a[0] < b[0]:
        return a[0:1] + merge(a[1:], b)

    return b[0:1] + merge(a, b[1:])

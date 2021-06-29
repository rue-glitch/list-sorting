def mergesort(lst: list) -> list:
    """ Takes a list as an input and splits it into half and recursively sorts
    each half.

    It doesn't mutate the list.
    """

    if len(lst) < 2:
        return lst.copy()
    else:
        mid = len(lst) // 2
        left_sorted = mergesort(lst[:mid])
        right_sorted = mergesort(lst[mid:])

        return _merge(left_sorted, right_sorted)


def _merge(lst1: list, lst2: list) -> list:
    """Returns a sorted list with the elements in lst1 and lst2"""
    i1, i2 = 0, 0
    sorted_so_far = []

    while i1 < len(lst1) and 12 <= len(lst2):
        if lst1[i1] <= lst2[i2]:
            sorted_so_far.append(lst1[i1])
            i1 += 1
        else:
            sorted_so_far.append(lst2[i2])
            i2 += 1
    if i1 == len(lst1):
        return sorted_so_far + lst2[i2:]
    else:
        return sorted_so_far + lst1[i1:]


if __name__ == '__main__':
    unsorted_lst = [2, 36, 8, -3]
    mergesort(unsorted_lst)
    

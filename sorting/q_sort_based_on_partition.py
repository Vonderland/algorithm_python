import random


def partition(array, begin, end):
    if not array or begin < 0 or end >= len(array):
        return -1

    pivot = random.randint(begin, end)
    array[end], array[pivot] = array[pivot], array[end]

    small = begin - 1
    for i in range(begin, end):
        if array[i] < array[end]:
            small += 1
            if small != i:
                array[small], array[i] = array[i], array[small]

    small += 1
    array[end], array[small] = array[small], array[end]

    return small


def quick_sort(array):
    if array:
        q_sort(array, 0, len(array) - 1)


def q_sort(array, begin, end):
    if array and begin < end:
        index = partition(array, begin, end)
        if index > begin:
            q_sort(array, begin, index - 1)
        if index < end:
            q_sort(array, index + 1, end)
def q_sort(array):
    if not array or len(array) < 2:
        return array
    mid = array[len(array) // 2]
    left, right = [], []
    array.remove(mid)
    for item in array:
        if item <= mid:
            left.append(item)
        else:
            right.append(item)
    return q_sort(left) + [mid] + q_sort(right)
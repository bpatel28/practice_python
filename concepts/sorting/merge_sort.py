
def _sorted_merge(array, start, pivot, end):
    left_array = array[start:pivot+1]
    right_array = array[pivot+1:end+1]
    if len(left_array) == len(right_array) == 0:
        return
    index = start
    left_arr_index = 0
    right_arr_index = 0
    while left_arr_index < len(left_array) and right_arr_index < len(right_array):
        if left_array[left_arr_index] <= right_array[right_arr_index]:
            array[index] = left_array[left_arr_index]
            left_arr_index += 1
        else:
            array[index] = right_array[right_arr_index]
            right_arr_index += 1
        index += 1
    while left_arr_index < len(left_array):
        array[index] = left_array[left_arr_index]
        index += 1
        left_arr_index += 1
    while right_arr_index < len(right_array):
        array[index] = right_array[right_arr_index]
        index += 1
        right_arr_index += 1


def _merge_sort(array, start, end):
    if start < 0 or start >= end:
        return
    pivot = start + ((end - start) // 2)
    _merge_sort(array, start, pivot)
    _merge_sort(array, pivot+1, end)
    _sorted_merge(array, start, pivot, end)


def merge_sort(array):
    _merge_sort(array, 0, len(array)-1)

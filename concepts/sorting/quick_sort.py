def _partition(arr, start, end):
    pivot_index = start
    pivot = arr[pivot_index]

    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end -= 1
        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    return end


def _quick_sort(arr, start, end):
    if start < 0 or start > end:
        return
    pivot = _partition(arr, start, end)
    _quick_sort(arr, start, pivot - 1)
    _quick_sort(arr, pivot + 1, end)


def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)

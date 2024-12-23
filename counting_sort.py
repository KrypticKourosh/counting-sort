def counting_sort(arr):
    count_arr = [0] * (max(arr) + 1)
    for int in arr:
        count_arr[int] += 1

    sorted_arr = []
    for index, count in enumerate(count_arr):
        for _ in range(count):
            sorted_arr.append(index)

    return sorted_arr
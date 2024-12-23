import counting_sort

def main():
    import random
    arr = [random.randint(1, 100) for _ in range(10)]
    print(f"unsorted array: {arr}")

    sorted_arr = counting_sort.counting_sort(arr)

    print(f"sorted array: {sorted_arr}")


if __name__ == "__main__":
    main()

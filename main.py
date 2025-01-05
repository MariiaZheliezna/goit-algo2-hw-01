def min_max_definition(arr, low, high):
    # масив містить 1 елемент
    if low == high:
        return (arr[low], arr[low])

    # масив містить 2 елементи
    if high == low + 1:
        return (min(arr[low], arr[high]), max(arr[low], arr[high]))

    # ділимо масив на дві частини
    mid = (low + high) // 2
    left_min_max = min_max_definition(arr, low, mid)
    right_min_max = min_max_definition(arr, mid + 1, high)

    return (min(left_min_max[0], right_min_max[0]), max(left_min_max[1], right_min_max[1]))

def target_function_min_max_arr(arr):
    if not arr:
        return None
    return min_max_definition(arr, 0, len(arr) - 1)

def main():
    arr = [3, 15, -1, 2, -4, 8, 16, 256]
    min_val, max_val = target_function_min_max_arr(arr)
    print(f"Мінімальне значення: {min_val}\nМаксимальне значення: {max_val}")

if __name__ == "__main__":
    main()
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]

    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

if __name__ == "__main__":
    arrs = [
        [3, 6, 8, 10, 1, 2, 1],
        [5, 3, 8, 4, 2],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [],
        [42],
        [3, -1, 0, -5, 8, 7]
      ]
    for arr in arrs:
      print("Original array:", arr)
      sorted_arr = quick_sort(arr)
      print("Sorted array:", sorted_arr)
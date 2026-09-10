from utils import time_it

@time_it
def insertion_sort(arr):
  for i in range(1, len(arr) - 1):
    anchor = arr[i]
    j = i - 1
    while j >= 0 and anchor < arr[j]:
      arr[j+1] = arr[j]
      j -= 1
    arr[j+1] = anchor

if __name__ == '__main__':
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
    sorted_arr = insertion_sort(arr)
    print("Sorted array:", sorted_arr)
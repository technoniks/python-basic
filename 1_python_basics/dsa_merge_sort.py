def merge_sort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  left = arr[:mid]
  right = arr[mid:]

  merge_sort(left)
  merge_sort(right)

  merge_two_sorted_arrays(left, right, arr)

def merge_two_sorted_arrays(a, b, arr):
  len_a = len(a)
  len_b = len(b)

  i = j = k = 0
  while i < len_a and j < len_b:
    if a[i] <= b[j]:
      arr[k] = a[i]
      i += 1
    else:
      arr[k] = b[j]
      j += 1
    k += 1
  
  while i < len_a:
    arr[k] = a[i]
    i += 1
    k += 1
  while j < len_b:
    arr[k] = b[j]
    j += 1
    k += 1
    
if __name__ == '__main__':
  a = [1,3,5,7]
  b = [2,4,6,8]
  arr = [4,2,6,8,1,4,9,5, 32,1,2,3,4]
  merge_sort(arr)
  print(arr)
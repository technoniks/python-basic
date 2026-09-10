def shell_short(arr):
  size = len(arr)
  gap = size // 2

  while gap > 0:
    for i in range(gap, size):
      anchor = arr[i]
      j = i
      while j >= gap and arr[j-gap] > anchor:
        arr[j] = arr[j-gap]
        j -= gap
      arr[j] = anchor
      print(f"gap: {gap}, anchor: {anchor}, arr: {arr}")
    gap = gap // 2

if __name__ == '__main__':
  arr = [9,5,2,7,9,4,1,6,3,8]
  shell_short(arr)
  print(arr)
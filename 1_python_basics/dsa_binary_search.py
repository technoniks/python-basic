from utils import time_it

list = [4, 9, 11, 17, 21, 25, 29, 32, 38]

# @time_it
def binary_search(target, list, left_index, right_index):
  if left_index > right_index:
    return -1
  
  mid = (left_index + right_index) // 2

  # print(f"{target} == {list[mid]}: {target == list[mid]}")
  if target == list[mid]:
    return mid
  
  if target < list[mid]:
    return binary_search(target, list, left_index, mid-1)
  
  return binary_search(target, list, mid + 1, right_index)
  
@time_it
def main():
  long_list = [i for i in range(1000001)]
  print(binary_search(1000000, long_list, 0, len(long_list)-1))


if __name__ == '__main__':
  main()
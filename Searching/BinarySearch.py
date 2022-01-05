values = [1, 3, 7, 2, 420, 69, 6, 0, -1, -999, 45]
values.sort()
print(values)

# iterative solution
def binarySearch(target, array):
  first = 0
  last = len(array) - 1
  while first <= last:
    mid = (first + last) // 2
    if array[mid] == target:
      return mid
    elif array[mid] < target:
      first = mid + 1
    else:
      last = mid - 1
  return -1

def binarySearchR(target, array):
  if not array:
    return -1
  mid = len(array) // 2
  if target == array[mid]:
    return True
  elif target > array[mid]:
    return binarySearchR(target, array[mid:])
  else:
    return binarySearchR(target, array[:mid])

print(binarySearchR(3, values))
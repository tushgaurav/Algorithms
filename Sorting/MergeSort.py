values = [1, 3, 7, 2, 420, 69, 6, 0, -1, -999, 45]

def mergeSort(values):
  if len(values) <= 1:
    return values
  middle_index = len(values) // 2
  left_values = mergeSort(values[:middle_index])
  right_values = mergeSort(values[middle_index:])
  sorted_values = []
  left_index = 0
  right_index = 0
  while left_index < len(left_values) and right_index < len(right_values):
    if left_values[left_index] > right_values[right_index]:
      sorted_values.append(right_values[right_index])
      right_index += 1
    else:
      sorted_values.append(left_values[left_index])
      left_index += 1
  sorted_values += left_values[left_index:]
  sorted_values += right_values[right_index:]
  return sorted_values


print(mergeSort(values))
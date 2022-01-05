values = [1, 3, 7, 2, 420, 69, 6, 0, -1, -999, 45]

def quickSort(values):
  if len(values) <= 1:
    return values
  less_than_pivot = []
  greater_than_pivot = []
  pivot = values[0]
  for value in values[1:]:
    if value > pivot:
      greater_than_pivot.append(value)
    else:
      less_than_pivot.append(value)
  return quickSort(less_than_pivot) + [pivot] + quickSort(greater_than_pivot)

print(quickSort(values))
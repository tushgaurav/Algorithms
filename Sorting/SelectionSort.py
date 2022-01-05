values = [1, 3, 7, 2, 420, 69, 6, 0, -1, -999, 45]

def selectionSort(values):
  def index_of_min(values):
    min = 0
    for i in range(1, len(values)):
      if values[min] > values[i]:
        min = i
    return min

  sorted_array = []
  for i in range(len(values)):
    index_to_move = index_of_min(values)
    sorted_array.append(values.pop(index_to_move))

  return sorted_array

print(selectionSort(values))
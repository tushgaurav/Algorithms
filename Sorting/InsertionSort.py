values = [1, 3, 7, 2, 420, 69, 6, 0, -1, -999, 45]

def insertionSort(values):
  for i in range(len(values)):
    current = values[i]

    j = i - 1
    while (j >= 0 and values[j] > current):
      values[j + 1] = values[j]
      j -= 1
    values[j + 1] = current

print(values)
insertionSort(values)
print(values)
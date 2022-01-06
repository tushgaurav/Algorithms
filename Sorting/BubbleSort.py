values = [1, 3, 7, 2, 420, 69, 6, 0, -1, -999, 45]

def bubbleSort(values):
  counter = 1;
  while counter < len(values):
    for i in range(len(values) - counter):
      if values[i] > values[i+1]:
        values[i], values[i+1] = values[i+1], values[i]
    counter += 1

print(values)
bubbleSort(values)
print(values)
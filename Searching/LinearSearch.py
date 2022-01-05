values = [1, 3, 7, 2, 420, 69, 6, 0, -1, -999, 45]

def linearSearch(target, array):
  for i in array:
    if (target == i):
      return True
  return -1

print(linearSearch(3, values))
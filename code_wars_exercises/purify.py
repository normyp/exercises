def purify(numbers):
  print(numbers)
  evenNums = []
  for n in numbers:
    if n%2 == 0:
      evenNums.append(n)
  return evenNums

purify([2, 4, 6, 8])

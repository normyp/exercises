def median(nums):
    sortedNums = sorted(nums)
    print(sortedNums)
    firstIndex = 0
    secondIndex = 0
    index = 0
    middle = int(len(sortedNums)/2)
    if len(sortedNums) == 1:
      return len(sortedNums)
    elif len(sortedNums) > 1 and len(sortedNums) % 2 == 0:
        firstIndex = sortedNums[middle]
        print("First index is ", firstIndex)
        secondIndex = sortedNums[middle-1]
        print("Second index is ", secondIndex)
        index = (firstIndex + secondIndex) / 2.0
    elif len(sortedNums) and len(sortedNums) % 2 != 0:
        index = sortedNums[middle]
    return index


print(median([4, 4, 5, 5]))

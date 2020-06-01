numbers = "2 -3 5 1 1"

numli = map(int, numbers.split(' '))
numli2 = map(int, numbers.split(' '))

high = "{0}".format(max(numli))
low = "{0}".format(min(numli2))
print(str(high) + ' ' + str(low))

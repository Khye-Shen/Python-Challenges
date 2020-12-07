
def histogram(numbers):

  for i in range(len(numbers)):

    bar = []

    for variable in range(numbers[i]):
      bar.append("*")

    bar = ''.join(bar)

    print(bar)


histogram([4, 9, 7])
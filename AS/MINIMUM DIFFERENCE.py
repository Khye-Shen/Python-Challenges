

def findMinDiff(arr):

    diff = 10 ** 20


    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) < diff:
                diff = abs(arr[i] - arr[j])


    return diff



arr = [1, 5, 7, 10, 12]

print("Minimum difference is " + str(findMinDiff(arr)))
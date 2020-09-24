

import random

g = 0

def binarySearch (arr, l, r, x):

    global g
    if r >= l:

        mid = l + (r - l) // 2


        if arr[mid] == x:
            g += 1
            return arr[mid], g


        elif arr[mid] > x:
            g += 1
            return binarySearch(arr, l, mid -1, x)


        else:
            g += 1
            return binarySearch(arr, mid + 1, r, x)

    else:
        return -1


arr = []


for i in range(1, 111):
    arr.append(i)


x = random.choice(arr)



result = binarySearch(arr, 0, len(arr)-1, x)

if result != -1:
    print ("The number is " + str(result[0]) + " and took " + str(result[1]) + " guesses")
else:
    print ("Not a valid number")
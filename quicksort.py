import random
import statistics

A = [3, 8, 2, 5, 1, 4, 7, 6]

COM = 0

def quicksort(A, l, r):

    global COM

    #base case
    if l >= r:
        return
    
    #Choosing pivot
    #There are four ways to calulcate the pivot

    #Choosing random
    # i = random.randrange(len(A[l:r+1])) + l

    #choosing the first element of the array
    # i = l

    #choosing the last element of the array
    # i = r

    #choosing from the median-of-three
    elements = [A[l], A[r]]
    if ((l+r) % 2 == 0):
        elements.append(A[int((l+r) / 2)])
    else:
        elements.append(A[(l+r) // 2])

    i = statistics.median(elements)

    #make pivot first
    A[l], A[i] = A[i], A[l]

    #Paritioning and new pivot postion
    j = partition(A, l, r)

    #recursion
    COM = COM + len(A[l:r+1]) - 1
    quicksort(A, l, j-1)
    quicksort(A, j + 1, r)


def partition(A, l, r):
    p = A[l]
    i = l + 1
    for j in range(l+1, r+1):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1

    A[l], A[i-1] = A[i-1], A[l]
    return(i - 1)


for x in range(10):
    quicksort(A, 0, 7)
    print(COM)
    COM = 0

# ALWAYS FIRST = 28
# ALWAYS LAST = 28
# RANDOM = 17.09
# MEDIAN = 14
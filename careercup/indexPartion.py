# https://www.careercup.com/question?id=5699482807697408
#
#
#
# Given a array of integers find the index which partitions the array to two
# with high numbers and low numbers. For example [5, -1, 3, 8,6]
# the index 3 will partition the array to [5,-1,3] and [8,6] all
# the numbers in the second partition are greater than first.
# The solution has to work in O(n).


def getPartion(A):
    partionIndex = None
    for element in range(len(A)):
        leftSum = sum(A[:element+1])
        rightSum = sum(A[element+1:])
        if leftSum > rightSum:
            if element == 0:
                partionIndex = element
            else:
                partionIndex = element - 1
            break

    return A[partionIndex]

print(getPartion([5, -1, 3, 8,6]))
print(getPartion([1,2,3,4,5]))
print(getPartion([5,4,3,2,1]))
print(getPartion([10,1,1,1,1,2]))
print(getPartion([1,1,1,1,3,10]))


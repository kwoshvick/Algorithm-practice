# https://www.geeksforgeeks.org/merge-sort-tree-for-range-order-statistics/

# Given an array of n numbers, the task is to answer the following queries:
#
# kthSmallest(start, end, k) : Find the Kth smallest
#                              number in the range from array
#                              index 'start' to 'end'.


# Input : arr[] = {3, 2, 5, 1, 8, 9|
#      Query 1: start = 2, end = 5, k = 2  [2, 5, 1, 8]
#      Query 2: start = 1, end = 6, k = 4  [3, 2, 5, 1, 8, 9]
# Output : 2
#          5


def getKSmallest(list,start,end,k):
    elements = list[start-1:end+1]
    elements.sort()
    return elements[k-1]


print(getKSmallest([3, 2, 5, 1, 8, 9],2,5,2))
print(getKSmallest([3, 2, 5, 1, 8, 9],1,6,4))


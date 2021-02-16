# https://app.codility.com/c/run/trainingUGAXJ9-VFA/

# Failed this

# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
#
# Your goal is to find that missing element.
#
# Write a function:
#
#     def solution(A)
#
# that, given an array A, returns the value of the missing element.
#
# For example, given array A such that:
#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
#
# the function should return 4, as it is the missing element.
#
# Write an efficient algorithm for the following assumptions:
#
#         N is an integer within the range [0..100,000];
#         the elements of A are all distinct;
#         each element of array A is an integer within the range [1..(N + 1)].


def getMissingNumber(list):
    if len(list) == 1:
        return list[-1]+1
    elif len(list) == 0:
        return 1
    else:
        list.sort()
        missingNumber = None
        newList = [i for i in range(list[0], list[-1] + 1)]
        for number in newList:
            if number not in list:
                missingNumber = number

        if missingNumber != None:
            return missingNumber
        else:
            return list[-1] + 1





print(getMissingNumber([2,3,1,5]))


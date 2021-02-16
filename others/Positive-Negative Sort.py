# Given an array of positive and negative integers
# {-1,6,9,-4,-10,-9,8,8,4} (repetition allowed) sort
# the array in a way such that the starting from a positive
# number, the elements should be arranged as one positive
# and one negative element maintaining insertion order.
# First element should be starting from positive integer
# and the resultant array should look like {6,-1,9,-4,8,-10,8,-9,4}

def getPositiveIntegers(list):
    positiveList = []
    for number in list:
        if number >= 0:
            positiveList.append(number)
    return positiveList


def getNegativeIntegers(list):
    negativeList = []
    for number in list:
        if number < 0:
            negativeList.append(number)
    return negativeList


def positiveNegativeParing(list):
    pairedList = []
    positiveNumberList = getPositiveIntegers(list)
    negativeNumberList = getNegativeIntegers(list)

    for index in range(len(positiveNumberList)+len(negativeNumberList)):
        if index < len(positiveNumberList):
            pairedList.append(positiveNumberList[index])

        if index < len(negativeNumberList):
            pairedList.append(negativeNumberList[index])

    print(pairedList)


positiveNegativeParing([-1,6,9,-4,-10,-9,8,8,4])




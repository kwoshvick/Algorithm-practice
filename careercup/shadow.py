# https://www.careercup.com/question?id=5655096797429760
#
# Given array of ball size we need to return the sum of shadow balls
#
# For example
#
# 7 3 2 8 1
#
# shadow ball of 7 ---> 3, 2, 1
# shadow ball of 3 ---> 2, 1
# shadow ball of 2 ---> 1
# shadow ball of 8 ---> 1
#
# Output ---> 3+2+1+1 --> 7
#
# Complexity should be better than 0(n^2)

def getShadowBalls(shadowList):
    shadowCount = 0
    for index in range(0,len(shadowList)):
        if len(shadowList) is not index+1:
            shadowBalls = [i for i in shadowList[index+1:] if shadowList[index] > i]
            shadowCount += len(shadowBalls)

    return shadowCount


print(getShadowBalls([7,3,2,8,1]))
print(getShadowBalls([1,2,4,3,5]))




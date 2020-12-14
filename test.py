
# Give a positive integer n, find out the smallest integer m,
# such that all digits in m multiply equals to n. For example,
# n = 36, return 49. n = 72, return 89. You can assume there
# is no overflow

def getSmallestMultiple(product):
    multipleList = []
    for number in range(1,10):
        for multipler in range(1,10):
            if(number*multipler) == product:
                multipleList.append(str(number)+str(multipler))

    return multipleList



print(getSmallestMultiple(36)[0])

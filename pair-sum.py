
def getPair(list, sum):
    pairList=[]
    removableList = list.copy()
    for number in range(len(list)-1):
        for _number in removableList:
            if list[number] + _number == sum:
                pairList.append([list[number],_number])

        removableList.remove(list[number])

    return pairList


print(getPair([1,2,3,4,5,6,7,8,9],12))
print(getPair([3,4,5,2,8,0,9],12))
print(getPair([0,5,8],12))
print(getPair([12,12,12,12],12))
print(getPair([-2,-1,-4,1,1,2,-3],-3))


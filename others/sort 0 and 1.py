# Given a binary array {0,1,1,0,0,1,0,0,1} ,
# sort the array in a way that all zeros come to the left
# and all the one's come to the right side of the array.

def sortList(list):
    list.sort()
    return list


print(sortList([0,1,1,0,0,1,0,0,1]))

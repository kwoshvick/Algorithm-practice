lineages = [
    ['A', 'B', 'D'],
    ['A', 'B', 'E'],
    ['A', 'B', 'F'],
    ['A', 'C', 'G', 'H', 'L'],
    ['A', 'C', 'G', 'I'],
    ['A', 'C', 'G', 'J'],
    ['A', 'C', 'K']
]


def getLine(element):
    for lineage in lineages:
        if element in lineage:
            valueList = lineage
            break
    position = valueList.index(element)
    return valueList[:position+1]

def getLeastAncestor(a, b):
    ancestors = []
    lineA = getLine(a)
    lineB = getLine(b)
    for lineAElements in lineA:
        if lineAElements in lineB:
            ancestors.append(lineAElements)
    return ancestors[-1]



print(getLeastAncestor('H','J'))
print(getLeastAncestor('F','K'))
print(getLeastAncestor('H','K'))
print(getLeastAncestor('D','B'))
print(getLeastAncestor('B','L'))

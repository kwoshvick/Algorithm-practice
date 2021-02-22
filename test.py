https://www.tutorialspoint.com/python_data_structure/python_graphs.htm

v = ['a','b','c','d','e']
e = []
for i in range(len(v)) :
    if i+1 == len(v):
        e.append((v[0],v[i]))
    else:
        e.append((v[i],v[i+1]))

print(e)

#bd
start_index = v.index('b')
end_index = v.index('d')
clockwise_elements = []
for i in v[start_index+1:]:
    if i == v[end_index]:
        clockwise_elements.append(i)
        break
    else:
        clockwise_elements.append(i)


print(clockwise_elements)

p = v[end_index:]
m = v[:start_index] + p[::-1]

print(m)

rV = []
for i in range(len(m)) :
    rV.append((m[i],m[i+1]))






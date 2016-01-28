#defining a and initializing aList
aList = [1,18,2,'hello',4,'5']

bList = [0,12,13]
#aList = aList.extend(bList)

print aList


print 'aList: ' + str(aList)
print 'bList: ' + str(bList)

print 'Element at index 1 using aList[1]: ' + str(aList[1])
print 'Element at index 3 using aList[3]: ' + str(aList[3])
print 'Element at max index using aList[-1]: ' + str(aList[-1])
print 'Element at index -3 using aList[-3]: ' + str(aList[-3])

# .insert(index, element) will only display new element
# if done before printing
aList.insert(0,10)

print 'Insert new item in bList using bList.insert(index,element): ' + str(aList)


#aList is appended and updated without having to assign to another list

cList = []
aList.append(bList)

print 'Append bList to aList using .append(list): ' + str(aList)



[[10, 1, 2, 'hello', 4, '5', [0, 12, 13]]]
cList[len(aList):] = [aList for i in range(len(aList) - (len(aList)-1))]
print 'cList: ' + str(cList)


dList = [1,2,3,4,5]

print 'dList: ' + str(dList)
print 'dList[len(dList):len(dList)-len(dList):-1]: ' + str(dList[len(dList):len(dList)-len(dList):-1])

print 'dList[len(dList)::-1]: ' + str(dList[len(dList)::-1])

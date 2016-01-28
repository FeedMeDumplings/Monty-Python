#numList = [1,22,200,100] 
newList = raw_input('Enter list: ')
numList = newList.split()

numList = [int(i) for i in numList] 

print numList

Largest = max(numList)
numList.remove(Largest)
secLargest = max(numList)
Total = int(Largest) + int(secLargest)

print 'Largest: ' + str(Largest)
print 'Second Largest: ' + str(secLargest)
print 'Total: ' + str(Total)

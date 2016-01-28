def sum_max_smax(string):
	newList = string.split()
	newList = [int(i) for i in newList]
	
	Largest = max(newList)
	newList.remove(Largest)

	secLargest = max(newList)

	Total = int(Largest) + int(secLargest)
	
	print 'Largest: ' + str(Largest)
	print 'Second Largest: ' + str(secLargest)
	print 'Total: ' + str(Total)

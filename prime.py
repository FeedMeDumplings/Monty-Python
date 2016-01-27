n = int(raw_input('Enter max. value: '))
primeList = []
if n <= 1:
	print('Please enter valid input [x>1]: ')
else:
	for i in range(2,n+1):
		check = True
		for j in range(2,i):
			if i % j == 0:
				check = False
				break
		if check == True:
			primeList.append(i)
	print(primeList)

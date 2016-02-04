getInput = int(raw_input('Enter number ----->\n'))
calcSum = 0

for i in range(1,getInput):
	if getInput % i == 0:
		calcSum += i
if calcSum == getInput:
	print str(getInput) + ' is a perfect number'
else:
	print str(getInput) + ' is not a perfect number'

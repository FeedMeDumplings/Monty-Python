str1 = str(raw_input('Enter string: '))
#stringN = string[::-1] #[begin:end:step]

stringSub = str1[-3:]
stringSubR = stringSub[::-1]
print stringSub
print stringSubR
r = ""
for i in range(len(str1)-1,-1,-1):
	r = r + str1[i]
print r

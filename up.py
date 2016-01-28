#import string
#print string.capwords(userInput)

userInput = str(raw_input('Enter string: '))

strList = userInput.split()
print strList

cStr = ''

for word in strList:
	if not word.isdigit(): 
		cStr = cStr + ' ' + word[:1].upper() + word[1:].lower()
print cStr

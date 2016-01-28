#import string

userInput = str(raw_input('Enter string: '))
#print string.capwords(userInput)

strList = userInput.split()
print strList

cStr = ''

for word in strList:
	cStr = cStr + ' ' + word[:1].upper() + word[1:]
print cStr

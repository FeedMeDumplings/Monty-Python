#def get_int(str1):
#	getting_int = int(''.join(integer for integer in str1 if integer.isdigit()))
#	return getting_int

#strGet = get_int(str(raw_input('Enter string: ')))

#print strGet
inputString = str(raw_input('->\n'))
#r = ''
#s = ''
t = ''
u = ''
'''for i in inputString:
	if i.isdigit():
		r = r + '' + i
print 'Int: ' + r
	
for i in inputString:
	if i.isalpha():
		s = s + '' + i
print 'Char: ' + s
'''
for i in inputString:
	if i.isdigit():
		t = t + '' + i
	else:
		u = u + '' + i
print 'Int: ' + t
print 'Char: ' + u

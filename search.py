import re

searching = re.search(r'cat','dog dog cat cat dog')
#re.search: will find a match anywhere in the string

print searching.group(0)
'''when group() method is called with 0 as its argument,
it returns the pattern matched by the query'''

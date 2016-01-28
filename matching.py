import re

matching = re.match(r'dog','dog cat cat dog')
#re.match: only find matches if they occur at the start of the string

print matching.group(0)

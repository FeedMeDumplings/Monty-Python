import re

matching = re.search(r'dog','cat dog cat')
print matching.group(0)

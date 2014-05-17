# File filter06.py
# for the course "Python: Regular Expressions"

# This is an example file.  No changes are required by the student.

import sys
import re

words = open('words', 'r')

#pattern=r"^([a-z]+)([a-z]+)$"
pattern=r"^([a-z]+)\1$"

regexp = re.compile(pattern, re.VERBOSE)

for word in words:
    result = regexp.search(word)
    if result:
        #sys.stdout.write("%s\t%s\n" % (result.group(1), result.group(2)))
        sys.stdout.write("%s\n" % (result.group(1)))
        
words.close()

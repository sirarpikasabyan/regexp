# File filter01.py
# for the course "Python: Regular Expressions"

import sys
import re

pattern = "Fred"
regexp = re.compile(pattern, re.I) # You have to write this bit

for line in sys.stdin:
    result = regexp.search(line)# You have to write this bit
    if result:
        sys.stdout.write(line)


# File filter03.py
# for the course "Python: Regular Expressions"

# You have to write a regular expression
# pattern to match the "invalid user" lines.
# Match the whole line!

import sys
import re

pattern = r"^\w{3}\s{1,2}\d{1,} \d{2}:\d{2}:\d{2} noether.+Invalid user.+\d{3}$"

regexp = re.compile(pattern)

for line in sys.stdin:
    result = regexp.search(line)
    if result:
        sys.stdout.write(line)


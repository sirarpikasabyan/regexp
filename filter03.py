# File filter03.py
# for the course "Python: Regular Expressions"

# You have to write a regular expression
# pattern to match the "invalid user" lines.
# Match the whole line!

import sys
import re

pattern = r"^RUN \d{6} COMPLETED\. OUTPUT IN FILE \w+\.dat\.$"

regexp = re.compile(pattern)

for line in sys.stdin:
    result = regexp.search(line)
    if result:
        sys.stdout.write(line)


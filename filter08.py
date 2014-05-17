# File filter03.py
# for the course "Python: Regular Expressions"

# You have to write a regular expression
# pattern to match the "invalid user" lines.
# Match the whole line!

import sys
import re

pattern = r"""
(?P<element>[A-Z][a-z])
\s+
(?P<boil>\d+\.\d+)
"""

regexp = re.compile(pattern, re.VERBOSE)

for line in sys.stdin:
    result = regexp.search(line)
    if result:
        sys.stdout.write("%s\t%s\n" % (result.group("element"), result.group("boil")))


# File filter03.py
# for the course "Python: Regular Expressions"

# You have to write a regular expression
# pattern to match the "invalid user" lines.
# Match the whole line!

import sys
import re

pattern = r"""
^
(RUN)\ 
(\d{6})\                        #Job number
COMPLETED\.\ OUTPUT\ IN\ FILE\ 
([a-z]+\.dat)                   #file name
\.
$
"""

regexp = re.compile(pattern, re.VERBOSE)

for line in sys.stdin:
    result = regexp.search(line)
    if result:
        sys.stdout.write("%s\t%s\n" % (result.group(2), result.group(3)))


#!/usr/bin/env python3

import sys
import re

print('filename', sys.argv[0])

#
# print(sys.argv[1], 'is', sys.argv[2], 'years old!')
#
# print('remaining: ', sys.argv[3:])

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

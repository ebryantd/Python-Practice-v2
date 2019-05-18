import re
"""
string = "Two too."

m = re.findall("t[ow]o", string, re.IGNORECASE)

print(m)
"""
"""
line = "123?34 hello?"

m = re.findall("\d", line, re.IGNORECASE)

print(m)
"""
"""
t = "__one__ __two__ __three__"

found = re.findall("__.*?__", t)

for match in found:
    print(match)
"""
"""
line = "I love $"

m = re.findall("\\$", line, re.IGNORECASE)

print(m)
"""

string = "The ghost that says boo haunts the loo."

m = re.findall(".o[o]", string, re.IGNORECASE)

print(m)

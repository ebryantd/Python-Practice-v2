"""
facts = dict()

# add a value
facts["code"] = "fun"
# look up a key
print(facts["code"])

# add a value
facts["Bill"] = "Gates"
# look up a key
print(facts["Bill"])

# add a value
facts["founded"] = 1776
# look up a key
print(facts["founded"])

print(facts)
"""

rhymes = {"1" : "fun",
          "2" : "blue",
          "3" : "me",
          "4" : "floor",
          "5" : "live"}

n = input("Type a number:")

if n in rhymes:
    rhyme = rhymes[n]
    print(rhyme)
else:
    print("not found")

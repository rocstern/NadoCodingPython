import re

word = "cat"

pattern = re.compile("[c.t]")

print(re.match(pattern, word))

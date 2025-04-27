# Regular Expressions
import re
pattern = re.compile(r"\d+")
print(pattern.findall("abc 123 def 456"))

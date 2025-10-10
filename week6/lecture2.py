# You can control the number of replacements by specifying the count parameter:
# Example
# Replace the first 2 occurrences:
import re
txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)

print(" ")
# Match Object
# A Match Object is an object containing information about the search and the result.
# Note: If there is no match, the value None will be returned, instead of the Match Object.
# Example
# Do a search that will return a Match Object:
import re
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)

print(" ")
# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match

# Example
# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S":
import re
txt = "The rain in Spain"
x = re.search(r'\bS\w+', txt)
print(x.span())

print(" ")
# Example
# Print the string passed into the function:
import re
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

print(" ")
# Example
# Print the part of the string where there was a match.
# The regular expression looks for any words that starts with an upper case "S":
import re
txt = "The rain in Spain"
x = re.search(r"\bT\w+", txt)
print(x.group())

# Note: If there is no match, the value None will be returned, instead of the Match Object.
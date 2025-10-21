import re

pattern = r'my_pattern'
text = r'my_text'

re.search() - finds first match
re.findall() - finds all matches
re.sub() - replace matches
re.split() - split by pattern

# Symbol	Meaning	                          Example
# .	        Any character (except newline)	  a.b matches "aab", "acb"
# *	        0 or more repetitions	          ab* matches "a", "ab", "abb"
# +	        1 or more repetitions	          ab+ matches "ab", "abb"
# ?	        0 or 1 repetition	              ab? matches "a", "ab"
# {m,n}	    m to n repetitions	              a{2,4} matches "aa", "aaa", "aaaa"
# ^	        Start of string	                  ^Hello matches "Hello world"
# $	        End of string	                  world$ matches "Hello world"
# []	    Character set	                  [abc] matches "a", "b", or "c"
# `	        OR operator	                      `a	b` matches "a" or "b"
# ()	    Grouping	                      (ab)+ matches "ab", "abab"
#6. Reverse Words
# Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We

def reverse_w(s):
    words = s.split()
    return ' '.join(words[::-1])
a = input()
print(reverse_w(a))
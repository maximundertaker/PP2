def count_up_to(n):
    for i in range(1, n + 1):
        yield i 
n = int(input())

for x in count_up_to(n):
    print(x)
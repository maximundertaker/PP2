# 4. Write a Python program that invoke square root function after specific milliseconds.

# Sample Input:
# 25100
# 2123
# Sample Output:
# Square root of 25100 after 2123 miliseconds is 158.42979517754858

import time
num = int(input())
ms = int(input())
time.sleep(ms / 1000)
print(f"Square root of {num} after {ms} miliseconds is {pow(num, 0.5)}")
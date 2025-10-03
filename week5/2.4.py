# Date Difference in Seconds
# Write a Python program to calculate two date difference in seconds.

from datetime import datetime

date1 = datetime(2024, 1, 1, 12, 0, 0)
date2 = datetime(2024, 1, 2, 12, 0, 0)

diff = (date2 - date1).total_seconds()
print(diff)
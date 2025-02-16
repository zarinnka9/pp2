from datetime import datetime

date1 = datetime(2024, 2, 15, 12, 0, 0)  # Example date 1
date2 = datetime(2024, 2, 17, 14, 30, 0)  # Example date 2

difference = abs((date2 - date1).total_seconds())

print("Difference in seconds:", difference)

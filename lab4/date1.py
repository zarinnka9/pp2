from datetime import datetime, timedelta
 
current_date = datetime.now()
 
new_date = current_date - timedelta(days=5)
 
print("Current Date and Time:", current_date)
print("Date and Time after subtracting 5 days:", new_date)
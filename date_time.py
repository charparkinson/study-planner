from datetime import datetime

# current date in the format dd/mm/yy
current_date = datetime.now()
print(current_date.strftime("%d %B %Y"))

# current time
current_time = datetime.now()
print(current_time.strftime("%X"))
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'] 
minutes = []
for day in days:
    daily_mins = int(input(f"{day} : "))
    minutes.append(daily_mins)

max_minute = max(minutes)
total = sum(minutes)
average = round(total/len(minutes) ,2)

max_days = []
for i in range(len(minutes)):
    if(minutes[i] == max_minute):
     max_days.append(days[i])

print(f"Average minutes are {average} Minutes")
if(len(max_days) == 1):
 print(f"Most Active Day was {max_days[0]} with {max_minute} Minutes")
else:
   print(f"Most Active Days were {'-'.join(max_days)} with {max_minute} Minutes each")
print(f"Total minutes of week are {total} Minutes")
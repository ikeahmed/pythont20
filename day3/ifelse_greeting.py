from datetime import datetime
now = datetime.now()

if now.hour < 12:
  print('Good Morning')
elif now.hour < 20:
  print('Good Afternoon')
else:
  print('Good Evening')
import datetime
x =  int(datetime.date.today().strftime("%Y"))
z =  int(datetime.date.today().strftime("%w"))
from datetime import datetime
mera = 0
months = range(1 ,13)
for year in range( x , x + 10):
    for month in months:
        if datetime(year, month, z).weekday() == 0:
            mera += 1
print(mera)

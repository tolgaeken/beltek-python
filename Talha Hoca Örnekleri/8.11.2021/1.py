from datetime import date, datetime
import time



start = datetime.now()
time.sleep(5)
finish = datetime.now()
finish = str(finish - start).split(".")[0]


print(finish)
today = date.today()

print(today)

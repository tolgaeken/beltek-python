from datetime import datetime
import time

now = datetime.now().second
time.sleep(5)

finish = datetime.now().second
finish = str(finish - now)


# now = datetime.now()
# time.sleep(5)

# finish = datetime.now()
# finish = str(finish - now)

# finish = str(finish - now).split(".")[0]

print(finish)
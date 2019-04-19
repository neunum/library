import schedule
import time
from .utills import deadline_end

schedule.every().day.at("15:00").do(deadline_end)
schedule.every(1).minutes.do(print('działam'))

while 1:
    schedule.run_pending()
    time.sleep(1)

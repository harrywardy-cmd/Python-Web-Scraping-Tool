import schedule 
import time

def func():
    print("Hello World!")

schedule.every(1).minutes.do(func)

while True:
    schedule.run_pending()
    time.sleep(1)
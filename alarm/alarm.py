import time

waitTime = 1
reset = False
def alarm():
    print("Alarm reset")
    while 1:
        time.sleep(waitTime)
        print("Alarm activated")
       #  return True

alarm()
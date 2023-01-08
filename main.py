import pyautogui
import datetime
import time



currentdate = datetime.date.today()
currentweekday = datetime.datetime.today().weekday()
status = 'n'
timeschedule = '15:50:00'

if currentweekday == 6:
    currentstrweekday = 'sunday'
if currentstrweekday == 0:
    currentstrweekday = 'Monday'
if currentstrweekday == 1:
    currentstrweekday = 'Tuesday'
if currentstrweekday == 2:
    currentstrweekday = 'Wednesday'
if currentstrweekday == 3:
    currentstrweekday = 'Thursday'
if currentstrweekday == 4:
    currentstrweekday = 'Friday'
if currentstrweekday == 5:
    currentstrweekday = 'Saturday'


def JoinClass():
    status = 'y'
    pyautogui.moveTo(1058, 1079, duration=1)
    pyautogui.moveTo(1058, 1051, duration=1)
    pyautogui.leftClick()
    pyautogui.moveTo(856, 51, duration=1)
    pyautogui.leftClick()
    time.sleep(1)
    pyautogui.press('backspace ')
    pyautogui.write('PUT URL IN LINE 16 OF CODE FIRST!!!!!')
    pyautogui.press('enter')
    while status == 'y':
        currentime = time.strftime("%H:%M:%S")
        time.sleep(1)
        print("Joining with time "+currentime+" and day "+currentstrweekday)
        break
    
if currentweekday in [0, 1, 3, 5, 6]:
    print("Today's Day is not in the class DataBase, Do You Want a custom db for today?")
    customdb = str(input("y for Yes and n for No : "))
    if customdb == 'y':
        customstrdb = "a"
        timeschedule = str(input("What is the time for the joining of class?"))
        print("Ok! I will join your class on "+timeschedule)
    else:
        customstrdb = "No"
        print("Stop Doing These Silly Things, However I have canceled my automation as required")
        time.sleep(1)
        exit()

print("Your class will be joined on "+timeschedule+" "+currentstrweekday)
while True:
    currentime = time.strftime("%H:%M:%S")
    
    if status == 'n':
        time.sleep(1)
        print("Running with time "+currentime+" and day "+currentstrweekday+" With "+customstrdb+" Custom Schedule")
    if currentime == timeschedule:
        if currentweekday == 2:
            JoinClass()
            time.sleep(5)
            break
        elif currentweekday == 4:
            JoinClass()
            time.sleep(5)
            break
        elif customdb == 'y':
            JoinClass()
            time.sleep(5)
            break




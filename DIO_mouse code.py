import pyautogui,random
import time
w,h = pyautogui.size()
try:
	time1=float(input('enter time gap in sec:'))
	time2=float(input('enter time gap2 in sec:'))
except:
	print('not a valid input')
	time.sleep(3)
	while True:
		pass

time.sleep(1)
while True:
	for i in range(random.randint(1,10)):
		xaxis_ran = random.randint(700+(i*i),1000+(i*i))
		yaxis_ran = random.randint(300+(i*i),600+(i*i))
		pyautogui.moveTo(xaxis_ran, yaxis_ran, duration=0.25)
	time.sleep(random.uniform(time1,time2))

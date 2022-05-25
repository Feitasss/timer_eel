import eel
import time


eel.init("web")

# timer function
@eel.expose
def timer(minutes, seconds):
	
	if minutes == '':
		minutes = 0
	if seconds == '':
		seconds = 0

	minutes = int(minutes)
	seconds = int(seconds)

	if seconds == 0 and minutes == 0:
		eel.show_time('minutes>0,  seconds>0')
		time.sleep(3)
		eel.show_time('Timer')

	if seconds > 59 or minutes > 59:
		eel.show_time('minutes<60,  seconds<60')
		time.sleep(3)
		eel.show_time('Timer')

	else:
		seconds += minutes*60

		for seconds in range(seconds, -1, -1):
			strMinutes = str(seconds//60)
			strSeconds = str(seconds%60)
			# print(f"{strMinutes.zfill(2)}:{strSeconds.zfill(2)}")
			eel.show_time(f"{strMinutes.zfill(2)}:{strSeconds.zfill(2)}")
			time.sleep(1)

			if seconds == 0:
				# print("Time is up!")
				eel.show_time('Finish')
				time.sleep(3)
				eel.show_time('Timer')

eel.start("index.html", size=(400, 550))
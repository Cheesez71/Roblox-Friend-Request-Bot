#Created by Cheesez.
#NOTE: works only for windows!
import pyautogui
import time
import os
import sys
import webbrowser

time.sleep(5)
i = 1; #it means the first user of roblox: "ROBLOX".
while True:
	try:
		webbrowser.open("https://www.roblox.com/users/" + str(i) + "/profile")
		time.sleep(4)
		pyautogui.click(1332, 383)
		time.sleep(1)
		i = i + 1;
		os.system("taskkill /f /im chrome.exe")
		print(str(i))
	except KeyboardInterrupt:
		os.system("taskkill /f /im chrome.exe")
		exit()
	
#I hope you enjoyed while you running this code.
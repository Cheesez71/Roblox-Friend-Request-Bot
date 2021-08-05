#Created by Cheesez.
import pyautogui
import time
import os
import sys
import webbrowser

time.sleep(5)
i = 205509;
while True:
	webbrowser.open("https://www.roblox.com/users/" + str(i) + "/profile")
	time.sleep(4)
	pyautogui.click(1332, 383)
	time.sleep(1)
	i = i + 1;
	os.system("taskkill /f /im chrome.exe")
	print(str(i))
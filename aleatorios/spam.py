import pyautogui
import time

limite_msg = input("numero msg: ")
msg = input("qual a msg: ")
i = 0
time.sleep(5)
while i < int(limite_msg):
  pyautogui.press("Enter")
  i += 1

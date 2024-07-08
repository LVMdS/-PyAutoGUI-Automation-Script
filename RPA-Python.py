import pyautogui
import time

pyautogui.alert('O codigo esta runnando')
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('https://drive.google.com/drive/u/0/home')
pyautogui.press('enter')
pyautogui.hotkey('winleft','d')

pyautogui.moveTo(1555, 25)
pyautogui.mouseDown()
pyautogui.moveTo(807, 569)
pyautogui.hotkey('alt','tab')
time.sleep(1)
pyautogui.mouseUp()

time.sleep(5)

pyautogui.alert('se foi ruando')
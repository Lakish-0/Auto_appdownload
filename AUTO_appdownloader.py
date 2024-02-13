import pyautogui
import time


che = pyautogui.locateCenterOnScreen("microsoft_logo.png", confidence=0.9)
        
pyautogui.moveTo(che, duration=1)
pyautogui.click()
app_name = pyautogui.prompt(text="", title="Enter app you want to download")
time.sleep(2)
bar = pyautogui.locateCenterOnScreen("bar_.png", confidence=0.333)
pyautogui.moveTo(bar, duration=2)
pyautogui.click()
time.sleep(1)
pyautogui.write(app_name)
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(265, 405)
time.sleep(2)
get = pyautogui.locateCenterOnScreen("intsall.png", confidence=0.8)
pyautogui.moveTo(get, duration=2)
pyautogui.click()
pyautogui.prompt(text="App is downloading\nLakish Dev", title="Downloading")




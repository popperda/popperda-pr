import pyautogui
import keyboard
def autoclick():
    while True:
        if keyboard.is_pressed(' '):
            break
        pyautogui.PAUSE = 0.1
        print("hi")
        pyautogui.click()
print(pyautogui.position())
while True:
    if keyboard.is_pressed('.'):
        autoclick()
 
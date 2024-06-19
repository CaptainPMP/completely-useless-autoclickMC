import keyboard
import pyautogui
import mouse
def start(timing):
    keyboard.wait("i")
    while(True):
        time.sleep(timing/1000)
        mouse.click("right")
        if keyboard.is_pressed("p"):
            break

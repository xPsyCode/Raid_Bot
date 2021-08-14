import cv2
from capture import WindowCapture
import pygetwindow
import time
import pyautogui


class Utility:

    @classmethod
    def template_matching(cls,image:str):
        win = WindowCapture("Raid: Shadow Legends")
        img = win.get_screenshot()
        temp = cv2.imread(image)
        res =cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        return max_val, max_loc

    @classmethod
    def resize_window(cls):
        win = pygetwindow.getWindowsWithTitle("Raid: Shadow Legends")[0]
        win.size = (1296, 759)

    @classmethod
    def reconnect(cls):
        win = WindowCapture("Raid: Shadow Legends")
        img = win.get_screenshot()
        temp = cv2.imread("Template_Images/con_lost.png")
        res =cv2.matchTemplate(img, temp, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        if max_val > 0.9:
            time.sleep(1)
            pyautogui.click(win.get_screen_position((max_loc[0]+20,max_loc[1]+20)))
        time.sleep(1)
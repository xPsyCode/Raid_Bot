import cv2
from capture import WindowCapture
import pygetwindow
import win32gui


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
        # hwnd = win32gui.FindWindow(None, "Raid: Shadow Legends")
        # rect = win32gui.GetWindowRect(hwnd)
        # x = rect[0]
        # y = rect[1]
        # w = rect[2] - x
        # h = rect[3] - y
        # print((h,w))
        # (759, 1296)
        win = pygetwindow.getWindowsWithTitle("Raid: Shadow Legends")[0]
        win.size = (1296, 759)
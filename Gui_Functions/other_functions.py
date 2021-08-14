from PySide6.QtWidgets import QLabel
import pyautogui
import cv2
import time
from Utility import Utility
from capture import WindowCapture
class Other_Functions:

    def __init__(self):
        self.finish = True
        self.win = WindowCapture("Raid: Shadow Legends")

    def autoclicker(self,label:QLabel):
        style = label.styleSheet()
        label.setStyleSheet(style + "color: rgb(15, 226, 0);")
        while not self.finish:
            Utility.reconnect()
            pyautogui.click(self.win.get_screen_position((680,665)))
            time.sleep(28)
        label.setStyleSheet(style)

    def autoseller(self):
        time.sleep(0.5)
        for i in range(6):
            for j in range(6):
                pyautogui.click(self.win.get_screen_position((880-(100*j),(660-(100*i)))))

    def set_finish(self, finish):
        self.finish = finish

    def is_finish(self):
        return self.finish
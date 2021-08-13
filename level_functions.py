from PySide6.QtWidgets import QLabel
from Utility import Utility
import pyautogui
from capture import WindowCapture
import time


class Level_Function():
    finish = True
    def __init__(self):
        self.win = WindowCapture("Raid: Shadow Legends")
        self.finish = True

    def _vk(self):
        max_val, max_loc = Utility.template_matching("Template_Images/art.jpg")
        if max_val >= 0.7:
            pyautogui.click(self.win.get_screen_position((max_loc[0]+20,max_loc[1]+20)))
            time.sleep(0.5)
            max_val, max_loc = Utility.template_matching("Template_Images/button.jpg")
            pyautogui.click(self.win.get_screen_position((max_loc[0]+20,max_loc[1]+20)))
            time.sleep(0.5)
            pyautogui.click(self.win.get_screen_position((800,400)))
    
    def run(self,counterlbl:QLabel,statuslbl:QLabel,counter:int):
        Utility.resize_window()
        style = statuslbl.styleSheet()
        statuslbl.setStyleSheet(style[0:27]+" color: rgb(15, 226, 0);")
        statuslbl.setText("Bot is running")
        for i in range(counter):
            counterlbl.setText(str(counter - i))
            if(self.finish):
                break
            while not self.finish:
                max_val, max_loc = Utility.template_matching("Template_Images/temp.jpg")
                if max_val >= 0.7:
                    time.sleep(1.5)
                    self._vk()
                    time.sleep(1)
                    pyautogui.click(self.win.get_screen_position((max_loc[0]+50,max_loc[1]+20)))
                    time.sleep(3)
                    break
        counterlbl.setText(str(0))
        statuslbl.setStyleSheet(style[0:27]+"color: rgb(221, 0, 0);")
        statuslbl.setText("Bot isn't running")
    def set_finish(self,fin):
        self.finish = fin

    def is_finish(self):
        return self.finish
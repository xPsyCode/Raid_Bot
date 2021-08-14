from Utility import Utility
from PySide6.QtWidgets import QLabel
import cv2
import pyautogui
import time
from capture import WindowCapture

class Minotaurus:
    def __init__(self):
        self.finish = True
        self.win = WindowCapture("Raid: Shadow Legends")

    def run(self, statuslbl:QLabel,refilllbl:QLabel,refill:int):
        refilllbl.setText(str(refill))
        style = statuslbl.styleSheet()
        refill_counter = refill
        statuslbl.setStyleSheet(style[0:27]+" color: rgb(15, 226, 0);")
        statuslbl.setText("Bot is running")
        Utility.resize_window()
        while not self.finish:
            max_val_btn, max_loc_btn = Utility.template_matching("Template_Images/temp.jpg")
            if max_val_btn >= 0.7:
                time.sleep(3)
                max_val_roll = Utility.template_matching("Template_Images/roll.png")[0]
                max_val_count= Utility.template_matching("Template_Images/roll_zahl.png")[0]
                max_val_refill, max_loc_refill = Utility.template_matching("Template_Images/refill.png")
                if(max_val_roll >= 0.89 and max_val_count >= 0.78):
                    self.finish = True
                elif max_val_refill >= 0.9:
                    if refill_counter > 0:
                        pyautogui.click(self.win.get_screen_position((max_loc_refill[0],max_loc_refill[1]+305)))
                        time.sleep(2)
                        pyautogui.click(self.win.get_screen_position((max_loc_btn[0]+50,max_loc_btn[1]+20)))
                        refill_counter -= 1
                        refilllbl.setText(str(refill_counter))
                    else:
                        refilllbl.setText(str(0))
                        pyautogui.click(self.win.get_screen_position((max_loc_btn[0]+50,max_loc_btn[1]+20)))
                        time_count = 0
                        while time_count < 180 and not self.finish:
                            time.sleep(1)
                            time_count +=1
                else:
                    pyautogui.click(self.win.get_screen_position((max_loc_btn[0]+50,max_loc_btn[1]+20)))
                    time.sleep(2)
            Utility.reconnect()
        refilllbl.setText(str(0))
        statuslbl.setStyleSheet(style[0:27]+"color: rgb(221, 0, 0);")
        statuslbl.setText("Bot isn't running")

    def set_finish(self,finish):
        self.finish = finish

    def is_finish(self):
       return self.finish


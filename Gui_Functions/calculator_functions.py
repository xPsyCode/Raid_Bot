import math

from PySide6.QtWidgets import QLineEdit

class Calculator:
    def __init__(self):
        self.switch = False

    def acc_res_cal(self,acc_input:QLineEdit,res_input:QLineEdit):
        acc = 0 if acc_input.text() == "" else int(acc_input.text())
        res = 0 if res_input.text() == "" else int(res_input.text())
        if ((acc - res) <= - 30):
            er = 0.3 + 0.67 * (1 - math.e **(3*(0.3 - ((res - acc)/100))))
        else:
            er = 0.03 + 0.27 * math.e ** (6*(((res - acc)/100)-0.3))
        er = er if self.switch else 1-er
        return str(round(round(er,4)*100,2))+"%"
        
    def set_switch(self, switch):
        self.switch = switch

    def is_switch(self):
        return self.switch
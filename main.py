from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
import sys
from ui_Raid import Ui_MainWindow

import images_rc

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
       
        #PAGE CHANGE
        self.ui.level_Btn.clicked.connect(lambda: self.ui.main_Stack.setCurrentWidget(self.ui.level_Page))
        self.ui.dungeon_Btn.clicked.connect(lambda: self.ui.main_Stack.setCurrentWidget(self.ui.dungeon_Page))
        self.ui.auto_Btn.clicked.connect(lambda: self.ui.main_Stack.setCurrentWidget(self.ui.other_Page))
        self.ui.cal_Btn.clicked.connect(lambda: self.ui.main_Stack.setCurrentWidget(self.ui.cal_Page))
        self.ui.info_Btn.clicked.connect(lambda: self.ui.main_Stack.setCurrentWidget(self.ui.info_Page))
        self.ui.dragon_Btn.clicked.connect(lambda: self.ui.dungeon_Stack.setCurrentWidget(self.ui.dragon_Page))
        self.ui.golem_Btn.clicked.connect(lambda: self.ui.dungeon_Stack.setCurrentWidget(self.ui.golem_Page))
        self.ui.knight_Btn.clicked.connect(lambda: self.ui.dungeon_Stack.setCurrentWidget(self.ui.knight_Page))

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
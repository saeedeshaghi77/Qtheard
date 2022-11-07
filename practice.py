from PySide6.QtWidgets import QApplication,QWidget
from PySide6.QtUiTools import QUiLoader
from functools import partial
from PySide6.QtCore import QThread,Signal
import random 
import time
class Main (QWidget):
    def __init__(self):
        super(Main,self).__init__()
        loader= QUiLoader()
        self.ui=loader.load('fourm.ui')
        self.ui.btn_s_c.clicked.connect(self.start_color)
        self.ui.btn_st_c.clicked.connect(self.stop_color)
        self.ui.btn_s_num.clicked.connect(self.start_number)
        self.ui.btn_st_num.clicked.connect(self.stop_number)
        self.color=Color()
        self.number=Number()
        self.ui.show()
  
    def start_color(self):
        self.color.start()
        self.color.color_stp_signal.connect(self.update_color)
    def update_color(self):
        self.ui.label_color.setStyleSheet(f"background-color: rgb({self.color.r},{self.color.g},{self.color.b})")    
        self.ui.label_color.setText(f"background-color: rgb({self.color.r},{self.color.g},{self.color.b})")    
    def stop_color(self):
        self.color.terminate()

    def start_number(self):
        self.number.start()
        self.number.number_stp_signal.connect(self.update_number)
    def update_number(self):
        self.ui.lbl_num.setText(f"Random number : {self.number.num}")
    def stop_number(self):
        self.number.terminate()    



class Color(QThread):
    color_stp_signal=Signal()
    def __init__(self):
        QThread.__init__(self)
        self.r=0
        self.g=0
        self.b=0

    def set(self):
        self.r=random.randint(0,255)
        self.g=random.randint(0,255)
        self.b=random.randint(0,255)

    def run(self):
        while True:
            self.set()
            self.color_stp_signal.emit()
            time.sleep(1) 

class Number(QThread):
    number_stp_signal=Signal()
    def __init__(self):
        QThread.__init__(self)
        self.num=0
    
    def set_num(self):
        self.num=random.randint(0,100)    
    
    def run_num(self):
        while True:
            self.set_num()
            self.number_stp_signal.emit()
            time.sleep(1)
app=QApplication()
main=Main()
app.exit(app.exec())
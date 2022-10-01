import json
import random
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QPushButton
import sys
import os
from win32 import win32gui


class MainWindow(QWidget):
    """ 
    主窗口
    """
    def __init__(self):
        super().__init__()
        self.get_name_list()
        self.counter = 0
        self.initUI()
        
    def initUI(self):
        self.setGeometry(500,300,400,300)
        self.setStyleSheet(""" 
                           background: #2f3542; 
                           """)
        self.setWindowTitle("Victim-Generator")
        self.setFixedSize(self.width(), self.height())
        icon = QIcon()
        icon.addFile("icon.svg")
        self.setWindowIcon(icon)
        self.show()
        
        self.pb1 = QPushButton("抽取",self)
        self.pb1.setStyleSheet(""" 
                               QPushButton{
                               background-color: none;
                               border:3px solid #ffffff;
                               border-radius:20px;
                               color:#ffffff;
                               font-family:KaiTi;
                               font-size:36px;
                               font-weight:bold;
                               }
                               QPushButton:hover{
                               background-color: #ffffff;
                               color:#2f3542;
                               }
                               """)
        self.pb1.setGeometry(100,200,200,80)
        self.pb1.clicked.connect(self.choose_name)
        self.pb1.show()
        
        # self.pb2 = QPushButton("重置",self)
        
        self.lab = QLabel(self)
        self.lab.setGeometry(80,60,240,90)
        self.lab.setStyleSheet(""" 
                               QLabel{
                               background-color: none;
                               font-size:72px;
                               font-family:KaiTi;
                               font-weight:bold;
                               color:white;
                               }
                               QLabel:hover{
                               color:red;
                               }
                               """)
        self.lab.setAlignment(QtCore.Qt.AlignCenter)
        self.lab.show()
        
        #历史
        self.pb2 = QPushButton(self)
        self.pb2.setGeometry(400-40,0,40,40)
        self.pb2.setText("H")
        self.pb2.setStyleSheet("""
                               QPushButton{
                               font-size:32px;
                               font-weight:bold;
                               color:white;
                               border:0px solid #ffffff;
                               border-radius:10px;
                               }
                               QPushButton:hover{
                               background-color: #ffffff;
                               color:#2f3542;
                               }
                               """)
        self.pb2.clicked.connect(lambda: os.popen("python history.py"))
        self.pb2.show()
        
        #修改
        self.pb2 = QPushButton(self)
        self.pb2.setGeometry(400-80,0,40,40)
        self.pb2.setText("C")
        self.pb2.setStyleSheet("""
                               QPushButton{
                               font-size:32px;
                               font-weight:bold;
                               color:white;
                               border:0px solid #ffffff;
                               border-radius:10px;
                               }
                               QPushButton:hover{
                               background-color: #ffffff;
                               color:#2f3542;
                               }
                               """)
        self.pb2.clicked.connect(lambda: os.popen("python editor.py"))
        self.pb2.show()
        
        #排行
        self.pb2 = QPushButton(self)
        self.pb2.setGeometry(400-120,0,40,40)
        self.pb2.setText("T")
        self.pb2.setStyleSheet("""
                               QPushButton{
                               font-size:32px;
                               font-weight:bold;
                               color:white;
                               border:0px solid #ffffff;
                               border-radius:10px;
                               }
                               QPushButton:hover{
                               background-color: #ffffff;
                               color:#2f3542;
                               }
                               """)
        self.pb2.clicked.connect(lambda: os.popen("python statistic.py"))
        self.pb2.show()
        
    def get_name_list(self):
        with open("./namelist.json","r") as f:
            self.namelist = json.loads(f.read())
        # print(len(self.namelist))
        
    def choose_name(self):
        if len(self.namelist)!=0:            
            name = random.choice(self.namelist)
            self.namelist.remove(name)
            # print(self.namelist)
            with open("./history.csv","a") as f:
                f.write(name+",")
        else:
            self.counter += 1
            if self.counter <3:
                name = "没有啦"
            elif self.counter <6:
                self.lab.setStyleSheet(""" 
                               QLabel{
                               background-color: none;
                               font-size:58px;
                               font-family:KaiTi;
                               font-weight:bold;
                               color:white;
                               }
                               QLabel:hover{
                               color:red;
                               }
                               """)
                name = "(*/ω\*)"
            elif self.counter < 9:
                name = "(≧□≦)"
            else :
                name = "(°Д °)"
            if self.counter == 13:
                os.popen("python EE.py")
        self.lab.setText(name)
        
        
if __name__ == "__main__":
    try:
        h = win32gui.FindWindow(None,"Victim-Generator")
        win32gui.SetForegroundWindow(h)
    except:
        app = QApplication(sys.argv)
        box = MainWindow()
        app.exit(app.exec_())
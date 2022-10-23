from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QLabel
from PyQt5.QtGui import QIcon
import sys
import re
import json

class MainWin(QWidget):
    def __init__(self):
        super(MainWin,self).__init__()
        self.initUI()
        
    def initUI(self):
        #初始化界面
        self.setGeometry(600,400,400,300)
        self.setStyleSheet(""" 
                           background: #2f3542;
                           color:white; 
                           """)
        self.setWindowTitle("Bless YOU!")
        self.setFixedSize(self.width(), self.height())
        icon = QIcon()
        icon.addFile("icon.svg")
        self.setWindowIcon(icon)
        
        #文本框
        self.te = QTextEdit(self)
        self.te.setReadOnly(True)
        self.te.setGeometry(10,30,280,260)
        self.te.setStyleSheet(""" 
                           background: white;
                           color:#2f3542;
                           font-family:KaiTi;
                           font-size:26px;
                           font-weight:bold;
                           """)
        self.refresh()
        # self.te.setText(self.namelist2text())
        self.te.show()
        
        self.warning = QLabel(self)
        self.warning.setGeometry(310,80,80,140)
        self.warning.setWordWrap(True)
        self.warning.setStyleSheet(""" 
                           background: #2f3542;
                           color:white;
                           font-family:KaiTi;
                           font-size:16px;
                           font-weight:bold;
                           """)
        self.warning.setText("福星高照\n前程似锦\n")

        self.lb = QLabel(self)
        self.lb.setGeometry(165,10,40,20)
        self.lb.setWordWrap(True)
        self.lb.setStyleSheet(""" 
                           background: #2f3542;
                           color:white;
                           font-family:KaiTi;
                           font-size:14px;
                           font-weight:bold;
                           """)
        self.lb.setText("bias")

        self.show()   
        
    def refresh(self):
        with open("./history.csv","r") as f:
            self.namelist = re.findall(r"[^, ]+",f.read())
        with open("./namelist.json","r") as f:
            named = json.loads(f.read())
        namedict = dict()
        for n in named:
            namedict[n] = 0
        for n in self.namelist:
            try:
                namedict[n] += 1
            except:
                namedict[n] = 0
        self.te.setText(self.namedict2text(namedict))

    def namedict2text(self,namedict:dict)->str:
        text = ""
        min_v = min(namedict.values())
        namedict = sorted(namedict.items(),key=lambda x:x[1],reverse=True)
        for i,(key,value) in enumerate(namedict):
            text = text + str(i+1) + "-" + key + ":\t" + str(value-min_v) + "\n"
        return text
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    box = MainWin()
    app.exit(app.exec_())
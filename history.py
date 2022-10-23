from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QPushButton,QMessageBox
from PyQt5.QtGui import QIcon
import sys
import re

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
        self.setWindowTitle("history")
        self.setFixedSize(self.width(), self.height())
        icon = QIcon()
        icon.addFile("icon.svg")
        self.setWindowIcon(icon)
        
        #文本框
        self.te = QTextEdit(self)
        self.te.setReadOnly(True)
        self.te.setGeometry(10,10,280,280)
        self.te.setStyleSheet(""" 
                           background: white;
                           color:#2f3542;
                           font-family:KaiTi;
                           font-size:16px;
                           font-weight:bold;
                           """)
        self.refresh_history()
        # self.te.setText(self.namelist2text())
        self.te.show()

        self.pb1 = QPushButton(self)
        self.pb1.clicked.connect(self.clean)
        self.pb1.setGeometry(310,20,80,40)
        self.pb1.setStyleSheet(""" 
                           background: white;
                           border:3px solid #ffffff;
                           border-radius:20px;
                           font-size:16px;
                           font-weight:bold;
                           color:#2f3542;
                           """)
        self.pb1.setText("清空")
        
        

        self.show()   
        
    def clean(self):
        a = QMessageBox.question(self,"QAQ","确定要清空历史记录吗?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if a == QMessageBox.Yes:    
            with open("./history.csv","w") as f:
                f.write("")
            self.refresh_history()
        else:
            pass

    def namelist2text(self)->str:
        text = ""
        for n in self.namelist:
            text = text + n + "\n"
        return text

    def refresh_history(self):
        with open("./history.csv","r") as f:
            self.namelist = re.findall(r"[^,]+",f.read())
        self.te.setText(self.namelist2text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    box = MainWin()
    app.exit(app.exec_())
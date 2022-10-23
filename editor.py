from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QPushButton,QLabel,QMessageBox
from PyQt5.QtGui import QIcon
import sys
import json
import re

LISTNAME = "namelist.json"

def text2json(text:str):
    text = re.findall(r"[^\n]+",text)
    with open("./%s"%LISTNAME,"w+") as f:
        f.write(json.dumps(text))


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
        self.setWindowTitle("NameListEditor")
        self.setFixedSize(self.width(), self.height())
        icon = QIcon()
        icon.addFile("icon.svg")
        self.setWindowIcon(icon)
        
        #文本框
        self.te = QTextEdit(self)
        self.te.setGeometry(10,10,280,280)
        self.te.setStyleSheet(""" 
                           background: white;
                           color:black;
                           font-family:KaiTi;
                           font-size:16px;
                           font-weight:bold;
                           """)
        self.refresh_namelist()
        # self.te.setText(self.namelist2text())
        self.te.show()
        
        
        #确认按钮
        self.yb = QPushButton(self)
        self.yb.clicked.connect(self.changenamelist)
        self.yb.setGeometry(310,10,80,40)
        self.yb.setStyleSheet(""" 
                           background: white;
                           border:3px solid #ffffff;
                           border-radius:20px;
                           color:#2f3542;
                           """)
        self.yb.setText("确认修改")
        
        #刷新按钮
        self.rb = QPushButton(self)
        self.yb.clicked.connect(self.refresh_namelist)
        self.rb.setGeometry(310,90,80,40)
        self.rb.setStyleSheet(""" 
                           background: white;
                           border:3px solid #ffffff;
                           border-radius:20px;
                           color:#2f3542;
                           """)
        self.rb.setText("刷新")
        
        #警告栏
        self.warning = QLabel(self)
        self.warning.setGeometry(310,170,80,80)
        self.warning.setWordWrap(True)
        self.warning.setStyleSheet(""" 
                           background: #2f3542;
                           color:white;
                           
                           """)
        self.warning.setText("读改文件为namelist.json,请严格按照格式修改！如有问题概不负责！")
        
        
        #导入按钮
        #以后再做吧
        
        
        self.show()
    
    def changenamelist(self):
        a = QMessageBox.question(self,"QAQ","确定要进行更改吗?",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
        if a == QMessageBox.Yes:
            text = self.te.toPlainText()
            text2json(text) 
            QMessageBox.information(self,"QAQ","或许你做出了重大改变")
    

    def namelist2text(self)->str:
        text = ""
        for n in self.namelist:
            text = text + n + "\n"        
        return text

    def refresh_namelist(self):
        with open("./%s"%LISTNAME,"r") as f:
            self.namelist = json.loads(f.read())
        self.te.setText(self.namelist2text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    box = MainWin()
    app.exit(app.exec_())
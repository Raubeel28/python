import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QPushButton,QWidget,QHBoxLayout
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1=QPushButton("#1")
        self.button2=QPushButton("#4")
        self.button3=QPushButton("#3")
        self.initUI()
    def initUI(self):
        centralWidgets=QWidget()
        self.setCentralWidget(centralWidgets)
        hbox=QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        centralWidgets.setLayout(hbox)
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")




        self.setStyleSheet("""
                           QPushButton{font-size :40px;
                           font-family:Arial;
                           padding:15px 75px;
                           margin:25px;
                           border:3px solid;
                           border-radius:15px
                           }
                           QPushButton#button1{
                           background-color:red;}
                           QPushButton#button2{
                           background-color:green}
                           QPushButton#button3{
                           background-color:blue}
                           """)







if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
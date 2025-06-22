import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QLineEdit,QPushButton
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.LineEdit=QLineEdit(self)
        self.button=QPushButton("submit",self)
        self.initUI()

    def initUI(self):
        self.LineEdit.setGeometry(10,10,200,40)
        self.button.setGeometry(210,10,100,40)
        self.LineEdit.setStyleSheet("font-size:25px;"
                                    "font-family:Arial")
        self.button.setStyleSheet("font-size: 25px;"
                                  "font-family: Arial")
        self.LineEdit.setPlaceholderText("Enter your Name!!")
        
        self.button.clicked.connect(self.Submit)
    def Submit(self):
        #print("You Clicked The Button")
        text=self.LineEdit.text()
        print(f"Hello {text}")


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
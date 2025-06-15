import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QRadioButton,QButtonGroup
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.radio1=QRadioButton("Visa",self)
        self.radio2=QRadioButton("MasterCard",self)
        self.radio3=QRadioButton("GiftCard",self)
        self.radio4=QRadioButton("In-Store",self)
        self.radio5=QRadioButton("Online",self)
        self.button_group1=QButtonGroup(self)
        self.button_group2=QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.radio1.setGeometry(0,0,300,50)
        self.radio2.setGeometry(0,50,300,50)
        self.radio3.setGeometry(0,100,300,50)
        self.radio4.setGeometry(0,150,300,50)
        self.radio5.setGeometry(0,200,300,50)
        
        self.setStyleSheet("QRadioButton{"
                           "font-size:40px;"
                           "font-family:Arial;"
                           "padding:10px}")
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)

        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)
        self.radio1.toggled.connect(self.radioChange)
        self.radio2.toggled.connect(self.radioChange)
        self.radio3.toggled.connect(self.radioChange)
        self.radio4.toggled.connect(self.radioChange)
        self.radio5.toggled.connect(self.radioChange)
        

    def radioChange(self):
        radioButton=self.sender()
        if radioButton.isChecked():
            print(f"{radioButton.text()} is selected")
        
        




if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

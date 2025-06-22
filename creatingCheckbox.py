import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QCheckBox
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.checkbox=QCheckBox("Do You Want To Party",self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("font-size:30px;"
                                    "font-family:Arial;")
        self.checkbox.setChecked(True)
        self.checkbox.stateChanged.connect(self.checkbox_Changed)

    def checkbox_Changed(self,state):
        print(state)
        if state==Qt.Checked:
            print("You  Like food")
        else:
            print("You do not like food")
        
        #print("You like Food")
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


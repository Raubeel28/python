import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import QTimer,QTime,Qt

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_Label=QLabel(self)
        self.timer=QTimer()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,500,100)

        vbox=QVBoxLayout()
        vbox.addWidget(self.time_Label)
        self.setLayout(vbox)
        self.time_Label.setAlignment(Qt.AlignCenter)
        self.time_Label.setStyleSheet("font-size:150px;"
                                      "font-family:Arial;"
                                      "color:green")
        self.setStyleSheet("background-color:black;")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)
        self.update_time()
        

    def update_time(self):
        current_time=QTime.currentTime().toString("hh:mm:ss AP")
        self.time_Label.setText(current_time)

if __name__=="__main__":
    app=QApplication(sys.argv)
    clock=DigitalClock()
    clock.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *


class Output(QMainWindow):

    def __init__(self):
        super(Output, self).__init__()
        self.setGeometry(450, 250, 500, 350)
        self.setWindowTitle('Method')
        self.output()
        self.stylesheet = '''
        QMainWindow{
            background-color: #F8CCD9;
        }
        QLabel {
            font: bold 18px;
            font-style: arial;
        }
        QPushButton {
            background-color: #EC769A;
            border-style: outset;
            border-width: 2px;
            border-radius: 22px;
            border-color: black;
            font: bold 12px;
            padding: 6px;
        }
        QPushButton:hover {
            background-color: #F199B3;
            border-style: inset;
            font: bold 13px;
        }
        QPushButton:pressed {
            background-color: #E75480;
            border-style: inset;
            font: bold 12px;
        }

        QPushButton:disabled {
            background-color: #F3AAC0;
            border-color: grey;
            border-style: inset;
        }
        QGraphicsView{
            background-color: #DCDCDC;
            border-style: outset;
            border-radius: 5px;
            border-color: white;
            border-width: 3px;
        }
        '''
        self.setStyleSheet(self.stylesheet)

    def output(self):
        #LABEL
        label = QLabel('OUTPUT', self)
        label.move(215,15)

        #SHOW OUTPUT
        outputBox = QGraphicsView(self)
        outputBox.setGeometry(105, 60, 300, 250)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Output()
    ui.show()

    sys.exit(app.exec_())
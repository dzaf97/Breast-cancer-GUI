import sys

from PyQt5.QtWidgets import *
from Method import *


class Classification(QMainWindow):

    def __init__(self):
        super(Classification, self).__init__()
        self.setGeometry(450, 250, 500, 350)
        self.setWindowTitle('Classification')
        self.classification()
        self.stylesheet = '''
        QMainWindow{
            background-color: #F8CCD9;
        }
        QLabel {
            font: bold 14px;
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
        QLineEdit {
            background-color: white;
            border-radius: 10px;
            border: 2px solid black;
            color: white;
        }
        QProgressBar {
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center;
        }
        QProgressBar::chunk {
            background-color: #FFC0CB;
            margin: 0.5px;
            width: 10px;
        }
        '''
        self.setStyleSheet(self.stylesheet)

    def classification(self):
        #LABEL
        label = QLabel('Project Name:', self)
        label.move(40, 20)
        label2 = QLabel('File Path:', self)
        label2.move(70, 60)
        label3 = QLabel('CHOOSE CLASSIFICATION', self)
        label3.resize(200, 25)
        label3.move(180, 110)

        #TEXT INPUT BOX
        text = QLineEdit(self)
        text.resize(335, 25)
        text.move(150, 25)
        text.setDisabled(True)
        text2 = QLineEdit(self)
        text2.resize(335, 25)
        text2.move(150, 65)
        text2.setDisabled(True)

        #BUTTON
        btn1 = QPushButton('CLASSIFICATION 1', self)
        # btn.clicked.connect(QCoreApplication.instance().quit)
        btn1.resize(150, 45)
        btn1.move(90, 150)
        btn2 = QPushButton('CLASSIFICATION 2', self)
        # btn.clicked.connect(QCoreApplication.instance().quit)
        btn2.resize(150, 45)
        btn2.move(90, 210)
        btn3 = QPushButton('CLASSIFICATION 3', self)
        # btn.clicked.connect(QCoreApplication.instance().quit)
        btn3.resize(150, 45)
        btn3.move(290, 150)
        btn4 = QPushButton('CLASSIFICATION 4', self)
        # btn.clicked.connect(QCoreApplication.instance().quit)
        btn4.resize(150, 45)
        btn4.move(290, 210)
        btn5 = QPushButton('PROCEED', self)
        btn5.clicked.connect(self.nextWindow)
        self.centralWidget()
        btn5.resize(150, 45)
        btn5.move(190, 280)

        self.show()

    def nextWindow(self):
        self.window = QMainWindow()
        self.ui = Method()
        self.ui.method()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Classification()
    ui.show()

    sys.exit(app.exec_())
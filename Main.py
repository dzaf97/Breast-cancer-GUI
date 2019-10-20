from Classification import *
from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(450, 250, 500, 350)
        #self.setFixedSize(self.size())
        self.setWindowTitle('Main')
        self.main()


    def main(self):

        #LABEL
        label = QLabel('Project Name:', self)
        label.move(40, 20)
        label2 = QLabel('File Path:', self)
        label2.move(70, 60)

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
        btn3 = QPushButton('PROCEED', self)
        btn3.setEnabled(False)
        btn3.resize(150, 45)
        btn3.move(190, 280)
        btn3.clicked.connect(self.nextWindow)

        btn = QPushButton('LOAD DATASET', self)
        btn.resize(150, 45)
        btn.move(335, 150)
        btn.clicked.connect(self.file_open)
        btn.clicked.connect(lambda: btn3.setEnabled(True))

        #PROGRESS BAR
        self.progress = QProgressBar(self)
        self.progress.setGeometry(150, 110, 335, 25)

        self.show()

    def nextWindow(self):
        self.window = QMainWindow()
        self.ui = Classification()
        self.ui.classification()
        self.close()

    def file_open(self, btn):
        name = QFileDialog.getOpenFileName(self, 'Open File')

        #PROGRESS FOR UPLOADING FILE
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.00005
            self.progress.setValue(self.completed)




if __name__ == "__main__":

    stylesheet = '''
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
        border-color: #2F4F4F;
        border-style: inset;
    }
    QLineEdit {
        background-color: white;
        border-radius: 10px;
        border: 2px solid black;
        color: white;
    }
    QProgressBar {
        border: 2px solid #708090;
        border-radius: 5px;
        text-align: center;
        font: bold;
    }
    QProgressBar::chunk {
        background-color: #F199B3;
        margin: 0.5px;
        width: 10px;
    }
    '''
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.setStyleSheet(stylesheet)
    ui.show()

    sys.exit(app.exec_())

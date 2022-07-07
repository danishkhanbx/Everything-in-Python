from PyQt5.QtWidgets import *


class Widgets(QWidget):
    def __init__(self):
        super(Widgets, self).__init__()
        self.vlayout = QVBoxLayout()

        self.hlayout1 = QHBoxLayout()
        self.l1 = QLabel()
        self.l1.setText('Enter your name')
        self.hlayout1.addWidget(self.l1)
        self.t1 = QLineEdit()
        self.hlayout1.addWidget(self.t1)
        self.vlayout.addLayout(self.hlayout1)

        self.hlayout2 = QHBoxLayout()
        self.l2 = QLabel()
        self.l2.setText('Enter your age')
        self.hlayout2.addWidget(self.l2)
        self.t2 = QLineEdit()
        self.hlayout2.addWidget(self.t2)
        self.vlayout.addLayout(self.hlayout2)

        self.bttn = QPushButton('Submit')
        self.bttn.clicked.connect(self.onclick)
        self.vlayout.addWidget(self.bttn)

        self.setLayout(self.vlayout)

    def onclick(self):
        print(f'My name is {self.t1.text()} and age is {self.t2.text()}')


def window():
    app = QApplication([])
    wig = Widgets()
    wig.setWindowTitle('PyQt5')
    wig.show()
    app.exec_()


if __name__ == '__main__':
    window()

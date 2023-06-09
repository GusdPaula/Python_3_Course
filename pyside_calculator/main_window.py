from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget



class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # Setting the basic layout
        self.cw = QWidget()
        self.vLayout = QVBoxLayout()
        self.cw.setLayout(self.vLayout)
        self.setCentralWidget(self.cw)

        # Window title
        self.setWindowTitle('Calculator')


    def adjustFixedSize(self):
        # The last things to be done
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
    

    def addWidgetToVLayout(self, widget: QWidget):
        self.vLayout.addWidget(widget)

    
    def addLayoutToVlayout(self, layout):
        self.vLayout.addLayout(layout)



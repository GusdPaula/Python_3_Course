from typing import Optional
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QMainWindow
from PySide6.QtCore import Slot

class MyWindow(QMainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        self.button = QPushButton('click')
        self.button.setStyleSheet('font-size: 40px; color: red;')
        self.button_2 = QPushButton('click 2')

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button_2)
        self.central_widget.setLayout(self.layout)

        self.status_bar = self.statusBar()
        self.status_bar.showMessage('Mostrar msg')

        self.menu = self.menuBar()
        self.primeiro_menu = self.menu.addMenu('Coisa')
        self.primeira_acao = self.primeiro_menu.addAction('Ação')
        self.primeira_acao.triggered.connect(self.slot_example)

        self.segunda_acao = self.primeiro_menu.addAction('Segunda Ação')
        self.segunda_acao.setCheckable(True)
        self.segunda_acao.toggled.connect(self.slot_example_c)
        self.button.clicked.connect(self.slot_example)
        
    @Slot()
    def slot_example(self):
        self.status_bar.showMessage('Clicou em ação')


    @Slot()
    def slot_example_c(self, checked):
        print('Está marcado?', checked)
        
if __name__ == "__main__":
    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()
from PySide6.QtWidgets import QApplication, QLineEdit
import sys
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from display import Display
from info import Info
from styles import setupTheme
from buttons import Button, ButtonsGrid

if __name__ == '__main__':
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Setting the icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('code')
    window.addWidgetToVLayout(info)

    # Display
    display = Display('0')
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display)
    window.addLayoutToVlayout(buttonsGrid)

    # Run all
    window.adjustFixedSize()
    window.show()
    app.exec()
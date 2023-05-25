from PySide6.QtWidgets import QApplication, QLineEdit
import sys
from main_window import MainWindow
from variables import WINDOW_ICON_PATH
from PySide6.QtGui import QIcon
from display import Display

# Setting the theme
sys.argv += ['-platform', 'windows:darkmode=2']

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()

    # Setting the icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Display
    display = Display('0')
    display.setStyleDisplay()
    window.addWidgetToVLayout(display)


    # Run all
    window.adjustFixedSize()
    window.show()
    app.exec()
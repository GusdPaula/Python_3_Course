from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from display import Display
from PySide6.QtCore import Slot


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleButton()


    def setStyleButton(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(60, 60)



class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self._makeGrid()
        self._emptyDisplay = True
    

    def _makeGrid(self):
        rowIdx = 0
        for row in self._gridMask:
            colIdx = 0
            for item in row:
                button = Button(item)

                if not isNumOrDot(item):
                    button.setProperty('cssClass', 'specialButton')

                if isEmpty(item):
                    colIdx += 1
                    continue

                elif item != '0':
                    self.addWidget(button, rowIdx, colIdx)
                
                elif item == '0':
                    self.addWidget(button, rowIdx, 0, 1, 2)
                
                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertNumberToDisplay,
                    button)

                button.clicked.connect(buttonSlot)

                colIdx += 1

            rowIdx += 1
    
    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        
        return realSlot
    

    def _insertNumberToDisplay(self, button):
        if self._emptyDisplay == True:
            self.display.clear()
            self._emptyDisplay = False

        if isNumOrDot(button.text()):
            newDisplayValue = self.display.text() + button.text()
            if not isValidNumber(newDisplayValue):
                return False
            
            self.display.insert(button.text())
        
        elif button.text() == "C":
            self.display.setText('0')
            self._emptyDisplay = True




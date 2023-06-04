from PySide6.QtWidgets import QPushButton, QGridLayout
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isEmpty, isValidNumber
from display import Display
from PySide6.QtCore import Slot

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from display import Display
    from info import Info

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
    def __init__(self, display: 'Display', info: 'Info', *args, **kwargs):
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
        self._info = info
        self._equation = ''
        self._left = None
        self._right = None
        self._op = None

    @property
    def equation(self):
        return self._equation


    @equation.setter
    def equation(self, value):
        self._equation = value
        self._info.setText(value)


    def _makeGrid(self):
        rowIdx = 0
        for row in self._gridMask:
            colIdx = 0
            for item in row:
                button = Button(item)

                if not isNumOrDot(item):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                if isEmpty(item):
                    colIdx += 1
                    continue

                elif item != '0':
                    self.addWidget(button, rowIdx, colIdx)
                
                elif item == '0':
                    self.addWidget(button, rowIdx, 0, 1, 2)
                
                slot_ = self._makeSlot(
                    self._insertNumberToDisplay,
                    button)

                self._connectButtonClicked(button, slot_)
                
                colIdx += 1

            rowIdx += 1
    

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot) # type: ignore
    

    def _configSpecialButton(self, button):
        text = button.text()

        if text in '+-/*':
            self._connectButtonClicked(
                button, 
                self._makeSlot(self._operatorClicked, button))


    def _makeSlot(self, func, *args, **kwargs):
        
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
            self._clear()


    def _clear(self):
        self.display.setText('0')
        self._emptyDisplay = True
        self._left = None
        self._right = None
        self._op = None
        self.equation = ''

    def _operatorClicked(self, button):
        buttonText = button.text()
        displayText = self.display.text()
        self.display.clear()


        # Se a pessoa clicou no operador sem
        # configurar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            return False
        
        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = float(displayText)
        
        self._op = buttonText
        self.equation = f'{self._left} {self._op}'


from PyQt5.QtWidgets import *

def fillTab1(widget):
    widget.layout = QVBoxLayout()
    pushbutton = QPushButton("PyQt5 button")
    widget.layout.addWidget(pushbutton)
    return widget.layout
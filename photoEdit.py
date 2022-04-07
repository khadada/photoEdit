# Importing necessary Module and classes
import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QStatusBar,QAction,QTextEdit,QToolBar,QDockWidget)
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon


class BasicMenuGui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initialize_ui()
        self.show()
    
    def initialize_ui(self):
        """
        Initialize the window and & display its content to the screen.
        """
        self.setGeometry(100, 50, 500, 700)
        self.setWindowTitle("Basic Menu v.1")
        
        # set Central Widget for main window
        self.setCentralWidget(QTextEdit())
        
        self.create_menu()
        self.create_toolbar()
        self.create_dockwidget()
        
    
        
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
        
    
    def create_menu(self):
        """
        Create menubar & menu actions.
        """
        # Create Actions for "File" menu:
        self.exit_action = QAction(QIcon("icons/close.png"), "Exit",self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.setToolTip("Quit the program (T_T)")
        self.exit_action.triggered.connect(self.close)
        
        # Create Actions for "View" menu:
        full_screen_action = QAction(QIcon("icons/fullscreen.png"),"Full screen", self)
        full_screen_action.setCheckable(True)
        full_screen_action.setToolTip("Switch to full screen mode")
        full_screen_action.setShortcut("Ctrl+Shift+F")
        full_screen_action.triggered.connect(self.switch_on_fullscreen)
        
        # Create menubar
        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        
        # Create file menu & add its actions:
        file_menu = menu_bar.addMenu("File")
        file_menu.addAction(self.exit_action)
        
# Run Program 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BasicMenuGui()
    sys.exit(app.exec_())        
        
        
    
        
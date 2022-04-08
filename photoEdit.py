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
        
        # Create View menu, Appearance submenu, and add actions:
        view_menu = menu_bar.addMenu("View")
        submenu_of_view = view_menu.addMenu("Appearance")
        submenu_of_view.addAction(full_screen_action)
        
        # Display info about tools, menu, and view in the status bar:
        self.setStatusBar(QStatusBar(self))
    
    def create_toolbar(self):
        """
        Create toolbar for GUI 
        """
        # Setup toolbar
        tool_bar = QToolBar("Main Toolbar")
        tool_bar.setIconSize(QSize(20, 20))
        self.addToolBar(tool_bar)
        
        # Add Actions to toolbar
        tool_bar.addAction(self.exit_action)
        
    def create_dockwidget(self):
        """
        Create dock widget
        """
        # Setup dock widget:
        dock_widget = QDockWidget()
        dock_widget.setWindowTitle("Example Dock")
        dock_widget.setAllowedAreas(Qt.AllDockWidgetAreas)
        
        # Set main widget for dok widget
        dock_widget.setWidget(QTextEdit())
        
        # Set inital location of dock widget in main window
        self.addDockWidget(Qt.LeftDockWidgetArea, dock_widget) 
        
    def switch_on_fullscreen(self,state):
        """
        If state is True, then Display the main window in full screen. otherwise return the window to normal.
        """
        if state:
            self.showFullScreen()
        else:
            self.showNormal()
# Run Program 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BasicMenuGui()
    sys.exit(app.exec_())        
        
        
    
        
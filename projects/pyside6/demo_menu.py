import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QKeySequence, QWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox


class Dialog(QDialog):
    ...


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle("Author:ID:1135395")

        # Menu
        self.menu = self.menuBar()
        self.main = self.menu.addMenu("Menu")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        self.main.addAction(exit_action)

        about_action = QAction("About", self)
        about_action.triggered.connect(self.about)
        self.main.addAction(about_action)

        # Status Bar
        self.status = self.statusBar()
        # self.status.showMessage("Data loaded and plotted")

        # Window dimensions
        geometry = self.screen().availableGeometry()
        self.setFixedSize(geometry.width() * 0.6, geometry.height() * 0.7)

    def about(self):
        msg = f"this is a about messagebox, nice awesome"
        QMessageBox.information(self, "about", msg)


if __name__ == '__main__':
    app = QApplication()
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

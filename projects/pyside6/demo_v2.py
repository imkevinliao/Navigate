import sys

from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextBrowser, QGridLayout


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.edit1 = None
        self.text_browser = None
        self.init_ui()

    def init_ui(self):
        self.edit1 = QLineEdit()
        self.edit1.setText("input any thing")

        btn1 = QPushButton("btn1 append", self)
        btn2 = QPushButton("btn2 clean ", self)
        btn1.clicked.connect(self.btn1_func)
        btn2.clicked.connect(self.btn2_func)

        self.text_browser = QTextBrowser()
        self.text_browser.setText("Hello, world!")

        main_layout = QGridLayout(self)
        main_layout.addWidget(self.edit1, 1, 0)
        main_layout.addWidget(btn1, 1, 1)
        main_layout.addWidget(btn2, 1, 2)
        main_layout.addWidget(self.text_browser, 2, 0, 2, 3)
        self.setLayout(main_layout)
        self.setWindowTitle("demo2")

    def btn1_func(self):
        text = self.edit1.text()
        self.text_browser.append(text)
        ...

    def btn2_func(self):
        self.text_browser.clear()
        ...


if __name__ == '__main__':
    app = QApplication()
    win = MyWidget()
    win.show()
    sys.exit(app.exec())

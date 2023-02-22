# pyside6
PyQt 的入门参考
# 界面设置
高清屏幕自适应设置，以及界面风格设置
```angular2html
QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

QApplication.setStyle(QStyleFactory.create('Fusion'))
```

# QPushButton
btn = QPushButton("ok", self)
btn.clicked.connect(func)

# QLineEdit
edit = QLineEdit()
edit.setText()
edit.text()

# QTextBrowser
browser =  QTextBrowser()
browser.setText()
browser.append("your text")
browser.clear()

# QGridLayout
main_layout = QGridLayout(self)
main_layout = addWidget(self.btn,1,0)
main_layout = addWidget(self.browser,2,0,2,3)
self.setLayout(main_layout)

# 窗口大小
geometry = self.screen().availableGeometry()
self.setFixedSize(geometry().width*0.8,geometry.height()*0.7)


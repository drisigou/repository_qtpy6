from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton,QLabel,QLineEdit,QWidget,QVBoxLayout
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI Title")
        self.container=QWidget()
        self.layout= QVBoxLayout()

        self.label = QLabel("Label:")
        self.line_edit = QLineEdit()

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.line_edit)

        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
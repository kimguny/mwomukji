import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from page_home import HomePage
from page_mode import ModePage
from page_select import SelectPage
from page_result import ResultPage
import styles


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("뭐먹지?")
        self.setFixedSize(560, 680)
        self.setStyleSheet(styles.WINDOW)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.home   = HomePage(self.go_mode)
        self.mode   = ModePage(self.go_home, self.go_select, self.go_result)
        self.select = SelectPage(self.go_mode, self.go_result)
        self.result = ResultPage(self.go_mode)

        self.stack.addWidget(self.home)    # 0
        self.stack.addWidget(self.mode)    # 1
        self.stack.addWidget(self.select)  # 2
        self.stack.addWidget(self.result)  # 3

    def go_home(self):   self.stack.setCurrentIndex(0)
    def go_mode(self):   self.stack.setCurrentIndex(1)
    def go_select(self): self.stack.setCurrentIndex(2)

    def go_result(self, menu):
        self.result.set_menu(menu)
        self.stack.setCurrentIndex(3)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

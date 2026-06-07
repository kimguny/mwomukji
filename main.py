import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from pages.page_home import HomePage
from pages.page_mode import ModePage
from pages.page_select import SelectPage
from pages.page_result import ResultPage
from pages.page_browse import BrowsePage
import styles


# QStackedWidget으로 여러 페이지를 겹쳐 관리하고 인덱스로 전환하는 메인 창
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("뭐먹지?")
        self.resize(560, 680)
        self.setStyleSheet(styles.WINDOW)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        self.home   = HomePage(self.go_mode)
        self.mode   = ModePage(self.go_home, self.go_select, self.go_result_random, self.go_browse)
        self.select = SelectPage(self.go_mode, self.go_result_select)
        self.result = ResultPage(self.go_mode, self.go_select)
        self.browse = BrowsePage(self.go_mode, self.go_result_browse)

        # 인덱스 순서: 0=홈, 1=모드, 2=선택, 3=결과, 4=탐색
        self.stack.addWidget(self.home)
        self.stack.addWidget(self.mode)
        self.stack.addWidget(self.select)
        self.stack.addWidget(self.result)
        self.stack.addWidget(self.browse)

    def go_home(self):
        self.stack.setCurrentIndex(0)

    def go_mode(self):
        self.stack.setCurrentIndex(1)

    def go_select(self):
        self.select.reset()
        self.stack.setCurrentIndex(2)

    def go_result_random(self, menus):
        self.result.start(menus, mode="random")
        self.stack.setCurrentIndex(3)

    def go_result_select(self, menus):
        self.result.start(menus, mode="select")
        self.stack.setCurrentIndex(3)

    def go_result_browse(self, menus, category):
        self.result.start(menus, mode="random", category=category)
        self.stack.setCurrentIndex(3)

    def go_browse(self):
        self.stack.setCurrentIndex(4)


app = QApplication(sys.argv)
styles.load_fonts()
window = MainWindow()
window.show()
sys.exit(app.exec())

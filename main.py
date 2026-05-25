# main.py
# 앱의 진입점. 창을 생성하고 모든 페이지를 연결해 화면 전환을 관리한다

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from page_home import HomePage
from page_mode import ModePage
from page_select import SelectPage
from page_result import ResultPage
import styles


class MainWindow(QMainWindow):
    # 앱의 메인 창. QStackedWidget을 사용해 여러 페이지를 겹쳐 관리하고,
    # 필요한 페이지를 앞으로 꺼내는 방식으로 화면 전환을 구현한다

    def __init__(self):
        super().__init__()
        self.setWindowTitle("뭐먹지?")
        self.setFixedSize(560, 680)
        self.setStyleSheet(styles.WINDOW)

        # QStackedWidget: 여러 페이지를 스택처럼 쌓아두고 인덱스로 전환하는 위젯
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # 각 페이지 인스턴스 생성 시 이동 함수를 인자로 넘긴다
        # 각 페이지에서 버튼을 누르면 여기서 정의한 go_* 함수가 호출된다
        self.home   = HomePage(self.go_mode)
        self.mode   = ModePage(self.go_home, self.go_select, self.go_result)
        self.select = SelectPage(self.go_mode, self.go_result)
        self.result = ResultPage(self.go_mode)

        # 스택에 페이지를 추가한다 (인덱스 순서: 0=홈, 1=모드, 2=선택, 3=결과)
        self.stack.addWidget(self.home)    # 0
        self.stack.addWidget(self.mode)    # 1
        self.stack.addWidget(self.select)  # 2
        self.stack.addWidget(self.result)  # 3

    def go_home(self):
        # 홈 화면으로 이동
        self.stack.setCurrentIndex(0)

    def go_mode(self):
        # 추천 방식 선택 화면으로 이동
        self.stack.setCurrentIndex(1)

    def go_select(self):
        # 조건 선택 화면으로 이동
        self.stack.setCurrentIndex(2)

    def go_result(self, menu):
        # 결과 화면으로 이동. 선택된 메뉴 데이터를 결과 페이지에 전달한 후 전환한다
        self.result.set_menu(menu)
        self.stack.setCurrentIndex(3)


# 앱 실행
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())

# page_mode.py
# 추천 방식을 선택하는 화면
# "랜덤으로 추천받기"와 "직접 선택하기" 두 가지 경로로 분기한다

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
import styles


class ModePage(QWidget):
    # 추천 방식 선택 화면 위젯
    # go_back   : 홈 화면으로 돌아가는 함수
    # go_select : 조건 선택 화면으로 이동하는 함수
    # go_result : 결과 화면으로 이동하는 함수 (랜덤 추천 시 바로 호출)

    def __init__(self, go_back, go_select, go_result):
        super().__init__()
        self.go_result = go_result  # on_random 메서드에서 사용하기 위해 인스턴스 변수로 저장
        self.setStyleSheet(styles.WINDOW)

        # 전체를 감싸는 세로 레이아웃
        outer = QVBoxLayout()
        outer.setContentsMargins(20, 20, 20, 20)

        # 뒤로가기 버튼 (홈으로 이동)
        back_btn = QPushButton("< 뒤로")
        back_btn.setFixedSize(80, 34)
        back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        back_btn.setStyleSheet(styles.BACK_BTN)
        back_btn.clicked.connect(go_back)

        # 상단 행: 뒤로가기 버튼을 왼쪽에 배치하고 나머지 공간은 비운다
        top_row = QHBoxLayout()
        top_row.addWidget(back_btn)
        top_row.addStretch()

        # 중앙 콘텐츠 레이아웃 (제목 + 버튼 두 개)
        center = QVBoxLayout()
        center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center.setSpacing(16)

        title = QLabel("어떻게 추천받을까요?")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {styles.TEXT}; font-size: 24px; font-weight: bold;")

        subtitle = QLabel("원하는 방식을 선택해주세요")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet(f"color: {styles.SUBTEXT}; font-size: 14px;")

        # 랜덤 추천 버튼: 클릭 시 조건 없이 바로 메뉴를 뽑아 결과 화면으로 이동
        random_btn = QPushButton("랜덤으로 추천받기")
        random_btn.setFixedSize(260, 58)
        random_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        random_btn.setStyleSheet(styles.PRIMARY_BTN)
        random_btn.clicked.connect(self.on_random)

        # 직접 선택 버튼: 클릭 시 조건 선택 화면으로 이동
        select_btn = QPushButton("직접 선택하기")
        select_btn.setFixedSize(260, 58)
        select_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        select_btn.setStyleSheet(styles.OUTLINE_BTN)
        select_btn.clicked.connect(go_select)

        center.addWidget(title)
        center.addWidget(subtitle)
        center.addSpacing(10)
        center.addWidget(random_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        center.addWidget(select_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        # addStretch(1)을 위아래에 동일하게 넣어 중앙 콘텐츠를 수직 가운데 정렬한다
        outer.addLayout(top_row)
        outer.addStretch(1)
        outer.addLayout(center)
        outer.addStretch(1)
        self.setLayout(outer)

    def on_random(self):
        # 전체 메뉴에서 조건 없이 무작위로 1개를 뽑아 결과 화면으로 넘긴다
        from menu_data import load_menus
        from random_recommend import pick_random
        menus = load_menus()
        result = pick_random(menus)
        self.go_result(result)

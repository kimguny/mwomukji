from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
import styles


class ModePage(QWidget):
    def __init__(self, go_back, go_select, go_result):
        super().__init__()
        self.go_result = go_result
        self.setStyleSheet(styles.WINDOW)

        outer = QVBoxLayout()
        outer.setContentsMargins(20, 20, 20, 20)

        back_btn = QPushButton("< 뒤로")
        back_btn.setFixedSize(80, 34)
        back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        back_btn.setStyleSheet(styles.BACK_BTN)
        back_btn.clicked.connect(go_back)

        top_row = QHBoxLayout()
        top_row.addWidget(back_btn)
        top_row.addStretch()

        center = QVBoxLayout()
        center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center.setSpacing(16)

        title = QLabel("어떻게 추천받을까요?")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {styles.TEXT}; font-size: 24px; font-weight: bold;")

        subtitle = QLabel("원하는 방식을 선택해주세요")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet(f"color: {styles.SUBTEXT}; font-size: 14px;")

        random_btn = QPushButton("랜덤으로 추천받기")
        random_btn.setFixedSize(260, 58)
        random_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        random_btn.setStyleSheet(styles.PRIMARY_BTN)
        random_btn.clicked.connect(self.on_random)

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

        outer.addLayout(top_row)
        outer.addStretch(1)
        outer.addLayout(center)
        outer.addStretch(1)
        self.setLayout(outer)

    def on_random(self):
        from menu_data import load_menus
        from random_recommend import pick_random
        menus = load_menus()
        result = pick_random(menus)
        self.go_result(result)

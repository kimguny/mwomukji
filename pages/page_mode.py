from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
import styles


class ModePage(QWidget):

    def __init__(self, go_back, go_select, go_result):
        super().__init__()
        self.go_result = go_result
        self.setStyleSheet(styles.WINDOW)

        outer = QVBoxLayout()
        outer.setContentsMargins(24, 24, 24, 24)

        back_btn = QPushButton("← 뒤로")
        back_btn.setFixedSize(72, 32)
        back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        back_btn.setStyleSheet(styles.BACK_BTN)
        back_btn.setFont(styles.font(13))
        back_btn.clicked.connect(go_back)

        top_row = QHBoxLayout()
        top_row.addWidget(back_btn)
        top_row.addStretch()

        title = QLabel("어떻게 추천받을까요?")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(styles.font(24))
        title.setStyleSheet(f"color: {styles.TEXT}; background: transparent;")

        subtitle = QLabel("원하는 방식을 선택해주세요")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setFont(styles.font(13))
        subtitle.setStyleSheet(f"color: {styles.SUBTEXT}; background: transparent;")

        random_btn = QPushButton("랜덤으로 추천받기")
        random_btn.setFixedSize(280, 52)
        random_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        random_btn.setStyleSheet(styles.PRIMARY_BTN)
        random_btn.setFont(styles.font(15))
        random_btn.clicked.connect(self.on_random)

        select_btn = QPushButton("직접 선택하기")
        select_btn.setFixedSize(280, 52)
        select_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        select_btn.setStyleSheet(styles.OUTLINE_BTN)
        select_btn.setFont(styles.font(15))
        select_btn.clicked.connect(go_select)

        center = QVBoxLayout()
        center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center.setSpacing(14)
        center.addWidget(title)
        center.addSpacing(4)
        center.addWidget(subtitle)
        center.addSpacing(24)
        center.addWidget(random_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        center.addWidget(select_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        outer.addLayout(top_row)
        outer.addStretch(1)
        outer.addLayout(center)
        outer.addStretch(1)
        self.setLayout(outer)

    def on_random(self):
        from utils.loader import load_menus
        from utils.random_recommend import pick_random
        menus = load_menus()
        result = pick_random(menus)
        self.go_result(result)

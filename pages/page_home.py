from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
from utils.loader import get_menu_count
import styles


class HomePage(QWidget):

    def __init__(self, go_mode):
        super().__init__()
        self.setStyleSheet(styles.WINDOW)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(0)

        title = QLabel("뭐먹지?")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(styles.font(38))
        title.setStyleSheet(f"color: {styles.TEXT}; background: transparent;")

        subtitle = QLabel("오늘 뭐 먹을지 골라드릴게요")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setFont(styles.font(14))
        subtitle.setStyleSheet(f"color: {styles.SUBTEXT}; background: transparent;")

        count_label = QLabel(f"총 {get_menu_count()}개 메뉴 중 추천")
        count_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        count_label.setFont(styles.font(12))
        count_label.setStyleSheet(f"color: {styles.SUBTEXT}; background: transparent;")

        btn = QPushButton("추천받기")
        btn.setFixedSize(200, 52)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setStyleSheet(styles.PRIMARY_BTN)
        btn.setFont(styles.font(15))
        btn.clicked.connect(go_mode)

        layout.addStretch(2)
        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(subtitle)
        layout.addSpacing(6)
        layout.addWidget(count_label)
        layout.addSpacing(30)
        layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(3)

        self.setLayout(layout)

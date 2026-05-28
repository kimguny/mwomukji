from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
import styles


# go_mode: 추천 방식 선택 화면으로 이동하는 함수 (main.py에서 전달받음)
class HomePage(QWidget):

    def __init__(self, go_mode):
        super().__init__()
        self.setStyleSheet(styles.WINDOW)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(16)

        title = QLabel("뭐먹지?")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {styles.TEXT}; font-size: 38px; font-weight: bold;")

        subtitle = QLabel("오늘 뭐 먹을지 골라드릴게요!")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet(f"color: {styles.TEXT}; font-size: 15px;")

        btn = QPushButton("추천받기")
        btn.setFixedSize(220, 52)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setStyleSheet(styles.PRIMARY_BTN)
        btn.clicked.connect(go_mode)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(12)
        layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

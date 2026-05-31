from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
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
        layout.addSpacing(36)
        layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(3)

        self.setLayout(layout)

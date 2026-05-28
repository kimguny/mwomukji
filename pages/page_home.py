# page_home.py
# 앱 시작 시 가장 먼저 보이는 홈 화면
# 타이틀과 추천받기 버튼만 있는 단순한 구조

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt
import styles


class HomePage(QWidget):
    # 홈 화면 위젯
    # go_mode: 추천 방식 선택 화면으로 이동하는 함수 (main.py에서 전달받음)

    def __init__(self, go_mode):
        super().__init__()
        self.setStyleSheet(styles.WINDOW)

        # 세로 방향 레이아웃, 가운데 정렬
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(16)

        # 타이틀 텍스트
        title = QLabel("뭐먹지?")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {styles.TEXT}; font-size: 38px; font-weight: bold;")

        # 부제목 텍스트
        subtitle = QLabel("오늘 뭐 먹을지 골라드릴게요!")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet(f"color: {styles.TEXT}; font-size: 15px;")

        # 추천받기 버튼: 클릭하면 go_mode 함수 호출
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

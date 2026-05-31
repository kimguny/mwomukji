import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QStackedWidget, QWidget,
    QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QFontDatabase

# 색상
BG_START   = "#EDE9FF"   # 연보라
BG_END     = "#E0F0FF"   # 연하늘
WHITE      = "#FFFFFF"
TEXT       = "#2D2B55"   # 짙은 보라 계열
SUBTEXT    = "#8B87B0"
ACCENT     = "#A78BFA"   # 소프트 퍼플
ACCENT2    = "#7DD3FC"   # 소프트 스카이블루
PINK       = "#F9A8D4"   # 소프트 핑크
BORDER     = "#E5E0FF"

BG_GRAD = "background-color: white;"

PRIMARY_BTN = f"""
    QPushButton {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 {ACCENT}, stop:1 {ACCENT2});
        color: white;
        font-size: 15px;
        font-weight: bold;
        border-radius: 26px;
        border: none;
    }}
    QPushButton:hover {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #9B72F0, stop:1 #60C0F8);
    }}
    QPushButton:pressed {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #8B62E0, stop:1 #50B0E8);
    }}
"""

OUTLINE_BTN = f"""
    QPushButton {{
        background-color: white;
        color: {TEXT};
        font-size: 15px;
        border-radius: 26px;
        border: 1px solid {BORDER};
    }}
    QPushButton:hover {{ background-color: {BG_START}; }}
    QPushButton:pressed {{ background-color: {BORDER}; }}
"""

BACK_BTN = f"""
    QPushButton {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 {ACCENT}, stop:1 {ACCENT2});
        color: white;
        font-size: 13px;
        font-weight: bold;
        border: none;
        padding: 4px 12px;
        border-radius: 16px;
    }}
    QPushButton:hover {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #9B72F0, stop:1 #60C0F8);
    }}
"""

BASE = "/Users/rlarjs/Project/Python/mwomukji/fonts"

def load_fonts():
    QFontDatabase.addApplicationFont(f"{BASE}/KERISKEDU_B.otf")
    QFontDatabase.addApplicationFont(f"{BASE}/KERISKEDU_R.otf")
    QFontDatabase.addApplicationFont(f"{BASE}/KERISKEDU_Line.otf")

def rounded_font(size, bold=False):
    font = QFont("KERIS KEDU OTF", size)
    return font


class HomeDemo(QWidget):
    def __init__(self, go_next):
        super().__init__()
        self.setStyleSheet(BG_GRAD)

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(0)

        title = QLabel("뭐먹지?")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(rounded_font(38, bold=True))
        title.setStyleSheet(f"color: {TEXT}; background: transparent;")

        subtitle = QLabel("오늘 뭐 먹을지 골라드릴게요")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setFont(rounded_font(14))
        subtitle.setStyleSheet(f"color: {SUBTEXT}; background: transparent;")

        btn = QPushButton("추천받기")
        btn.setFixedSize(200, 52)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setStyleSheet(PRIMARY_BTN)
        btn.setFont(rounded_font(15, bold=True))
        btn.clicked.connect(go_next)

        layout.addStretch(2)
        layout.addWidget(title)
        layout.addSpacing(10)
        layout.addWidget(subtitle)
        layout.addSpacing(36)
        layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addStretch(3)
        self.setLayout(layout)


class ModeDemo(QWidget):
    def __init__(self, go_back, go_next):
        super().__init__()
        self.setStyleSheet(BG_GRAD)

        outer = QVBoxLayout()
        outer.setContentsMargins(24, 24, 24, 24)

        back_btn = QPushButton("← 뒤로")
        back_btn.setFixedSize(72, 32)
        back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        back_btn.setStyleSheet(BACK_BTN)
        back_btn.setFont(rounded_font(13))
        back_btn.clicked.connect(go_back)

        top = QHBoxLayout()
        top.addWidget(back_btn)
        top.addStretch()

        title = QLabel("어떻게 추천받을까요?")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(rounded_font(24, bold=True))
        title.setStyleSheet(f"color: {TEXT}; background: transparent;")

        subtitle = QLabel("원하는 방식을 선택해주세요")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setFont(rounded_font(13))
        subtitle.setStyleSheet(f"color: {SUBTEXT}; background: transparent;")

        random_btn = QPushButton("랜덤으로 추천받기")
        random_btn.setFixedSize(280, 52)
        random_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        random_btn.setStyleSheet(PRIMARY_BTN)
        random_btn.setFont(rounded_font(15, bold=True))
        random_btn.clicked.connect(go_next)

        select_btn = QPushButton("직접 선택하기")
        select_btn.setFixedSize(280, 52)
        select_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        select_btn.setStyleSheet(OUTLINE_BTN)
        select_btn.setFont(rounded_font(15))

        center = QVBoxLayout()
        center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center.setSpacing(14)
        center.addWidget(title)
        center.addSpacing(4)
        center.addWidget(subtitle)
        center.addSpacing(24)
        center.addWidget(random_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        center.addWidget(select_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        outer.addLayout(top)
        outer.addStretch(1)
        outer.addLayout(center)
        outer.addStretch(1)
        self.setLayout(outer)


class ResultDemo(QWidget):
    def __init__(self, go_back):
        super().__init__()
        self.setStyleSheet(BG_GRAD)

        outer = QVBoxLayout()
        outer.setContentsMargins(24, 24, 24, 24)

        back_btn = QPushButton("← 뒤로")
        back_btn.setFixedSize(72, 32)
        back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        back_btn.setStyleSheet(BACK_BTN)
        back_btn.setFont(rounded_font(13))
        back_btn.clicked.connect(go_back)

        top = QHBoxLayout()
        top.addWidget(back_btn)
        top.addStretch()

        tag = QLabel("오늘의 추천")
        tag.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tag.setFixedHeight(30)
        tag.setFont(rounded_font(11, bold=True))
        tag.setStyleSheet(f"""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {ACCENT}, stop:1 {PINK});
            color: white;
            border-radius: 15px;
            padding: 0 16px;
        """)

        name = QLabel("불고기버거")
        name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name.setFont(rounded_font(40, bold=True))
        name.setStyleSheet(f"color: {TEXT}; background: transparent;")

        # 정보 카드
        card = QFrame()
        card.setFixedWidth(320)
        card.setStyleSheet(f"""
            QFrame {{
                background-color: {WHITE};
                border-radius: 24px;
                border: 1px solid {BORDER};
            }}
            QLabel {{
                border: none;
            }}
        """)

        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(28, 22, 28, 22)
        card_layout.setSpacing(12)

        def info_row(label, value):
            row = QHBoxLayout()
            l = QLabel(label)
            l.setFont(rounded_font(13))
            l.setStyleSheet(f"color: {SUBTEXT}; background: transparent;")
            v = QLabel(value)
            v.setFont(rounded_font(13, bold=True))
            v.setStyleSheet(f"color: {TEXT}; background: transparent;")
            row.addWidget(l)
            row.addStretch()
            row.addWidget(v)
            return row

        def divider():
            line = QFrame()
            line.setFrameShape(QFrame.Shape.HLine)
            line.setStyleSheet(f"color: {BORDER};")
            return line

        card_layout.addLayout(info_row("브랜드", "맥도날드"))
        card_layout.addLayout(info_row("가격", "6,000원 ~ 9,000원"))
        card_layout.addLayout(info_row("맵기", "★☆☆☆☆"))
        card_layout.addLayout(info_row("카테고리", "패스트푸드"))
        card.setLayout(card_layout)

        again_btn = QPushButton("다시 추천받기")
        again_btn.setFixedSize(200, 52)
        again_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        again_btn.setStyleSheet(PRIMARY_BTN)
        again_btn.setFont(rounded_font(15, bold=True))
        again_btn.clicked.connect(go_back)

        center = QVBoxLayout()
        center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center.setSpacing(12)
        center.addWidget(tag, alignment=Qt.AlignmentFlag.AlignCenter)
        center.addWidget(name)
        center.addSpacing(6)
        center.addWidget(card, alignment=Qt.AlignmentFlag.AlignCenter)
        center.addSpacing(16)
        center.addWidget(again_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        outer.addLayout(top)
        outer.addStretch(1)
        outer.addLayout(center)
        outer.addStretch(1)
        self.setLayout(outer)


class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("뭐먹지? — UI 데모")
        self.resize(420, 680)

        self.setStyleSheet("background-color: white;")
        self.stack = QStackedWidget()
        self.stack.setStyleSheet("background-color: white;")
        self.setCentralWidget(self.stack)

        self.home   = HomeDemo(self.go_mode)
        self.mode   = ModeDemo(self.go_home, self.go_result)
        self.result = ResultDemo(self.go_mode)

        self.stack.addWidget(self.home)
        self.stack.addWidget(self.mode)
        self.stack.addWidget(self.result)

    def go_home(self):
        self.stack.setCurrentIndex(0)

    def go_mode(self):
        self.stack.setCurrentIndex(1)

    def go_result(self):
        self.stack.setCurrentIndex(2)


app = QApplication(sys.argv)
load_fonts()
window = DemoWindow()
window.show()
sys.exit(app.exec())

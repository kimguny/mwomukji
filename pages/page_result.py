from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt
from utils.formatters import spicy_stars, format_price
import styles


class ResultPage(QWidget):

    def __init__(self, go_back):
        super().__init__()
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

        self.tag = QLabel("오늘의 추천")
        self.tag.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tag.setFixedHeight(30)
        self.tag.setFont(styles.font(11))
        self.tag.setStyleSheet(f"""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {styles.ACCENT}, stop:1 {styles.PINK});
            color: white;
            border-radius: 15px;
            padding: 0 16px;
        """)

        self.name_label = QLabel("")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.setFont(styles.font(36))
        self.name_label.setStyleSheet(f"color: {styles.TEXT}; background: transparent;")

        # 카드 내부 라벨들
        self.brand_label = QLabel()
        self.price_label = QLabel()
        self.spicy_label = QLabel()
        self.cat_label   = QLabel()

        card = QFrame()
        card.setFixedWidth(320)
        card.setStyleSheet(f"""
            QFrame {{
                background-color: {styles.WHITE};
                border-radius: 24px;
                border: 1px solid {styles.BORDER};
            }}
            QLabel {{ border: none; }}
        """)

        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(28, 22, 28, 22)
        card_layout.setSpacing(12)

        for lbl, key in [
            (self.brand_label, "브랜드"),
            (self.price_label, "가격"),
            (self.spicy_label, "맵기"),
            (self.cat_label,   "카테고리"),
        ]:
            row = QHBoxLayout()
            key_lbl = QLabel(key)
            key_lbl.setFont(styles.font(13))
            key_lbl.setStyleSheet(f"color: {styles.SUBTEXT}; background: transparent;")
            lbl.setFont(styles.font(13))
            lbl.setStyleSheet(f"color: {styles.TEXT}; background: transparent;")
            row.addWidget(key_lbl)
            row.addStretch()
            row.addWidget(lbl)
            card_layout.addLayout(row)

        card.setLayout(card_layout)

        again_btn = QPushButton("다시 추천받기")
        again_btn.setFixedSize(200, 52)
        again_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        again_btn.setStyleSheet(styles.PRIMARY_BTN)
        again_btn.setFont(styles.font(15))
        again_btn.clicked.connect(go_back)

        center = QVBoxLayout()
        center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center.setSpacing(12)
        center.addWidget(self.tag, alignment=Qt.AlignmentFlag.AlignCenter)
        center.addWidget(self.name_label)
        center.addSpacing(6)
        center.addWidget(card, alignment=Qt.AlignmentFlag.AlignCenter)
        center.addSpacing(16)
        center.addWidget(again_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        outer.addLayout(top_row)
        outer.addStretch(1)
        outer.addLayout(center)
        outer.addStretch(1)
        self.setLayout(outer)

    # 결과 화면에 표시할 메뉴 데이터를 업데이트한다
    def set_menu(self, menu):
        self.name_label.setText(menu["name"])
        self.brand_label.setText(menu["brand"])
        self.price_label.setText(format_price(menu["price_min"], menu["price_max"]))
        self.spicy_label.setText(spicy_stars(menu["spicy_level"]))
        self.cat_label.setText(menu["category"])

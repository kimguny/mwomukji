from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFrame, QScrollArea
)
from PyQt6.QtCore import Qt
from utils.formatters import spicy_stars, format_price
from utils.random_recommend import pick_random, remove_menu
import styles


class ResultPage(QWidget):

    def __init__(self, go_back):
        super().__init__()
        self.go_back = go_back
        self.remaining = []
        self.history = []
        self.setStyleSheet(styles.WINDOW)

        outer = QVBoxLayout()
        outer.setContentsMargins(24, 24, 24, 24)
        outer.setSpacing(0)

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

        self.again_btn = QPushButton("다시 추천받기")
        self.again_btn.setFixedSize(200, 52)
        self.again_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.again_btn.setStyleSheet(styles.PRIMARY_BTN)
        self.again_btn.setFont(styles.font(15))
        self.again_btn.clicked.connect(self.on_again)

        # 이미 나온 메뉴 목록 영역
        self.history_title = QLabel("이미 나온 메뉴")
        self.history_title.setFont(styles.font(12))
        self.history_title.setStyleSheet(f"color: {styles.SUBTEXT}; background: transparent;")
        self.history_title.hide()

        self.history_layout = QVBoxLayout()
        self.history_layout.setSpacing(4)

        history_container = QWidget()
        history_container.setStyleSheet("background: transparent;")
        history_container.setLayout(self.history_layout)

        scroll = QScrollArea()
        scroll.setWidget(history_container)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setMaximumHeight(120)
        scroll.setStyleSheet(styles.WINDOW)
        self.history_scroll = scroll
        self.history_scroll.hide()

        center = QVBoxLayout()
        center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center.setSpacing(12)
        center.addWidget(self.tag, alignment=Qt.AlignmentFlag.AlignCenter)
        center.addWidget(self.name_label)
        center.addSpacing(6)
        center.addWidget(card, alignment=Qt.AlignmentFlag.AlignCenter)
        center.addSpacing(16)
        center.addWidget(self.again_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        center.addSpacing(16)
        center.addWidget(self.history_title, alignment=Qt.AlignmentFlag.AlignCenter)
        center.addWidget(self.history_scroll)

        outer.addLayout(top_row)
        outer.addStretch(1)
        outer.addLayout(center)
        outer.addStretch(1)
        self.setLayout(outer)

    # 새로운 메뉴 리스트로 결과 화면을 초기화하고 첫 추천을 표시한다
    def start(self, menus):
        self.remaining = menus[:]
        self.history = []
        self._clear_history_ui()
        self.history_title.hide()
        self.history_scroll.hide()
        self.again_btn.setEnabled(True)
        self._pick_next()

    def _pick_next(self):
        menu = pick_random(self.remaining)
        if menu is None:
            return
        remove_menu(self.remaining, menu)
        self._update_card(menu)
        if self.history:
            self._add_history_item(self.history[-1])
        self.history.append(menu)
        if not self.remaining:
            self.again_btn.setEnabled(False)
            self.again_btn.setText("더 이상 없어요")

    def on_again(self):
        self._pick_next()

    def _update_card(self, menu):
        self.name_label.setText(menu["name"])
        self.brand_label.setText(menu["brand"])
        self.price_label.setText(format_price(menu["price_min"], menu["price_max"]))
        self.spicy_label.setText(spicy_stars(menu["spicy_level"]))
        self.cat_label.setText(menu["category"])

    def _add_history_item(self, menu):
        self.history_title.show()
        self.history_scroll.show()
        lbl = QLabel(f"· {menu['name']}  ({menu['category']})")
        lbl.setFont(styles.font(12))
        lbl.setStyleSheet(f"color: {styles.SUBTEXT}; background: transparent;")
        lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.history_layout.addWidget(lbl)

    def _clear_history_ui(self):
        while self.history_layout.count():
            item = self.history_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

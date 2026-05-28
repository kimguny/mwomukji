from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt
from utils.formatters import spicy_stars, format_price
import styles


# go_back: 추천 방식 선택 화면으로 돌아가는 함수
# 메뉴 데이터는 set_menu()로 전달받는다 (위젯 재생성 없이 내용만 교체)
class ResultPage(QWidget):

    def __init__(self, go_back):
        super().__init__()
        self.setStyleSheet(styles.WINDOW)

        back_btn = QPushButton("< 뒤로")
        back_btn.setFixedSize(80, 34)
        back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        back_btn.setStyleSheet(styles.BACK_BTN)
        back_btn.clicked.connect(go_back)

        top_row = QHBoxLayout()
        top_row.addWidget(back_btn)
        top_row.addStretch()

        self.subtitle = QLabel("오늘의 추천!")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle.setStyleSheet(f"color: {styles.SUBTEXT}; font-size: 15px;")

        self.name_label = QLabel("")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.setStyleSheet(f"color: {styles.TEXT}; font-size: 36px; font-weight: bold;")

        # 카드 내부 라벨들 (set_menu() 호출 시 텍스트가 채워진다)
        self.brand_label = QLabel()
        self.price_label = QLabel()
        self.spicy_label = QLabel()
        self.cat_label   = QLabel()

        for lbl in [self.brand_label, self.price_label, self.spicy_label, self.cat_label]:
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            lbl.setStyleSheet(f"color: {styles.TEXT}; font-size: 15px;")

        self.cat_label.setStyleSheet(f"color: {styles.SUBTEXT}; font-size: 13px;")

        card_layout = QVBoxLayout()
        card_layout.setSpacing(8)
        card_layout.addWidget(self.brand_label)
        card_layout.addWidget(self.price_label)
        card_layout.addWidget(self.spicy_label)
        card_layout.addWidget(self.cat_label)

        card = QFrame()
        card.setStyleSheet("background-color: white; border-radius: 16px;")
        card.setLayout(card_layout)
        card.setFixedWidth(340)
        card_layout.setContentsMargins(24, 20, 24, 20)

        again_btn = QPushButton("다시 추천받기")
        again_btn.setFixedSize(220, 52)
        again_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        again_btn.setStyleSheet(styles.PRIMARY_BTN)
        again_btn.clicked.connect(go_back)

        center = QVBoxLayout()
        center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center.setSpacing(14)
        center.addWidget(self.subtitle)
        center.addWidget(self.name_label)
        center.addWidget(card, alignment=Qt.AlignmentFlag.AlignCenter)
        center.addSpacing(6)
        center.addWidget(again_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        # addStretch(1)을 위아래에 동일하게 넣어 수직 가운데 정렬
        outer = QVBoxLayout()
        outer.setContentsMargins(20, 20, 20, 20)
        outer.addLayout(top_row)
        outer.addStretch(1)
        outer.addLayout(center)
        outer.addStretch(1)
        self.setLayout(outer)

    # 결과 화면에 표시할 메뉴 데이터를 업데이트한다 (menu: menus.json 항목 딕셔너리)
    def set_menu(self, menu):
        self.name_label.setText(menu["name"])
        self.brand_label.setText(f"브랜드   {menu['brand']}")
        self.price_label.setText(f"가격     {format_price(menu['price_min'], menu['price_max'])}")
        self.spicy_label.setText(f"맵기     {spicy_stars(menu['spicy_level'])}")
        self.cat_label.setText(f"카테고리  {menu['category']}")

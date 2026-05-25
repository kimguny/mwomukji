# page_result.py
# 추천된 메뉴를 보여주는 결과 화면
# 메뉴명, 브랜드, 가격, 맵기, 카테고리를 카드 형태로 표시한다

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt
import styles


# 맵기 단계(1~5)를 별 기호 문자열로 변환한다
# 예: 3 -> "★★★☆☆"
def spicy_stars(level):
    return "★" * level + "☆" * (5 - level)


# 가격 최솟값과 최댓값을 "X,XXX원 ~ X,XXX원" 형식의 문자열로 변환한다
# 예: (8000, 12000) -> "8,000원 ~ 12,000원"
def format_price(price_min, price_max):
    return f"{price_min:,}원 ~ {price_max:,}원"


# 결과 화면 위젯
# go_back: 추천 방식 선택 화면으로 돌아가는 함수
# 실제 메뉴 데이터는 set_menu()로 별도 전달받는다 (위젯 재생성 없이 내용만 교체)
class ResultPage(QWidget):

    def __init__(self, go_back):
        super().__init__()
        self.setStyleSheet(styles.WINDOW)

        # 뒤로가기 버튼 (추천 방식 선택 화면으로 이동)
        back_btn = QPushButton("< 뒤로")
        back_btn.setFixedSize(80, 34)
        back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        back_btn.setStyleSheet(styles.BACK_BTN)
        back_btn.clicked.connect(go_back)

        # 상단 행: 뒤로가기 버튼 왼쪽 배치
        top_row = QHBoxLayout()
        top_row.addWidget(back_btn)
        top_row.addStretch()

        # "오늘의 추천!" 안내 문구
        self.subtitle = QLabel("오늘의 추천!")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle.setStyleSheet(f"color: {styles.SUBTEXT}; font-size: 15px;")

        # 추천된 메뉴 이름 (크게 표시)
        self.name_label = QLabel("")
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.setStyleSheet(f"color: {styles.TEXT}; font-size: 36px; font-weight: bold;")

        # 정보 카드 내부 라벨들 (브랜드, 가격, 맵기, 카테고리)
        # set_menu() 호출 시 텍스트가 채워진다
        self.brand_label = QLabel()
        self.price_label = QLabel()
        self.spicy_label = QLabel()
        self.cat_label   = QLabel()

        # 브랜드, 가격, 맵기는 기본 텍스트 스타일 적용
        for lbl in [self.brand_label, self.price_label, self.spicy_label, self.cat_label]:
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            lbl.setStyleSheet(f"color: {styles.TEXT}; font-size: 15px;")

        # 카테고리는 보조 색상으로 좀 더 작게 표시
        self.cat_label.setStyleSheet(f"color: {styles.SUBTEXT}; font-size: 13px;")

        # 카드 레이아웃: 네 개의 정보 라벨을 세로로 쌓는다
        card_layout = QVBoxLayout()
        card_layout.setSpacing(8)
        card_layout.addWidget(self.brand_label)
        card_layout.addWidget(self.price_label)
        card_layout.addWidget(self.spicy_label)
        card_layout.addWidget(self.cat_label)

        # 흰 배경의 둥근 카드 프레임
        card = QFrame()
        card.setStyleSheet("background-color: white; border-radius: 16px;")
        card.setLayout(card_layout)
        card.setFixedWidth(340)
        card_layout.setContentsMargins(24, 20, 24, 20)

        # 다시 추천받기 버튼: 클릭 시 go_back 호출 (추천 방식 선택 화면으로 이동)
        again_btn = QPushButton("다시 추천받기")
        again_btn.setFixedSize(220, 52)
        again_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        again_btn.setStyleSheet(styles.PRIMARY_BTN)
        again_btn.clicked.connect(go_back)

        # 중앙 콘텐츠 레이아웃: 안내 문구 + 메뉴명 + 카드 + 버튼
        center = QVBoxLayout()
        center.setAlignment(Qt.AlignmentFlag.AlignCenter)
        center.setSpacing(14)
        center.addWidget(self.subtitle)
        center.addWidget(self.name_label)
        center.addWidget(card, alignment=Qt.AlignmentFlag.AlignCenter)
        center.addSpacing(6)
        center.addWidget(again_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        # 전체 레이아웃: addStretch(1)을 위아래에 동일하게 넣어 수직 가운데 정렬
        outer = QVBoxLayout()
        outer.setContentsMargins(20, 20, 20, 20)
        outer.addLayout(top_row)
        outer.addStretch(1)
        outer.addLayout(center)
        outer.addStretch(1)
        self.setLayout(outer)

    # 결과 화면에 표시할 메뉴 데이터를 업데이트한다
    # main.py의 go_result()에서 화면 전환 전에 호출한다
    # menu: menus.json의 항목 하나 (딕셔너리)
    def set_menu(self, menu):
        self.name_label.setText(menu["name"])
        self.brand_label.setText(f"브랜드   {menu['brand']}")
        self.price_label.setText(f"가격     {format_price(menu['price_min'], menu['price_max'])}")
        self.spicy_label.setText(f"맵기     {spicy_stars(menu['spicy_level'])}")
        self.cat_label.setText(f"카테고리  {menu['category']}")

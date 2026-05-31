from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QButtonGroup, QScrollArea, QFrame
)
from PyQt6.QtCore import Qt
from utils.loader import load_menus
from utils.filter import filter_menus
from utils.random_recommend import pick_random
import styles

CATEGORIES = [
    ("한식", "한식"), ("중식", "중식"), ("일식", "일식"),
    ("양식", "양식"), ("분식", "분식"), ("치킨", "치킨"),
    ("피자", "피자"), ("패스트푸드", "패스트푸드"), ("상관없음", None),
]

PRICE_OPTIONS = [
    ("~1만원", (0, 10000)),
    ("1~2만원", (10000, 20000)),
    ("2만원 이상", (20000, 99999)),
    ("상관없음", None),
]

SPICY_OPTIONS = [
    ("안매움", 1), ("약간", 2), ("보통", 3),
    ("매움", 4), ("아주매움", 5), ("상관없음", None),
]


def make_section_label(text):
    label = QLabel(text)
    label.setFont(styles.font(14))
    label.setStyleSheet(f"color: {styles.TEXT}; background: transparent;")
    return label


def make_toggle_group(options):
    group = QButtonGroup()
    group.setExclusive(True)
    buttons = []
    for label, val in options:
        btn = QPushButton(label)
        btn.setCheckable(True)
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setStyleSheet(styles.TOGGLE_BTN)
        btn.setFont(styles.font(13))
        btn.setProperty("value", val)
        group.addButton(btn)
        buttons.append(btn)
    return group, buttons


class SelectPage(QWidget):

    def __init__(self, go_back, go_result):
        super().__init__()
        self.go_result = go_result
        self.setStyleSheet(styles.WINDOW)

        self.cat_group, cat_btns = make_toggle_group(CATEGORIES)
        self.price_group, price_btns = make_toggle_group(PRICE_OPTIONS)
        self.spicy_group, spicy_btns = make_toggle_group(SPICY_OPTIONS)

        content = QWidget()
        content.setStyleSheet(styles.WINDOW)
        content_layout = QVBoxLayout()
        content_layout.setSpacing(12)
        content_layout.setContentsMargins(30, 20, 30, 20)

        content_layout.addWidget(make_section_label("카테고리"))
        cat_grid = QGridLayout()
        cat_grid.setSpacing(8)
        for i, btn in enumerate(cat_btns):
            cat_grid.addWidget(btn, i // 3, i % 3)
        content_layout.addLayout(cat_grid)

        content_layout.addSpacing(8)
        content_layout.addWidget(self.make_divider())
        content_layout.addWidget(make_section_label("가격대"))
        price_row = QHBoxLayout()
        price_row.setSpacing(8)
        for btn in price_btns:
            price_row.addWidget(btn)
        content_layout.addLayout(price_row)

        content_layout.addSpacing(8)
        content_layout.addWidget(self.make_divider())
        content_layout.addWidget(make_section_label("맵기"))
        spicy_row = QHBoxLayout()
        spicy_row.setSpacing(8)
        for btn in spicy_btns:
            spicy_row.addWidget(btn)
        content_layout.addLayout(spicy_row)

        content_layout.addSpacing(12)
        content_layout.addWidget(self.make_divider())

        self.error_label = QLabel("")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.error_label.setFont(styles.font(13))
        self.error_label.setStyleSheet("color: #E53935; background: transparent;")
        content_layout.addWidget(self.error_label)

        recommend_btn = QPushButton("추천받기")
        recommend_btn.setFixedSize(200, 52)
        recommend_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        recommend_btn.setStyleSheet(styles.PRIMARY_BTN)
        recommend_btn.setFont(styles.font(15))
        recommend_btn.clicked.connect(self.on_recommend)
        content_layout.addWidget(recommend_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        content_layout.addSpacing(10)

        content.setLayout(content_layout)

        scroll = QScrollArea()
        scroll.setWidget(content)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setStyleSheet(styles.WINDOW)

        back_btn = QPushButton("← 뒤로")
        back_btn.setFixedSize(72, 32)
        back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        back_btn.setStyleSheet(styles.BACK_BTN)
        back_btn.setFont(styles.font(13))
        back_btn.clicked.connect(go_back)

        top_row = QHBoxLayout()
        top_row.setContentsMargins(20, 20, 20, 0)
        top_row.addWidget(back_btn)
        top_row.addStretch()

        title = QLabel("조건을 선택하세요")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(styles.font(22))
        title.setStyleSheet(f"color: {styles.TEXT}; background: transparent;")

        outer = QVBoxLayout()
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)
        outer.addLayout(top_row)
        outer.addWidget(title)
        outer.addWidget(scroll)
        self.setLayout(outer)

    def make_divider(self):
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet(f"color: {styles.BORDER};")
        return line

    def reset(self):
        for group in [self.cat_group, self.price_group, self.spicy_group]:
            group.setExclusive(False)
            for btn in group.buttons():
                btn.setChecked(False)
            group.setExclusive(True)
        self.error_label.setText("")

    def on_recommend(self):
        def get_val(group):
            btn = group.checkedButton()
            return btn.property("value") if btn else None

        menus = load_menus()
        filtered = filter_menus(
            menus,
            category=get_val(self.cat_group),
            price_range=get_val(self.price_group),
            spicy_level=get_val(self.spicy_group),
        )
        result = pick_random(filtered)

        if result is None:
            self.error_label.setText("조건에 맞는 메뉴가 없어요. 조건을 바꿔보세요!")
        else:
            self.error_label.setText("")
            self.go_result(result)

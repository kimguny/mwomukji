from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QFrame, QScrollArea, QButtonGroup
)
from PyQt6.QtCore import Qt
from utils.loader import get_categories, get_menus_by_category
from utils.formatters import format_menu_item
import styles


class BrowsePage(QWidget):

    def __init__(self, go_back, go_result):
        super().__init__()
        self.go_result = go_result
        self.current_menus = []
        self.current_category = None
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

        title = QLabel("카테고리 탐색")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(styles.font(24))
        title.setStyleSheet(f"color: {styles.TEXT}; background: transparent;")

        # 카테고리 버튼 그룹
        categories = get_categories()
        self.cat_group = QButtonGroup()
        self.cat_group.setExclusive(True)
        cat_row = QHBoxLayout()
        cat_row.setSpacing(8)
        first_btn = None
        for cat in categories:
            btn = QPushButton(cat)
            btn.setCheckable(True)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(styles.TOGGLE_BTN)
            btn.setFont(styles.font(13))
            btn.setProperty("value", cat)
            btn.clicked.connect(self.on_category_select)
            self.cat_group.addButton(btn)
            cat_row.addWidget(btn)
            if first_btn is None:
                first_btn = btn

        # 메뉴 리스트 영역
        self.list_label = QLabel("카테고리를 선택하세요")
        self.list_label.setFont(styles.font(13))
        self.list_label.setWordWrap(True)
        self.list_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.list_label.setStyleSheet(f"color: {styles.TEXT}; background: transparent;")

        list_scroll = QScrollArea()
        list_scroll.setWidget(self.list_label)
        list_scroll.setWidgetResizable(True)
        list_scroll.setFrameShape(QFrame.Shape.NoFrame)
        list_scroll.setStyleSheet("background: transparent; border: none;")

        list_card = QFrame()
        list_card.setStyleSheet(f"""
            QFrame#listCard {{
                background-color: {styles.WHITE};
                border-radius: 16px;
                border: 1px solid {styles.BORDER};
            }}
            QLabel {{ border: none; background: transparent; }}
            QScrollArea {{ border: none; background: transparent; }}
        """)
        list_card.setObjectName("listCard")
        list_card_layout = QVBoxLayout()
        list_card_layout.setContentsMargins(20, 16, 20, 16)
        list_card_layout.addWidget(list_scroll)
        list_card.setLayout(list_card_layout)

        self.random_btn = QPushButton("이 카테고리에서 랜덤 추천")
        self.random_btn.setFixedSize(280, 52)
        self.random_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.random_btn.setStyleSheet(styles.PRIMARY_BTN)
        self.random_btn.setFont(styles.font(15))
        self.random_btn.setEnabled(False)
        self.random_btn.clicked.connect(self.on_random)

        center = QVBoxLayout()
        center.setSpacing(12)
        center.addWidget(title)
        center.addSpacing(8)
        center.addLayout(cat_row)
        center.addSpacing(4)
        center.addWidget(list_card)
        center.addSpacing(8)
        center.addWidget(self.random_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        outer.addLayout(top_row)
        outer.addSpacing(12)
        outer.addLayout(center)
        self.setLayout(outer)

        if first_btn:
            first_btn.setChecked(True)
            self.on_category_select()

    def on_category_select(self):
        btn = self.cat_group.checkedButton()
        if btn is None:
            return
        self.current_category = btn.property("value")
        self.current_menus = get_menus_by_category(self.current_category)
        lines = [format_menu_item(m) for m in self.current_menus]
        self.list_label.setText("\n".join(lines))
        self.random_btn.setEnabled(True)

    def on_random(self):
        self.go_result(self.current_menus, self.current_category)

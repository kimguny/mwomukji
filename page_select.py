# page_select.py
# 카테고리, 가격대, 맵기 조건을 선택하는 화면
# 조건을 모두 고른 뒤 추천받기 버튼을 누르면 필터링 후 결과 화면으로 이동한다
# 담당: 김태민

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QButtonGroup, QScrollArea, QFrame
)
from PyQt6.QtCore import Qt
from menu_data import load_menus, filter_menus
from random_recommend import pick_random
import styles

# 카테고리 선택지: (화면에 표시할 텍스트, 필터링에 사용할 실제 값) 쌍의 리스트
# 상관없음은 값이 None이므로 필터링 시 해당 조건을 건너뛴다
CATEGORIES = [
    ("한식", "한식"), ("중식", "중식"), ("일식", "일식"),
    ("양식", "양식"), ("분식", "분식"), ("치킨", "치킨"),
    ("피자", "피자"), ("패스트푸드", "패스트푸드"), ("상관없음", None),
]

# 가격대 선택지: (표시 텍스트, (최솟값, 최댓값)) 쌍의 리스트
PRICE_OPTIONS = [
    ("~1만원", (0, 10000)),
    ("1~2만원", (10000, 20000)),
    ("2만원 이상", (20000, 99999)),
    ("상관없음", None),
]

# 맵기 선택지: (표시 텍스트, 맵기 단계 상한값) 쌍의 리스트
# 선택한 단계 이하인 메뉴만 포함된다
SPICY_OPTIONS = [
    ("안매움", 1), ("약간", 2), ("보통", 3),
    ("매움", 4), ("아주매움", 5), ("상관없음", None),
]


def make_section_label(text):
    # 각 섹션(카테고리, 가격대, 맵기) 위에 표시되는 소제목 라벨을 만들어 반환한다
    label = QLabel(text)
    label.setStyleSheet(f"color: {styles.TEXT}; font-size: 14px; font-weight: bold;")
    return label


def make_toggle_group(options):
    # 선택지 목록을 받아 토글 버튼 그룹을 만들어 반환한다
    # QButtonGroup의 setExclusive(True)로 한 번에 하나만 선택되도록 설정한다
    # 각 버튼에는 setProperty("value", val)로 실제 필터링 값을 저장해둔다
    # 반환: (QButtonGroup 객체, QPushButton 리스트)
    group = QButtonGroup()
    group.setExclusive(True)
    buttons = []
    for label, val in options:
        btn = QPushButton(label)
        btn.setCheckable(True)           # 눌렀다 떼도 선택 상태가 유지되는 토글 버튼
        btn.setCursor(Qt.CursorShape.PointingHandCursor)
        btn.setStyleSheet(styles.TOGGLE_BTN)
        btn.setProperty("value", val)    # 버튼에 실제 값을 태그처럼 저장해둔다
        group.addButton(btn)
        buttons.append(btn)
    return group, buttons


class SelectPage(QWidget):
    # 조건 선택 화면 위젯
    # go_back   : 추천 방식 선택 화면으로 돌아가는 함수
    # go_result : 결과 화면으로 이동하는 함수 (필터링된 메뉴를 인자로 전달)

    def __init__(self, go_back, go_result):
        super().__init__()
        self.go_result = go_result
        self.setStyleSheet(styles.WINDOW)

        # 세 개의 토글 그룹 생성 (카테고리 / 가격 / 맵기)
        self.cat_group, cat_btns = make_toggle_group(CATEGORIES)
        self.price_group, price_btns = make_toggle_group(PRICE_OPTIONS)
        self.spicy_group, spicy_btns = make_toggle_group(SPICY_OPTIONS)

        # 스크롤 가능한 내부 콘텐츠 위젯
        content = QWidget()
        content.setStyleSheet(styles.WINDOW)
        content_layout = QVBoxLayout()
        content_layout.setSpacing(12)
        content_layout.setContentsMargins(30, 20, 30, 20)

        # 카테고리 섹션: 3열 그리드로 버튼 배치 (9개 = 3x3)
        content_layout.addWidget(make_section_label("카테고리"))
        cat_grid = QGridLayout()
        cat_grid.setSpacing(8)
        for i, btn in enumerate(cat_btns):
            cat_grid.addWidget(btn, i // 3, i % 3)  # 3개씩 한 줄에 배치
        content_layout.addLayout(cat_grid)

        # 가격대 섹션: 한 줄로 버튼 배치
        content_layout.addSpacing(8)
        content_layout.addWidget(self.make_divider())
        content_layout.addWidget(make_section_label("가격대"))
        price_row = QHBoxLayout()
        price_row.setSpacing(8)
        for btn in price_btns:
            price_row.addWidget(btn)
        content_layout.addLayout(price_row)

        # 맵기 섹션: 한 줄로 버튼 배치
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

        # 오류 메시지 라벨: 조건에 맞는 메뉴가 없을 때 표시 (평소에는 빈 문자열)
        self.error_label = QLabel("")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.error_label.setStyleSheet("color: #E53935; font-size: 13px;")
        content_layout.addWidget(self.error_label)

        # 추천받기 버튼: 클릭 시 on_recommend 호출
        recommend_btn = QPushButton("추천받기")
        recommend_btn.setFixedSize(220, 52)
        recommend_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        recommend_btn.setStyleSheet(styles.PRIMARY_BTN)
        recommend_btn.clicked.connect(self.on_recommend)
        content_layout.addWidget(recommend_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        content_layout.addSpacing(10)

        content.setLayout(content_layout)

        # QScrollArea로 감싸서 내용이 많아도 스크롤로 볼 수 있게 한다
        scroll = QScrollArea()
        scroll.setWidget(content)
        scroll.setWidgetResizable(True)       # 내용 위젯이 스크롤 영역 크기에 맞게 늘어남
        scroll.setFrameShape(QFrame.Shape.NoFrame)  # 스크롤 영역 테두리 제거
        scroll.setStyleSheet(styles.WINDOW)

        # 뒤로가기 버튼 (추천 방식 선택 화면으로 이동)
        back_btn = QPushButton("< 뒤로")
        back_btn.setFixedSize(80, 34)
        back_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        back_btn.setStyleSheet(styles.BACK_BTN)
        back_btn.clicked.connect(go_back)

        # 상단 행: 뒤로가기 버튼 왼쪽 배치
        top_row = QHBoxLayout()
        top_row.setContentsMargins(20, 20, 20, 0)
        top_row.addWidget(back_btn)
        top_row.addStretch()

        title = QLabel("조건을 선택하세요")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet(f"color: {styles.TEXT}; font-size: 22px; font-weight: bold;")

        # 전체 레이아웃: 뒤로가기 행 + 제목 + 스크롤 영역
        outer = QVBoxLayout()
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)
        outer.addLayout(top_row)
        outer.addWidget(title)
        outer.addWidget(scroll)
        self.setLayout(outer)

    def make_divider(self):
        # 섹션 사이에 표시하는 가로 구분선을 만들어 반환한다
        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setStyleSheet("color: #EEEEEE;")
        return line

    def on_recommend(self):
        # 추천받기 버튼 클릭 시 실행되는 메서드
        # 각 그룹에서 선택된 버튼의 값을 읽어 filter_menus에 전달하고,
        # 필터링 결과에서 랜덤으로 1개를 뽑아 결과 화면으로 이동한다

        def get_val(group):
            # 버튼 그룹에서 현재 선택된 버튼의 value 속성을 반환한다
            # 아무것도 선택되지 않은 경우 None 반환 (상관없음과 동일하게 처리)
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
            # 조건에 맞는 메뉴가 없으면 오류 메시지를 표시하고 화면을 유지한다
            self.error_label.setText("조건에 맞는 메뉴가 없어요. 조건을 바꿔보세요!")
        else:
            self.error_label.setText("")
            self.go_result(result)

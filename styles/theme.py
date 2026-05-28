BG = "#FFFDE7"       # 배경색: 연노랑 크림
TEXT = "#1A1A1A"     # 기본 텍스트: 진한 검정
SUBTEXT = "#555555"  # 보조 텍스트: 중간 회색

YELLOW = "#F5D800"
YELLOW_HOVER = "#E5C800"
YELLOW_PRESSED = "#CCB200"

WINDOW = f"background-color: {BG};"

# 주요 버튼 (노란 배경)
PRIMARY_BTN = f"""
    QPushButton {{
        background-color: {YELLOW};
        color: {TEXT};
        font-size: 15px;
        font-weight: bold;
        border-radius: 14px;
        border: none;
    }}
    QPushButton:hover {{ background-color: {YELLOW_HOVER}; }}
    QPushButton:pressed {{ background-color: {YELLOW_PRESSED}; }}
"""

# 외곽선 버튼 (투명 배경, 회색 테두리)
OUTLINE_BTN = f"""
    QPushButton {{
        background-color: transparent;
        color: {TEXT};
        font-size: 15px;
        border-radius: 14px;
        border: 1px solid #BBBBBB;
    }}
    QPushButton:hover {{ background-color: rgba(0,0,0,0.04); }}
    QPushButton:pressed {{ background-color: rgba(0,0,0,0.08); }}
"""

# 뒤로가기 버튼
BACK_BTN = """
    QPushButton {
        background-color: transparent;
        color: #999999;
        font-size: 13px;
        border: none;
        padding: 4px 8px;
        border-radius: 8px;
    }
    QPushButton:hover {
        background-color: rgba(0,0,0,0.05);
        color: #444444;
    }
"""

# 토글 버튼 (선택 안됨: 흰 배경 / 선택됨: 노란 배경)
TOGGLE_BTN = f"""
    QPushButton {{
        background-color: white;
        color: {TEXT};
        font-size: 13px;
        border-radius: 10px;
        border: 1px solid #E0E0E0;
        padding: 7px 14px;
    }}
    QPushButton:checked {{ background-color: {YELLOW}; border: none; }}
    QPushButton:hover:!checked {{ background-color: #F5F5F5; }}
"""

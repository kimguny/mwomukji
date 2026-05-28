# styles.py
# 앱 전체에서 공통으로 사용하는 색상 상수와 버튼 스타일시트를 모아둔 모듈
# 색상을 바꾸고 싶을 때 이 파일만 수정하면 전체에 적용된다

# 배경색: 연노랑 크림
BG = "#FFFDE7"

# 기본 텍스트 색상: 진한 검정
TEXT = "#1A1A1A"

# 보조 텍스트 색상: 중간 회색 (설명 문구, 카테고리 등에 사용)
SUBTEXT = "#555555"

# 포인트 컬러: 노랑 계열 (버튼 배경 등에 사용)
YELLOW = "#F5D800"
YELLOW_HOVER = "#E5C800"    # 마우스를 올렸을 때
YELLOW_PRESSED = "#CCB200"  # 클릭했을 때

# 창 전체 배경 스타일
WINDOW = f"background-color: {BG};"

# 주요 버튼 스타일 (노란 배경, 굵은 글씨)
# 추천받기, 다시 추천받기, 랜덤으로 추천받기 등에 사용
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

# 외곽선 버튼 스타일 (투명 배경, 회색 테두리)
# 직접 선택하기 버튼처럼 PRIMARY 버튼과 함께 쓸 때 사용
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

# 뒤로가기 버튼 스타일 (테두리 없음, 흐린 글씨)
# 각 페이지 상단 좌측에 배치되는 뒤로가기 버튼에 사용
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

# 토글 버튼 스타일 (조건 선택 화면의 카테고리, 가격, 맵기 버튼)
# 선택되지 않은 상태: 흰 배경 / 선택된 상태(:checked): 노란 배경
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

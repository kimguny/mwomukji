BG = "#FFFDE7"
TEXT = "#1A1A1A"
SUBTEXT = "#555555"
YELLOW = "#F5D800"
YELLOW_HOVER = "#E5C800"
YELLOW_PRESSED = "#CCB200"

WINDOW = f"background-color: {BG};"

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

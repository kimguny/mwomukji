import os
from PyQt6.QtGui import QFont, QFontDatabase

BG         = "white"
WHITE      = "#FFFFFF"
TEXT       = "#2D2B55"
SUBTEXT    = "#8B87B0"
ACCENT     = "#A78BFA"
ACCENT2    = "#7DD3FC"
PINK       = "#F9A8D4"
BORDER     = "#E5E0FF"
BG_START   = "#EDE9FF"

WINDOW = "background-color: white;"

PRIMARY_BTN = f"""
    QPushButton {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 {ACCENT}, stop:1 {ACCENT2});
        color: white;
        font-size: 15px;
        font-weight: bold;
        border-radius: 26px;
        border: none;
    }}
    QPushButton:hover {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #9B72F0, stop:1 #60C0F8);
    }}
    QPushButton:pressed {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #8B62E0, stop:1 #50B0E8);
    }}
"""

OUTLINE_BTN = f"""
    QPushButton {{
        background-color: white;
        color: {TEXT};
        font-size: 15px;
        border-radius: 26px;
        border: 1px solid {BORDER};
    }}
    QPushButton:hover {{ background-color: {BG_START}; }}
    QPushButton:pressed {{ background-color: {BORDER}; }}
"""

BACK_BTN = f"""
    QPushButton {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 {ACCENT}, stop:1 {ACCENT2});
        color: white;
        font-size: 13px;
        font-weight: bold;
        border: none;
        padding: 4px 12px;
        border-radius: 16px;
    }}
    QPushButton:hover {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 #9B72F0, stop:1 #60C0F8);
    }}
"""

TOGGLE_BTN = f"""
    QPushButton {{
        background-color: white;
        color: {TEXT};
        font-size: 13px;
        border-radius: 16px;
        border: 1px solid {BORDER};
        padding: 7px 14px;
    }}
    QPushButton:checked {{
        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop:0 {ACCENT}, stop:1 {ACCENT2});
        color: white;
        border: none;
    }}
    QPushButton:hover:!checked {{ background-color: {BG_START}; }}
"""

def load_fonts():
    base = os.path.join(os.path.dirname(os.path.dirname(__file__)), "fonts")
    QFontDatabase.addApplicationFont(os.path.join(base, "KERISKEDU_B.otf"))
    QFontDatabase.addApplicationFont(os.path.join(base, "KERISKEDU_R.otf"))
    QFontDatabase.addApplicationFont(os.path.join(base, "KERISKEDU_Line.otf"))

def font(size):
    return QFont("KERIS KEDU OTF", size)

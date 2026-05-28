import json


# menus.json을 읽어서 메뉴 목록(리스트)을 반환한다
def load_menus():
    with open("data/menus.json", "r", encoding="utf-8") as f:
        return json.load(f)

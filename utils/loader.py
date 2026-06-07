import json


# menus.json을 읽어서 메뉴 목록(리스트)을 반환한다
def load_menus():
    with open("data/menus.json", "r", encoding="utf-8") as f:
        return json.load(f)


# 전체 메뉴 개수를 반환한다
def get_menu_count():
    return len(load_menus())


# 전체 메뉴에서 카테고리 목록을 중복 없이 반환한다
def get_categories():
    menus = load_menus()
    return list(dict.fromkeys(m["category"] for m in menus))


# 특정 카테고리에 해당하는 메뉴만 반환한다
def get_menus_by_category(category):
    menus = load_menus()
    return [m for m in menus if m["category"] == category]

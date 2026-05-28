# menu_data.py
# 메뉴 데이터를 JSON 파일에서 불러오고, 조건에 따라 필터링하는 모듈

import json


# menus.json 파일을 읽어서 메뉴 목록(리스트)을 반환한다
# 파일은 항상 프로젝트 루트 폴더에 있어야 한다
def load_menus():
    with open("menus.json", "r", encoding="utf-8") as f:
        return json.load(f)


# 전체 메뉴 목록에서 조건에 맞는 메뉴만 걸러서 반환한다
# 조건이 None이면 해당 항목은 필터링하지 않는다 (상관없음 선택 시)
#
# 매개변수:
#   menus       - 전체 메뉴 리스트 (load_menus()의 반환값)
#   category    - 카테고리 문자열 (예: "한식", "치킨")
#   price_range - 가격 범위 튜플 (최솟값, 최댓값) (예: (0, 10000))
#   spicy_level - 맵기 단계 상한값 (1~5), 이 값 이하인 메뉴만 포함
def filter_menus(menus, category=None, price_range=None, spicy_level=None):
    result = menus

    # 카테고리 필터: 선택한 카테고리와 일치하는 메뉴만 남긴다
    if category:
        result = [m for m in result if m["category"] == category]

    # 가격 필터: 메뉴의 최소 가격이 선택한 범위 안에 있는 메뉴만 남긴다
    if price_range:
        min_p, max_p = price_range
        result = [m for m in result if m["price_min"] >= min_p and m["price_min"] <= max_p]

    # 맵기 필터: 선택한 맵기 단계 이하인 메뉴만 남긴다
    if spicy_level:
        result = [m for m in result if m["spicy_level"] <= spicy_level]

    return result

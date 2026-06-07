# 조건에 맞는 메뉴만 걸러서 반환한다. 조건이 None이면 해당 항목은 건너뛴다
# category: 카테고리 문자열 / price_range: (최솟값, 최댓값) 튜플 / spicy_level: 맵기 상한값
def filter_menus(menus, category=None, price_range=None, spicy_level=None):
    result = menus

    # 카테고리 필터
    if category:
        result = [m for m in result if m["category"] == category]

    # 가격 필터: 메뉴의 최소 가격이 선택한 범위 안에 있는 것만 남긴다
    if price_range:
        min_p, max_p = price_range
        result = [m for m in result if m["price_min"] >= min_p and m["price_min"] <= max_p]

    # 맵기 필터
    if spicy_level:
        result = [m for m in result if m["spicy_level"] <= spicy_level]

    return result


# 조건에 맞는 메뉴 개수를 반환한다
def count_filtered(menus, category=None, price_range=None, spicy_level=None):
    return len(filter_menus(menus, category, price_range, spicy_level))

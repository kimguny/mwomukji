def filter_menus(menus, category=None, price_range=None, spicy_level=None):
    result = menus

    # TODO: category가 None이 아닌 경우, result에서 category와 일치하는 메뉴만 남겨라
    #       각 메뉴 딕셔너리에는 "category" 키가 있다
    #       힌트: result = [m for m in result if 조건]



    # TODO: price_range가 None이 아닌 경우, 가격 범위에 맞는 메뉴만 남겨라
    #       price_range는 (최솟값, 최댓값) 튜플이다 → min_p, max_p = price_range
    #       각 메뉴에는 "price_min" 키가 있다



    # TODO: spicy_level이 None이 아닌 경우, spicy_level 이하인 메뉴만 남겨라
    #       각 메뉴에는 "spicy_level" 키가 있다



    return result

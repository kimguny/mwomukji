# 맵기 단계(1~5)를 별 기호 문자열로 변환한다. 예: 3 -> "★★★☆☆"
def spicy_stars(level):
    return "★" * level + "☆" * (5 - level)


# 가격 최솟값과 최댓값을 "X,XXX원 ~ X,XXX원" 형식으로 변환한다
def format_price(price_min, price_max):
    return f"{price_min:,}원 ~ {price_max:,}원"

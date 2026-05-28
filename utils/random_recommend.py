# random_recommend.py
# 필터링된 메뉴 목록에서 랜덤으로 1개를 뽑는 모듈

import random


# 메뉴 리스트에서 무작위로 1개를 골라 반환한다
# 리스트가 비어있으면 None을 반환한다 (조건에 맞는 메뉴가 없는 경우)
def pick_random(menus):
    if not menus:
        return None
    return random.choice(menus)

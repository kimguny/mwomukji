import random


# 메뉴 리스트에서 무작위로 1개를 반환한다. 비어있으면 None을 반환한다
def pick_random(menus):
    if not menus:
        return None
    return random.choice(menus)


# 메뉴 리스트에서 무작위로 1개를 뽑아 반환하고, 원본 리스트에서 제거한다
# 중복 없이 순차적으로 추천할 때 사용한다
def pick_and_remove(menus):
    if not menus:
        return None
    menu = random.choice(menus)
    menus.remove(menu)
    return menu

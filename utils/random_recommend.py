import random


# 메뉴 리스트에서 무작위로 1개를 반환한다. 비어있으면 None을 반환한다
def pick_random(menus):
    if not menus:
        return None
    return random.choice(menus)


# 메뉴 리스트에서 특정 메뉴를 제거한다
def remove_menu(menus, menu):
    menus.remove(menu)


# 메뉴 리스트가 비어있는지 확인한다
def is_empty(menus):
    return len(menus) == 0


# 메뉴 리스트에서 무작위로 n개를 뽑아 반환한다. 리스트보다 n이 크면 전체를 반환한다
def pick_multiple(menus, n):
    return random.sample(menus, min(n, len(menus)))

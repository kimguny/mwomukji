import random


def pick_random(menus):
    if not menus:
        return None
    return random.choice(menus)

import json


def load_menus():
    with open("menus.json", "r", encoding="utf-8") as f:
        return json.load(f)


def filter_menus(menus, category=None, price_range=None, spicy_level=None):
    result = menus

    if category:
        result = [m for m in result if m["category"] == category]

    if price_range:
        min_p, max_p = price_range
        result = [m for m in result if m["price_min"] >= min_p and m["price_min"] <= max_p]

    if spicy_level:
        result = [m for m in result if m["spicy_level"] <= spicy_level]

    return result

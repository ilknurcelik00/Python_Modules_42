
def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    x = seed_type.capitalize()
    y = seed_type.capitalize()
    z = seed_type.capitalize()
    if unit == 'packets':
        print(x, "seeds:", quantity, unit, "available")
    elif unit == 'grams':
        print(y, "seeds:", quantity, unit, "total")
    elif unit == 'area':
        print(z, "seeds: covers", quantity, "square meters")
    else:
        print("Unknown unit type")

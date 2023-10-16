from gun_values import gun_stats

def get_name(gun: list) -> str:
    return gun[0]

def get_rarity(gun: list) -> str:
    return gun[1]

def get_dps(gun: list) -> float:
    return gun[2]

def get_damage(gun: list) -> int:
    return gun[3]

def get_structdmg(gun: list) -> int:
    return gun[4]

def get_firerate(gun: list) -> float:
    return gun[5]

def get_magsize(gun: list) -> int:
    return gun[6]

def get_reload(gun: list) -> float:
    return[7]

def raritytogun(gun: list, rarity: str) -> list:
    results = []
    for guns in gun:
        if get_rarity(gun) == rarity:
            results.append(guns)
    return results

def mostDmg(gun: list) -> list:
    result = []
    for index, guns in enumerate(gun):
        if index < len(gun) - 1:
            if get_damage(guns) > get_damage(gun[index + 1]):
                result = guns
    return result

def leastDmg(gun: list) -> list:
    result = []
    for index, guns in enumerate(gun):
        if index < len(gun) - 1:
            if get_damage(guns) < get_damage(gun[index + 1]):
                result = guns
    return result
            

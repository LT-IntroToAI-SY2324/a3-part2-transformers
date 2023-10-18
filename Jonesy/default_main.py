def firerate_to_name(matches: List[str]) -> List[str]:
    """returns the firerate of the gun named,
    """
    result = []
    for gun_stats in gun_values:
        if matches[0] == get_name(gun_stats):
            result.append(get_name(gun_stats) + "has a firerate of" )
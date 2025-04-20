def city_country(city, country, population=''):
    """返回固定格式"""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"

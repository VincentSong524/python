def city_country(city, country):
    """接受城市名称及所属国家，按格式返回"""
    return f"{city}, {country}"

while True:
    print("\nPlease enter city and country:")
    print("(enter 'q' at any time to quit)")
    
    city_name = input("city:")
    if city_name == 'q':
        break
    
    country_name = input("country:")
    if country_name == 'q':
        break
    
    print(city_country(city_name, country_name))
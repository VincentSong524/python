def desribe_city(city, country='China'):
    """接受一座城市的名字以及该城市所属的国家，返回城市描述"""
    print(f"{city.title()} is in {country.title()}.")

if __name__ == '__main__':
    desribe_city('Beijing')
    desribe_city(city='Shanghai')
    desribe_city(city='New Yok', country='Paris')

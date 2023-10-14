def make_car(manufacturer, model, **kwargs):
    """将一辆汽车的信息存储在字典中"""
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model
    return kwargs


car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
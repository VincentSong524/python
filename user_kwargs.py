def test_fuc(name, **kwargs):
    """将传入的参数导入字典kwargs"""
    kwargs['name'] = name
    return kwargs

kwargs = test_fuc('vincent', sex='man', age='23')
print(kwargs)
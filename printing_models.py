from printing_functions import print_models, show_completed_models

#首先创建一个列表，其中包含一些要打印的设计。
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs[:], completed_models)#使用列表切片方式阻止函数修改列表
show_completed_models(completed_models)

#试一下打印函数文档
print(show_completed_models.__doc__)
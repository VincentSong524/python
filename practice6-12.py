cities = {
    'BeiJing': {
        'country': 'China',
        'population': 21450000,
        'fact': '天坛始建于明永乐十八年（1420），明清两代帝王在此祭天、祈谷和祈雨。'
            '天坛的传说因天坛建筑和皇帝祭天大典而萌生和发展。“天人合一”宇宙观的融入，'
            '使天坛建筑群具有神圣而独特的寓意，成为相关传说发生和繁盛的重要驱动因素。'
        },
    'NewYork': {
        'country': 'USA',
        'population': 8468000,
        'fact': '现代纽约地区原居住着莱纳佩人原住民，传统语言使用阿尔冈昆语族的一支：'
        'Unami 语。 另在东长岛的原住民住属于莫西干人及佩科特人，在文化、语言上，'
        '与新英格兰地区的原住民比较有相关。'
        },
    'Paris': {
        'country': 'France',
        'population': 2161000,
        'fact': '巴黎（法语：Paris，法语发音：[paʁi] （ⓘ））是法国的首都及最大都市，'
        '同时是法兰西岛大区首府，为法国的政治与文化中心，隶属法兰西岛大区之下的巴黎省'
        '（编号第75省；范围重叠）。目前的巴黎市辖区范围大致为旧巴黎城墙内（环城大道内侧），'
        '依照发展历史共分成20个区，自从1860年代开始就没有重大变化。截至2019年为止，'
        '巴黎市内人口超过216万[4]，巴黎都会区的人口则逾1,300万[3]，是欧洲最大的都会区之一[5]。'
        },
}

for name, info in cities.items():
    print(f"{name}")
    for key, value in info.items():
        print(f"{key}: {value}")
    print()
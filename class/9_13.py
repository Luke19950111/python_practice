# xx_n = {
#     'list': 'list is list',
#     'class': 'class is class',
#     'dic': 'dic is dic',
#     'model': 'model is model',
#     'import': 'import is import',
#     }
# xx_n['xx_6'] = 'xxxxx6'
# xx_n['xx_7'] = 'xxxxx7'
# xx_n['xx_8'] = 'xxxxx8'
# xx_n['xx_9'] = 'xxxxx9'
# xx_n['xx_10'] = 'xxxxx10'
#
# for k, v in xx_n.items():
#     print('\n' + k)
#     print('\t' + v)

from collections import OrderedDict

xx_nn = OrderedDict()
xx_nn['xx_6'] = 'xxxxx6'
xx_nn['xx_7'] = 'xxxxx7'
xx_nn['xx_8'] = 'xxxxx8'
xx_nn['xx_9'] = 'xxxxx9'
xx_nn['xx_10'] = 'xxxxx10'

for k, v in xx_nn.items():
    print(k + ': ' + v)
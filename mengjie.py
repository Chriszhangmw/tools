#
# import pandas as pd
#
# # data = pd.read_excel('./jibin.xlsx',index_col=0)
# # print(data.to_csv('data.csv'))
#
# df = pd.read_csv('./data.csv')
# data_list = df["疾病名称"].array
# # print(data_list[0])
#
# data = pd.read_csv("./data2.csv")
# # print(data)
#
# def extract(x):
#     res = []
#     x = str(x)
#     for disease_name in data_list:
#         if disease_name in x:
#             res.append(disease_name)
#     res = ' '.join(res)
#     return res
#
#
# data["伴随症状"] = data["伴随症状"].apply(lambda x :extract(x))
#
# print(data)
#
#
#









import pandas as pd

server = pd.read_csv('./data.csv')
datacenter = pd.read_csv('./data2.csv')

# print(server)

print(server[server["datacenter"] == 10].empty)

# print(server[server["ip"]=="11.12.11.13"]["name"].values[0])
k = datacenter[datacenter["name"] == "chengdu"]["id"].values[0]
res = server[server["datacenter"]==k].values.tolist()
# print(res)
# print(str(res))



import numpy as np
import pandas as pd
import tabulatehelper as th
from markdownify import markdownify as md
# df = pd.DataFrame(np.random.random(16).reshape(4, 4), columns=('a', 'b', 'c', 'd'))
# # print(df.to_html)
# print(th.md_table(df, formats={-1: 'c'}))
# df = pd.DataFrame({
#     "weekday": ["monday", "thursday", "wednesday"],
#     "temperature": [20, 30, 25],
#     "precipitation": [100, 200, 150],
# }).set_index("weekday")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import six
import random
import string

#
# def render_mpl_table(data, col_width=3.0, row_height=0.625, font_size=14,
#         header_color='#40466e', row_colors=['#f1f1f2', 'w'], edge_color='w',
#         bbox=[0, 0, 1, 1], header_columns=0,
#         ax=None, **kwargs):
#
#     if ax is None:
#         size = (np.array(data.shape[::-1]) + np.array([0, 1])) * np.array([col_width, row_height])
#         fig, ax = plt.subplots(figsize=size)
#         ax.axis('off')
#
#     mpl_table = ax.table(cellText=data.values, bbox=bbox, colLabels=data.columns, **kwargs)
#
#     mpl_table.auto_set_font_size(False)
#     mpl_table.set_fontsize(font_size)
#
#     for k, cell in six.iteritems(mpl_table._cells):
#          cell.set_edgecolor(edge_color)
#          if k[0] == 0 or k[1] < header_columns:
#               cell.set_text_props(weight='bold', color='w')
#               cell.set_facecolor(header_color)
#          else:
#               cell.set_facecolor(row_colors[k[0]%len(row_colors) ])
#
#     return ax
#
#
# df = pd.read_csv('./data.csv')
#
# ax = render_mpl_table(df, header_columns=0, col_width=2.0)
# fig = ax.get_figure()
#
# temp = random.sample('1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()',5)
# temp = ''.join(temp)
# img_path = './' + temp + '.png'
# fig.savefig(img_path)
#
#
# print(pd.DataFrame())

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

f = open('test_data.json', encoding="UTF-8")
res = f.read()
data = json.loads(res)

df = pd.DataFrame(columns=['student_id', 'total', 'linear_table', 'tree', 'search', 'array', 'figure_operation', 'order', 'string', 'map_structure'])
ts_zh = ['线性表', '树结构', '查找算法', '数组', '数字操作', '排序算法', '字符串', '图结构']
ts_en = ['linear_table', 'tree', 'search', 'array', 'figure_operation', 'order', 'string', 'map_structure']

for (i, value) in enumerate(data.values()):
    user_id = value['user_id']
    cases = value['cases']
    final_scores = []
    type_scores = [[], [], [], [], [], [], [], []]
    for case in cases:
        final_scores.append(case['final_score'])
        for (_, t) in enumerate(ts_zh):
            if case['case_type'] == t:
                type_scores[_].append(case['final_score'])

    mean_final_score = np.mean(final_scores)

    mean_linear_table_score = np.mean(type_scores[0])
    mean_tree_score = np.mean(type_scores[1])
    mean_search_score = np.mean(type_scores[2])
    mean_array_score = np.mean(type_scores[3])
    mean_figure_operation_score = np.mean(type_scores[4])
    mean_order_score = np.mean(type_scores[5])
    mean_string_score = np.mean(type_scores[6])
    mean_map_structure_score = np.mean(type_scores[7])

    item = pd.DataFrame({'student_id': user_id,
                         'total': mean_final_score,
                         'linear_table': mean_linear_table_score,
                         'tree': mean_tree_score,
                         'search': mean_search_score,
                         'array': mean_array_score,
                         'figure_operation': mean_figure_operation_score,
                         'order': mean_order_score,
                         'string': mean_string_score,
                         'map_structure': mean_map_structure_score}
                        , index=[i])
    df = df.append(item)

plt.figure()
ax = plt.subplot(111)
ax = sns.distplot(df['total'])
plt.savefig('./总分分布.png')

for i in range(len(ts_en)):
    name = ts_en[i]
    plt.figure()
    ax = plt.subplot(111)
    ax = sns.distplot(df[name])
    plt.savefig('./' + ts_zh[i] + '分布.png')

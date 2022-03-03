from math import sqrt
from excel import *


# 距离计算函数


def distance(arg1, arg2):
    return sqrt(pow(arg1[0] - arg2[0], 2) + pow(arg1[1] - arg2[1], 2))


# 求斜率
def k_calculation(arg1, arg2):
    return (arg1[1] - arg2[1]) / (arg1[0] - arg2[0])


# 斜率规则判断函数
def k_judge(arg1):
    length = len(arg1)
    points = [arg1[0], arg1[int((length - 1) / 4)], arg1[int((length - 1) / 2)], arg1[int(3 * (length - 1) / 4)],
              arg1[length - 1]]
    if k_calculation(points[0], points[2]) < 0 and \
            k_calculation(points[2], points[4]) > 0:
        return True
    else:
        return False


# 获取数据
point_list = []
for i in range(2, rows + 1):
    point_list.append((table.cell(row=i, column=1).value, table.cell(row=i, column=2).value))

# 滑动窗口大小
window = 8

# 聚类距离阈值   最低数量阈值
r_max = 0.8

num_min = 5

# 多个目标聚类
i = 0
while i < len(point_list) - window + 1:
    prev = point_list[i]
    currect_point_list = [point_list[i]]
    for j in range(i + 1, i + window):
        dis = distance(prev, point_list[j])
        if dis <= r_max:
            currect_point_list.append(point_list[j])
            # 重置
            prev = point_list[j]
            r_max = 0.8
        else:
            # 跨越点阈值增加
            r_max += 0.02
    if len(currect_point_list) >= num_min and k_judge(currect_point_list):
        print(currect_point_list)
        for t in range(0, len(currect_point_list)):
            i += 1
    else:
        i += 1

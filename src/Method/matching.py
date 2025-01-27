# -*- coding: utf-8 -*-
"""
-------------------------------------------------
    @Project -> File   :lidarScan -> matching
    @IDE    :PyCharm
    @Author :Mr. LU
    @Date   :2022-03-03 15:48
    @Desc   :拟合与特征提取
            负责计算动态窗口聚类objectQueue点集的拟合度(R_Squared)
            返回符合条件的特征点T 维护队列keyPoints
-------------------------------------------------
   Change Activity:
                   2022-03-03 15:48:
-------------------------------------------------
"""
__author__ = 'bobi'

import threading
from src.Object import *


class matching:
    """聚类对象拟合与特征提取"""

    def __init__(self, objectQueue, flag, keyPoints):
        # object点集
        self.objectQueue = objectQueue
        self.flag = flag
        # 特征点集
        self.keyPoints = keyPoints
        threading.Thread(target=self.match, )

    # 拟合线程
    def match(self):
        while self.flag:
            if not self.objectQueue.empty():
                pass
                # 从objectQueue队列中去已经聚类好的object
                # object类型为元组
                # object = self.objectQueue.get(block=True, timeout=1)

                # todo 计算object中点集的拟合系数

                # todo 特征提取 输出特征点T
                # 构造特征点对象
                # keyPoint(position=?)

                # todo 存入keyPoints队列后续处理
                # self.keyPoints.put(item=keyPoint, block=True, timeout=1)

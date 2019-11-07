# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:28:32 2019
创建沿每个维度的数据分布的直方图
一维{ 1, 3, 2, 1, 3, 2, 75, 1, 3, 2, 2, 1, 2, 3, 2, 1 }
一维{ 1, 2, 3, 4, 2, 19, 9, 21, 20, 22 }
二维{(1, 9), (2, 9), (3, 9), (10, 10), (10, 3), (9, 1), (10, 2)}
@author: Kylin
"""
import numpy as np
import matplotlib.pyplot as plt

#1. 先绘制二维的数据
x1 = np.array([1,2,3,10,10,9,10])
y1 = np.array([9,9,9,10,3,1,2])
plt.figure("2 dimension plots figure")
plt.scatter(x1, y1)
plt.xlabel("Dimension1")
plt.ylabel("Dimension2")
plt.title("two dimension plots figure")

#2. 利用直方图绘制一维数据
x2 = np.array([1, 3, 2, 1, 3, 2, 75, 1, 3, 2, 2, 1, 2, 3, 2, 1])
x3 = np.array([1, 2, 3, 4, 2, 19, 9, 21, 20, 22])
x2max = max(x2)
x3max = max(x3)
plt.figure("one dimension histgrams")
plt.hist(x2, x2max, normed=0, color="blue", alpha=0.8)
plt.hist(x3, x3max, normed=0, color="red", alpha=0.8)
plt.title("one dimension plots figure")

#3.这里对于x3不易发现其异常值，因为直方图是按照其出现的个数绘制的，如果把它作为时序图会怎么样？
t = np.arange(len(x3))
plt.figure("time series figure for x3")
plt.plot(t, x3)
plt.xlabel("t")
plt.ylabel("value")
plt.title("Time series figure")



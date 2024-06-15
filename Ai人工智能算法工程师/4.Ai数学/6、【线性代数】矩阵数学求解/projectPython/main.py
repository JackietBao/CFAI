import numpy as np

# 系数矩阵
A = np.array([[1, 2, 3],
              [1, 6, 7],
              [1, 10, 6]])

# 常数向量
b = np.array([5, 9, 8])

# 使用 numpy.linalg.solve 解方程
x = np.linalg.solve(A, b)

print("解：", x)

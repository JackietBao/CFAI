import numpy as np

# 生成两组随机数据
data1 = np.random.randn(1000)
data2 = np.random.randn(1000)

# 计算期望（平均值）
expectation1 = np.mean(data1)
expectation2 = np.mean(data2)

# 计算方差
variance1 = np.var(data1)
variance2 = np.var(data2)

# 计算协方差矩阵（注意：协方差是两个变量间的关系度量）
covariance_matrix = np.cov(data1, data2)

print(f"期望值 Data1: {expectation1}, Data2: {expectation2}")
print(f"方差 Data1: {variance1}, Data2: {variance2}")
print(f"协方差矩阵:\n{covariance_matrix}")

# 从协方差矩阵中提取data1和data2的协方差
covariance = covariance_matrix[0, 1]
print(f"Data1 和 Data2 的协方差: {covariance}")


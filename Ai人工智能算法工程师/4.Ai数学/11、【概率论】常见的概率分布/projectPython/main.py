import numpy as np
import matplotlib.pyplot as plt

# 设定随机种子，以便于结果的复现
np.random.seed(0)

# 伯努利分布（参数p为成功概率）
p = 0.5
bernoulli_dist = np.random.binomial(1, p, 1000)

# 二项分布（参数n为试验次数，p为每次成功概率）
n = 10
binomial_dist = np.random.binomial(n, p, 1000)

# 正态分布（参数mu为均值，sigma为标准差）
mu, sigma = 0, 0.1
normal_dist = np.random.normal(mu, sigma, 1000)

# 指数分布（参数lambda为率参数，其倒数为平均间隔时间）
lambd = 1.0
exponential_dist = np.random.exponential(1/lambd, 1000)

# Logistic分布（参数mu为位置参数，s为尺度参数）
mu, s = 0, 1
logistic_dist = np.random.logistic(mu, s, 1000)

# 绘制柱状图
fig, axs = plt.subplots(5, 1, figsize=(5, 8))

# 伯努利分布柱状图
axs[0].hist(bernoulli_dist, bins=2)
axs[0].set_title('Bernoulli Distribution')

# 二项分布柱状图
axs[1].hist(binomial_dist, bins=range(n+2))
axs[1].set_title('Binomial Distribution')

# 正态分布柱状图
axs[2].hist(normal_dist, bins=30)
axs[2].set_title('Normal Distribution')

# 指数分布柱状图
axs[3].hist(exponential_dist, bins=30)
axs[3].set_title('Exponential Distribution')

# Logistic分布柱状图
axs[4].hist(logistic_dist, bins=30)
axs[4].set_title('Logistic Distribution')

plt.tight_layout()
plt.show()

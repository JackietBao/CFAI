import random
import matplotlib.pyplot as plt

# 模拟掷硬币函数，'H'代表正面，'T'代表反面
def toss_coin():
    return 'H' if random.random() < 0.5 else 'T'

# 进行N次掷硬币实验
N = 1000
results = [toss_coin() for _ in range(N)]

print(results)


# 计算正面和反面的频率
heads = results.count('H')
tails = results.count('T')

# 概率质量函数的值
pmf = [heads/N, tails/N]

# 绘制概率质量函数
labels = ['Heads', 'Tails']
plt.bar(labels, pmf, color=['blue', 'orange'])
plt.title('Probability Mass Function of Coin Toss')
plt.ylabel('Probability')
plt.show()


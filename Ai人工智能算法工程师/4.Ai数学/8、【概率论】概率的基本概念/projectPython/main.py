import random

# 模拟掷硬币函数，'H'表示正面，'T'表示反面
def toss_coin():
    return 'H' if random.random() < 0.5 else 'T'

# 进行N次掷硬币试验
N = 10
results = [toss_coin() for _ in range(N)]

# 打印结果
print(results)


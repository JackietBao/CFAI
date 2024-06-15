"""
import numpy as np
import matplotlib.pyplot as plt


def gamble_game(trials):
    # 抛硬币游戏，正面为1，反面为-1
    results = np.random.choice([1, -1], size=trials)
    return results


def simulate_gambling(trials):
    results = gamble_game(trials)

    # 计算累积盈亏
    cumulative_sum = np.cumsum(results)

    # 计算平均盈亏
    average_win_loss = cumulative_sum / np.arange(1, trials + 1)

    return cumulative_sum, average_win_loss


def plot_results(trials):
    cumulative_sum, average_win_loss = simulate_gambling(trials)

    # 绘制累积盈亏图
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(cumulative_sum)
    plt.title('Cumulative Win/Loss Over Trials')
    plt.xlabel('Trials')
    plt.ylabel('Cumulative Sum')

    # 绘制平均盈亏图
    plt.subplot(1, 2, 2)
    plt.plot(average_win_loss)
    plt.axhline(y=0, color='r', linestyle='-')  # 期望值线
    plt.title('Average Win/Loss Over Trials')
    plt.xlabel('Trials')
    plt.ylabel('Average Win/Loss')

    plt.tight_layout()
    plt.show()


# 模拟10000次游戏
plot_results(10000)


"""



import numpy as np
import matplotlib.pyplot as plt

def roll_dice():
    """模拟掷一个六面骰子"""
    return np.random.randint(1, 7)

def experiment(num_rolls):
    """进行一次实验，实验包括num_rolls次掷骰子"""
    total = 0
    for _ in range(num_rolls):
        total += roll_dice()
    return total / num_rolls

def run_experiments(num_experiments, num_rolls):
    """运行多次实验，并记录每次实验的平均值"""
    averages = []
    for _ in range(num_experiments):
        averages.append(experiment(num_rolls))
    return averages

def plot_histogram(averages):
    """绘制实验平均值的直方图"""
    plt.hist(averages, bins=20, edgecolor='black', density=True)
    plt.xlabel('Average of Rolls')
    plt.ylabel('Frequency')
    plt.title('Central Limit Theorem Demonstration')
    plt.show()

# 参数设置
num_experiments = 10000  # 实验次数
num_rolls = 30          # 每次实验掷骰子的次数

# 运行实验并绘图
averages = run_experiments(num_experiments, num_rolls)
plot_histogram(averages)


















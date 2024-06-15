"""
import numpy as np
import matplotlib.pyplot as plt

# 定义激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return np.tanh(x)

def relu(x):
    return np.maximum(0, x)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, x * alpha)

def parametric_relu(x, alpha=0.01):
    return np.where(x > 0, x, x * alpha)

def elu(x, alpha=1):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

# 绘制函数图像的通用函数
def plot_activation_function(func, x, title):
    y = func(x)
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel('Input value (x)')
    plt.ylabel('Output value (f(x))')
    plt.grid(True)
    plt.show()

# 创建一个x值的数组，范围从-10到10，这里0.1为步长
x_values = np.arange(-10, 10, 0.1)

# 绘制每个激活函数
plot_activation_function(sigmoid, x_values, 'Sigmoid Activation Function')
plot_activation_function(tanh, x_values, 'Tanh Activation Function')
plot_activation_function(relu, x_values, 'ReLU Activation Function')
plot_activation_function(leaky_relu, x_values, 'Leaky ReLU Activation Function')
plot_activation_function(parametric_relu, x_values, 'Parametric ReLU Activation Function')
plot_activation_function(elu, x_values, 'ELU Activation Function')

# Softmax 函数通常应用于多分类问题中输出层的一组值上，
# 由于它将输出转换为概率分布，因此单独的x值没有太多意义。
# 我们可以对一组随机值应用softmax来展示它的效果。
softmax_values = np.random.randn(10)  # 创建一组随机值
plt.figure()
plt.bar(range(len(softmax_values)), softmax(softmax_values))
plt.title('Softmax Activation Function')
plt.xlabel('Index of e^x')
plt.ylabel('Probability')
plt.show()






import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def f(x):
    return x ** 2

# 导数（梯度）
def df(x):
    return 2 * x

# 绘制原始函数
x = np.linspace(-3, 3, 100)
y = f(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = x^2")

# 在 x = 1 处的梯度和切线
x1 = 1
y1 = f(x1)
slope = df(x1)

# 切线方程: y = m(x - x1) + y1
def tangent_line(x, x1, y1, slope):
    return slope * (x - x1) + y1

# 在切点附近绘制切线
x_tangent = np.linspace(x1 - 1, x1 + 1, 10)  # 切线的x坐标范围
y_tangent = tangent_line(x_tangent, x1, y1, slope)

plt.plot(x_tangent, y_tangent, label="Tangent at x = 1", color='red')
plt.scatter([x1], [y1], color='black')  # 切点

# 设置图形
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function and Tangent Line at a Point')
plt.grid(True)
plt.show()
















"""


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 创建x，y的数据点
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y) # 生成网格点坐标矩阵

# 定义三维函数
def f(x, y):
    return x**2 + y**2

# 计算z的值
z = f(x, y)

# 创建图形和轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制表面
surf = ax.plot_surface(x, y, z, cmap='viridis', alpha=0.5)

# 定义要突出显示的点
point_x, point_y = 1.0, 1.0  # 可以根据需要修改这些值
point_z = f(point_x, point_y)

# 绘制该点
ax.scatter(point_x, point_y, point_z, color='red', s=50)  # s是点的大小

# 计算切平面的法线
normal = np.array([2 * point_x, 2 * point_y, -1])

# 定义平面上的点(x_plane, y_plane, z_plane)
x_plane = np.linspace(-5, 5, 10)
y_plane = np.linspace(-5, 5, 10)
x_plane, y_plane = np.meshgrid(x_plane, y_plane)
z_plane = (-normal[0] * (x_plane - point_x) - normal[1] * (y_plane - point_y)) / normal[2] + point_z

# 绘制切平面
ax.plot_surface(x_plane, y_plane, z_plane, color='yellow', alpha=0.5)

# 设置标签和标题
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Surface Plot with Tangent Plane')

# 显示图形
plt.show()






































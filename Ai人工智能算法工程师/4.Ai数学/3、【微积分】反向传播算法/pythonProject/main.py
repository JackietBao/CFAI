"""
# 定义输入值和期望输出
x_1 = 40.0
x_2 = 80.0
expected_output = 60.0

'''
初始化
'''
# 定义权重
w_1_11 = 0.5
w_1_12 = 0.5
w_1_13 = 0.5
w_1_21 = 0.5
w_1_22 = 0.5
w_1_23 = 0.5

w_2_11 = 1.0
w_2_21 = 1.0
w_2_31 = 1.0


'''前向传播
'''
z_1 = x_1 * w_1_11 + x_2 * w_1_21
z_2 = x_1 * w_1_12 + x_2 * w_1_22
z_3 = x_1 * w_1_13 + x_2 * w_1_23
y_pred = z_1 * w_2_11 + z_2 * w_2_21 + z_3 * w_2_31

# print(z_1, z_2, z_3, y_pred)
print("前向传播预测值为： ", y_pred)

# 计算损失函数值（L2损失）
loss = 0.5 * (expected_output - y_pred) ** 2
print("当前的loss值为：",loss)

'''
开始计算梯度
'''

# 计算输出层关于损失函数的梯度
d_loss_predicted_output = -(expected_output - y_pred)
# print(d_loss_predicted_output)
#
# 计算权重关于损失函数的梯度
d_loss_w_2_11 = d_loss_predicted_output * z_1
d_loss_w_2_21 = d_loss_predicted_output * z_2
d_loss_w_2_31 = d_loss_predicted_output * z_3
# print(d_loss_w_2_11,d_loss_w_2_21,d_loss_w_2_31)


d_loss_w_1_11 = d_loss_predicted_output * w_2_11 * x_1
# print(d_loss_w_1_11)
d_loss_w_1_21 = d_loss_predicted_output * w_2_11 * x_2
# print(d_loss_w_1_21)
d_loss_w_1_12 = d_loss_predicted_output * w_2_21 * x_1
# print(d_loss_w_1_12)
d_loss_w_1_22 = d_loss_predicted_output * w_2_21 * x_2
# print(d_loss_w_1_22)
d_loss_w_1_13 = d_loss_predicted_output * w_2_31 * x_1
# print(d_loss_w_1_13)
d_loss_w_1_23 = d_loss_predicted_output * w_2_31 * x_2
# print(d_loss_w_1_23)



# 使用梯度下降法更新权重
learning_rate = 1e-5
w_2_11 -= learning_rate * d_loss_w_2_11
w_2_21 -= learning_rate * d_loss_w_2_21
w_2_31 -= learning_rate * d_loss_w_2_31

w_1_11 -= learning_rate * d_loss_w_1_11
w_1_12 -= learning_rate * d_loss_w_1_12
w_1_13 -= learning_rate * d_loss_w_1_13
w_1_21 -= learning_rate * d_loss_w_1_21
w_1_22 -= learning_rate * d_loss_w_1_22
w_1_23 -= learning_rate * d_loss_w_1_23

'''前向传播
'''


z_1 = x_1 * w_1_11 + x_2 * w_1_21
z_2 = x_1 * w_1_12 + x_2 * w_1_22
z_3 = x_1 * w_1_13 + x_2 * w_1_23

y_pred = z_1 * w_2_11 + z_2 * w_2_21 + z_3 * w_2_31
print("Final: ",y_pred)

# print("前向传播预测值为： ", y_pred)
loss = 0.5 * (expected_output - y_pred) ** 2
print("当前的loss值为：",loss)







def forward_propagation(layer_1_list, layer_2_list):
    w_1_11, w_1_12, w_1_13, w_1_21, w_1_22, w_1_23 = layer_1_list
    w_2_11, w_2_21, w_2_31 = layer_2_list
    z_1 = x_1 * w_1_11 + x_2 * w_1_21
    z_2 = x_1 * w_1_12 + x_2 * w_1_22
    z_3 = x_1 * w_1_13 + x_2 * w_1_23
    y_pred = z_1 * w_2_11 + z_2 * w_2_21 + z_3 * w_2_31
    return y_pred


def compute_loss(y_true, y_pred):
    loss = 0.5 * (y_true - y_pred) ** 2
    return loss

def backward_propagation(layer_1_list,layer_2_list,learning_rate):

    w_1_11, w_1_12, w_1_13, w_1_21, w_1_22, w_1_23 = layer_1_list
    w_2_11, w_2_21, w_2_31 = layer_2_list
    z_1 = x_1 * w_1_11 + x_2 * w_1_21
    z_2 = x_1 * w_1_12 + x_2 * w_1_22
    z_3 = x_1 * w_1_13 + x_2 * w_1_23

    # 计算输出层关于损失函数的梯度
    d_loss_predicted_output = -(y_true - y_pred)

    # 计算权重关于损失函数的梯度
    d_loss_w_2_11 = d_loss_predicted_output * z_1
    d_loss_w_2_21 = d_loss_predicted_output * z_2
    d_loss_w_2_31 = d_loss_predicted_output * z_3

    d_loss_w_1_11 = d_loss_predicted_output * w_2_11 * x_1
    d_loss_w_1_21 = d_loss_predicted_output * w_2_11 * x_2
    d_loss_w_1_12 = d_loss_predicted_output * w_2_21 * x_1
    d_loss_w_1_22 = d_loss_predicted_output * w_2_21 * x_2
    d_loss_w_1_13 = d_loss_predicted_output * w_2_31 * x_1
    d_loss_w_1_23 = d_loss_predicted_output * w_2_31 * x_2

    # 使用梯度下降法更新权重
    w_2_11 -= learning_rate * d_loss_w_2_11
    w_2_21 -= learning_rate * d_loss_w_2_21
    w_2_31 -= learning_rate * d_loss_w_2_31

    w_1_11 -= learning_rate * d_loss_w_1_11
    w_1_12 -= learning_rate * d_loss_w_1_12
    w_1_13 -= learning_rate * d_loss_w_1_13
    w_1_21 -= learning_rate * d_loss_w_1_21
    w_1_22 -= learning_rate * d_loss_w_1_22
    w_1_23 -= learning_rate * d_loss_w_1_23

    layer_1_list = [w_1_11, w_1_12, w_1_13, w_1_21, w_1_22, w_1_23]
    layer_2_list = [w_2_11, w_2_21, w_2_31]
    return layer_1_list,layer_2_list


def parm_init():
    # 初始化定义权重
    w_1_11 = 0.5
    w_1_12 = 0.5
    w_1_13 = 0.5
    w_1_21 = 0.5
    w_1_22 = 0.5
    w_1_23 = 0.5

    w_2_11 = 1.0
    w_2_21 = 1.0
    w_2_31 = 1.0

    layer_1_list = [w_1_11,w_1_12,w_1_13,w_1_21,w_1_22,w_1_23]
    layer_2_list = [w_2_11,w_2_21,w_2_31]
    return layer_1_list, layer_2_list

if __name__ == '__main__':
    # 定义输入值和期望输出
    x_1 = 40.0
    x_2 = 80.0
    y_true = 60.0
    learning_rate = 1e-5

    epoch = 100

    '''
    初始化
    '''
    # 初始化定义权重
    layer_1_list, layer_2_list = parm_init()

    for i in range(epoch):

        # 正向传播
        y_pred = forward_propagation(layer_1_list,layer_2_list)
        # 计算损失
        loss = compute_loss(y_true, y_pred)
        print(f"第{i}次 预测值为： ", y_pred, " 误差为： ",loss)
        # 反向传播
        layer_1_list,layer_2_list = backward_propagation(layer_1_list,layer_2_list,learning_rate)









import numpy as np
import matplotlib.pyplot as plt

# 定义函数
def f(x):
    return x ** 2

# 导数（梯度）
def df(x):
    return 2 * x

# 梯度下降参数
lr = 0.1  # 学习率
n_iterations = 10  # 迭代次数
# x1 = np.random.uniform(-3, 3)  # 随机初始化 x
x1 = 2.5

# 梯度下降算法
for i in range(n_iterations):
    gradient = df(x1)
    x1 = x1 - lr * gradient  # 更新 x

# 绘制原始函数
x = np.linspace(-3, 3, 100)
y = f(x)
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="f(x) = x^2")

# 绘制梯度下降过程中 x 的位置
x_history = []
y_history = []

# 重新初始化 x1 用于演示
x1 = np.random.uniform(-3, 3)
for i in range(n_iterations):
    gradient = df(x1)
    x1 = x1 - lr * gradient  # 更新 x
    x_history.append(x1)
    y_history.append(f(x1))
    plt.scatter(x1, f(x1), color='red')

# 绘制梯度下降路径
plt.plot(x_history, y_history, label="Gradient Descent", color='red')

# 设置图形
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Function and Gradient Descent Path')
plt.grid(True)
plt.show()











import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 定义函数
def f(x):
    return x ** 2

# 导数（梯度）
def df(x):
    return 2 * x

# 梯度下降参数
lr = 0.1  # 学习率
n_iterations = 10  # 迭代次数
x1 = np.random.uniform(-3, 3)  # 随机初始化 x

# 绘制原始函数
x = np.linspace(-3, 3, 100)
y = f(x)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(x, y, label="f(x) = x^2")
point, = ax.plot([], [], 'ro', label="Gradient Descent")
value_display = ax.text(0.7, 0.02, '', transform=ax.transAxes)

# 初始化梯度下降过程的点
def init():
    point.set_data([], [])
    value_display.set_text('')
    return point, value_display

# 动画更新函数
def update(i):
    global x1
    gradient = df(x1)
    x1 -= lr * gradient  # 更新 x
    point.set_data(x1, f(x1))
    value_display.set_text('Min = ({:.2f}, {:.2f})'.format(x1, f(x1)))
    return point, value_display

# 创建动画
ani = FuncAnimation(fig, update, frames=np.arange(0, n_iterations), init_func=init, blit=True)

# 设置图形
ax.legend()
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Function and Gradient Descent Animation')
ax.grid(True)

plt.show()





import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# 创建x，y的数据点
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# 定义三维函数
def f(x, y):
    return x**2 + y**2

# 计算z的值
z = f(x, y)

# 创建图形和轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 绘制表面
ax.plot_surface(x, y, z, cmap='viridis')

# 设置标签和标题
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Surface Plot')

# 显示图形
plt.show()











"""





import matplotlib.pyplot as plt
import numpy as np

# 定义三维函数
def f(x, y):
    return x**2 + y**2

# 定义函数的梯度
def grad_f(x, y):
    return 2*x, 2*y

# 梯度下降函数
def gradient_descent(grad, start_x, start_y, learning_rate, num_iterations):
    x, y = start_x, start_y
    xs, ys, zs = [], [], []
    for i in range(num_iterations):
        dx, dy = grad(x, y)
        x, y = x - learning_rate * dx, y - learning_rate * dy
        z = f(x, y)
        xs.append(x)
        ys.append(y)
        zs.append(z)
    return xs, ys, zs

# 初始点
start_x, start_y = 3.0, 3.0

# 运行梯度下降
xs, ys, zs = gradient_descent(grad_f, start_x, start_y, 0.1, 50)

# 创建图形和轴
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 创建x，y的数据点
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = f(x, y)

# 绘制表面
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.7)

# 绘制梯度下降的点
ax.scatter(xs, ys, zs, color='r', s=50)

# 绘制点的连接线
for i in range(len(xs)-1):
    ax.plot([xs[i], xs[i+1]], [ys[i], ys[i+1]], [zs[i], zs[i+1]], 'r-')

# 设置标签和标题
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('Gradient Descent on 3D Surface')

# 显示图形
plt.show()



















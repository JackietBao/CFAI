"""

import numpy as np

# 定义矩阵 A 和 B
A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# 定义标量 c
c = 3

# 标量与矩阵的乘法
scalar_matrix_multiplication = c * A

# 矩阵的加法
matrix_addition = A + B

print(scalar_matrix_multiplication, matrix_addition)





import cv2
import numpy as np

# 读取图片
image = cv2.imread('MTALL-056-1.png')  # 替换为你的图片路径

# 增加亮度
# 为了避免溢出，使用cv2.add而不是直接加法
brighter_image = cv2.add(image, np.array([50.0]))  # 增加亮度

# 减少亮度
# 同样，使用cv2.subtract避免溢出
darker_image = cv2.subtract(image, np.array([50.0]))  # 减少亮度

# 将原图、增亮后的图和减暗后的图横向拼接
combined_image = cv2.hconcat([image, brighter_image, darker_image])

# 显示图片
cv2.imshow('Original - Brighter - Darker', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()









"""





import cv2
import numpy as np

# 读取图片
image = cv2.imread('056-1.png')  # 替换为你的图片路径

# 增加对比度
# 为了避免溢出，使用cv2.convertScaleAbs而不是直接乘法
increased_contrast = cv2.convertScaleAbs(image, alpha=1.5)  # alpha > 1 增加对比度

# 减少对比度
decreased_contrast = cv2.convertScaleAbs(image, alpha=0.5)  # alpha < 1 减少对比度

# 将原图、增加对比度后的图和减少对比度后的图横向拼接
combined_image = cv2.hconcat([image, increased_contrast, decreased_contrast])

# 显示图片
cv2.imshow('Original - Increased Contrast - Decreased Contrast', combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()




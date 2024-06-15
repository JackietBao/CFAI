"""
import numpy as np

# 创建向量,向量是一维的
vector = np.array([1, 2, 3, 4, 5])
vector_norm = np.linalg.norm(vector)
print("Vector:\n", vector)
print("Vector L2 Norm:", vector_norm)

# 创建矩阵,矩阵是二维的
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matrix_norm = np.linalg.norm(matrix)
print("\nMatrix:\n", matrix)
print("Matrix L2 Norm:", matrix_norm)

# 创建张量,张量是三维或更高维的
tensor = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
])
tensor_norm = np.linalg.norm(tensor)
print("\nTensor:\n", tensor)
print("Tensor L2 Norm:", tensor_norm)



"""



import numpy as np
import cv2

# 创建一个大小为224x224的二维矩阵，值在0-255之间
two_d_matrix = np.random.randint(0, 256, (224, 224), dtype=np.uint8)

# 创建一个大小为3x224x224的三维矩阵，值在0-255之间
three_d_matrix = np.random.randint(0, 256, (3, 224, 224), dtype=np.uint8)

# 将三维矩阵转换为224x224x3，以便用于图像保存
# 对于OpenCV，需要将矩阵的维度变为高x宽x通道数
three_d_matrix_transposed = three_d_matrix.transpose(1, 2, 0)

# 显示图像
cv2.imshow('two_d_image.png', two_d_matrix)
cv2.imshow('three_d_image.png', three_d_matrix_transposed)
cv2.waitKey(0)

# 使用OpenCV保存这些矩阵为图像
cv2.imwrite('two_d_image.png', two_d_matrix)
cv2.imwrite('three_d_image.png', three_d_matrix_transposed)

print("图像已保存。")



























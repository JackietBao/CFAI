"""
import numpy as np

# 定义矩阵 A
A = np.array([[4, 1],
              [2, 3]])

# 使用numpy求特征值和特征向量
eigenvalues, eigenvectors = np.linalg.eig(A)

eigenvalues, eigenvectors


print("特征向量：", eigenvectors)











"""


import cv2
import numpy as np

# 读取图像
image = cv2.imread('wallhaven-1kvjk1_2898x3598.png', 0)

# 对图像进行svd分解
U, S, V = np.linalg.svd(image.astype(np.float64), full_matrices=False)

# 定义要保留的奇异值数量
k = 10
s_k = np.diag(S[:k])

# 重构图像
compressed_image = np.dot(U[:,:k], np.dot(s_k, V[:k,:]))
compressed_image = np.clip(compressed_image, 0, 255).astype(np.uint8)

# 显示图像
cv2.imshow('Original Image', image)
cv2.imshow('Compress Image', compressed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()



import numpy as np

# # 建立一個2*3的矩陣
# matrix = np.array([[1, 2, 3], [4, 5, 6]])

# print(matrix)
# print(matrix.shape)

# matrix = np.array([[10, 20, 30], [40, 50, 60]])

# print(matrix[0])

# 取出每一列的第一欄
# print(matrix[:, 1])

# print(matrix[1, 2])


data = np.array([
    [25, 50000, 10], # 客戶 A
    [40, 120000, 5], # 客戶 B
    [32,870000, 12]  # 客戶 C
])

# 如何快速取出A, B兩位客戶的年齡與存款資料?

result = data[0:2, 0:2]

print(result)
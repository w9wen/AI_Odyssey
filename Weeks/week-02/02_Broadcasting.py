import numpy as np

# suppress=True 代表壓制科學記號，precision=2 代表小數點後兩位
np.set_printoptions(suppress=True, precision=2)

# # matrix  = np.array([[1, 2, 3], [4, 5, 6]])
# # print(matrix)

# # # 直接加 100
# # result = matrix + 100
# # print(result)

# data = np.array([
#     [50000], # 客戶 A
#     [120000], # 客戶 B
#     [80000] # 客戶 C
# ])

# print(data)

# # 每位客戶存款加 5000
# new_data = data + 5000
# print(new_data)

# # 三位客人，兩項資料 [年齡, 存款]
# data = np.array([
#     [25, 50000], # 客戶 A
#     [40, 120000], # 客戶 B
#     [32, 80000]  # 客戶 C
# ])

# # 年齡加一歲，存款加 5000
# age_increase = np.array([1, 5000])
# new_data = data + age_increase
# print(new_data)

# # 計算每一欄的平均值
# mean_values = np.mean(data, axis=0)
# print("Mean values (Age, Savings):", mean_values)

# guest_a = np.array([25, 50000]) # 年齡, 存款
# ai = np.array([0.1, 0.001])    # 權重相加
# score = guest_a @ ai  # 內積運算
# print("Guest A score:", score)

# 三位客人，兩項資料 [年齡, 存款]
all_guests = np.array([
    [25, 50000], 
    [40, 120000], 
    [32, 80000]
])  # 客戶 A  # 客戶 B  # 客戶 C

# AI 權重
weights = np.array([
    0.1,
    0.001
])  # 權重

# # 計算每位客戶的分數
# all_scores = all_guests @ weights  # 矩陣乘法
# print("Scores for each customer:", all_scores)

# w = 1 # 權重
# b = 3 # 偏差

# x = np.array([5])
# w = np.array([1]) # 權重
b = 3 # 偏差

# prediection = x @ w + b
# print(prediection)

prediections_all_guests = all_guests @ weights + b
print(prediections_all_guests)
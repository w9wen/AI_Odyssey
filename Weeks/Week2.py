import numpy as np
import matplotlib.pyplot as plt

# numpy
# x = np.arange(0, 5)
# print(x)

# y_1 = x
# y_2 = x * 2
# y_3 = x + 3

# # matplotlib
# plt.plot(y_1)
# plt.plot(y_2)
# plt.plot(y_3)
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("Simple Plot")
# plt.legend(["y=x", "y=2x", "y=x+3"])
# plt.show()

# x = 2
# y = 1
# 1. 準備資料
x = np.array([0, 1, 2, 3, 4])
y = np.array([5, 2, 1, 8, 6])

# 2. 建立決策邊界 (模型)
# y = x + 3
line_x = np.arange(0, 5)
line_y = line_x + 3

# 3. 進行預測 (分類)
prediction = y > line_y # 這就是那個 [True, False, ...] 的遮罩

# 4. 繪圖
plt.figure(figsize=(6, 6))

# 畫出決策邊界 (綠線)
plt.plot(line_x, line_y, color='green', label='Decision Boundary (y=x+3)')

# 畫出分類結果
# prediction 為 True 的點 (上方)
plt.scatter(x[prediction], y[prediction], color='red', s=100, label='True (Class A)')

# prediction 為 False 的點 (下方) - 用 ~ 符號來取反向 (Not)
plt.scatter(x[~prediction], y[~prediction], color='blue', s=100, label='False (Class B)')

plt.legend()
plt.grid(True)
plt.show()
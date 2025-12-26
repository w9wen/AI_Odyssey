import numpy as np

np.set_printoptions(precision=4, suppress=True)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# # 假設這是三位客人的原始得分
# # 1. 分數很高 (5)
# # 2. 分數剛好是中立 (0)
# # 3. 分數很低 (-5)
# scores = np.array([5, 0, -5])
# sigmoid_scores = sigmoid(scores)
# print("Sigmoid 函數結果:", sigmoid_scores)

# scores = np.array([-10, -1, 0, 1, 10])

# sigmoid_scores = sigmoid(scores)
# print("Sigmoid 函數結果:", sigmoid_scores)

np.set_printoptions(precision=15, suppress=True)

x1 = np.array([10])
x2 = np.array([100])

print("Sigmoid(10):", sigmoid(x1))
print("Sigmoid(100):", sigmoid(x2))
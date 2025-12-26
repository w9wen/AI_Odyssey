import numpy as np

# 計算 e 的 1 次方
# print(np.exp(1))


# 設定顯示的格式
np.set_printoptions(precision=2, suppress=True)

# 1. 準備兩組特徵分數 (A是一般表現，B是優異表現)
scores = np.array([1, 5, -2])

# 2. 計算指數函數
exp_scores = np.exp(scores)
print("指數函數結果:", exp_scores)
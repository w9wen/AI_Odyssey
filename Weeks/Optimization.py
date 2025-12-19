# x = 3 # 初始位置
# learning_rate = 0.1 # 學習率
# steps = 20 # 迭代次數，我們走的步數
# precision = 0.0001 # 停止更新的門檻

# for i in range(steps):
#     # 1. 計算斜率  (之前假設 y = x^2, 所以斜率是2*x)
#     slope = 2 * x

#     # 判斷斜率大小是否已經可以小到可以忽略了
#     print(f"abs(slope) = {abs(slope)}")
#     if abs(slope) <= precision:
#         break

#     # 2. 更新位置 (走一步)
#     x = x - learning_rate * slope

#     print(f"Step {i+1}: x = {x:.4f}, slope = {slope:.4f}")
#     pass

x = 3
learning_rate = 0.1
precision = 0.0001  # 停止更新的門檻

# 當坡度還「不夠平」的時候，就繼續走
while True:
    slope = 2 * x
    
    # 判斷斜率的大小是否已經小到可以忽略了？
    if abs(slope) < precision:
        break
        
    x = x - (learning_rate * slope)
    print(f"x = {x:.4f}, slope = {slope:.4f}")


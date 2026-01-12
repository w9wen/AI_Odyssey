import torch
import torch.nn as nn
import torch.optim as optim

# 1. 準備數據 (y = 2x + 1)
# 我們隨機生成100個x值，形狀為 (100, 1)
x_train = torch.randn(100, 1) * 10

# 根據公式生成y, 並加上一些隨機噪聲
y_train = 2 * x_train + 1 + torch.randn(100, 1) * 2


# 2. 建立模型
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        # 定義一個線性層，這裡使用一個簡單的線性模型，輸入1個值，輸出1個值
        self.linear = nn.Linear(1, 1)

    def forward(self, x):
        # 定義數據如何流過模型 (正向傳播)
        return self.linear(x)


# 實例化模型
model = SimpleModel()

# 3. 定義損失函數與優化器
# 使用均方誤差(MSE)
criterion = nn.MSELoss()

# 使用隨機梯度下降作為優化器(SGD), 傳入模型的參數與學習率
# model.parameters() 傳入模型的參數會自動把模型內所有Linear層的weight和bias都交給優化器
optimizer = optim.SGD(model.parameters(), lr=0.01)


# 4. 開始訓練循環
epochs = 100  # 讓模型練習 100 次

for epoch in range(epochs):
    # (1) 正向傳播: 把 x 丟進模型得到預測值
    predictions = model(x_train)

    # (2) 計算損失值: 預測值跟真實答案差多少
    loss = criterion(predictions, y_train)

    # (3) 梯度歸零，這很重要，避免上次的梯度影響到這次的訓練
    optimizer.zero_grad()

    # (4) 反向傳播: 計算梯度
    loss.backward()

    # (5) 更新參數: 真正跨出那一步
    optimizer.step()

    # 印出進度
    # if (epoch + 1) % 10 == 0:
    print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

# 5. 檢查成果
print("-" * 30)
# 檢查模型學到的參數是否接近 w=2, b=1
print(f"學到的權重 (Weight): {model.linear.weight.item():.4f}")
print(f"學到的偏差 (Bias): {model.linear.bias.item():.4f}")

import torch
import torch.nn as nn

# 建立一個線性層: 輸入維度 2, 輸出維度 1
layer = nn.Linear(in_features=2, out_features=1)

# 查看他內部的初始權重和偏差
print(f"初始權重 (Weights): {layer.weight}")
print(f"初始偏差 (Bias): {layer.bias}")

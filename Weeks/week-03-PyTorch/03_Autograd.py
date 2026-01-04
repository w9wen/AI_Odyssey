import torch

torch.set_printoptions(precision=4)

# 建立一個 requires_grad=True 的張量
x = torch.tensor([3.0], requires_grad=True)

# 3. 定義一個簡單的函數 y = x^2
y = x ** 3

print(f"張量 x = {x}")
print(f"運算結果 y = {y}")

y.backward()  # 自動計算 y 對 x 的導數
print(f"張量 x 的導數 = {x.grad}")


import torch
import time

# 建立兩個形狀為 (10000, 10000) 的張量，先把他們放在 CPU 上
tensor1 = torch.randn(10000, 10000)
tensor2 = torch.randn(10000, 10000)

# 在 CPU 上進行矩陣乘法並計時
start_cpu = time.time()
result_cpu = torch.matmul(tensor1, tensor2)
end_cpu = time.time()
print(f"CPU 矩陣乘法時間: {end_cpu - start_cpu} 秒")

# 如果有可用的 GPU，將張量移動到 GPU 上
if torch.cuda.is_available():
    tensor1_gpu = tensor1.to('cuda')
    tensor2_gpu = tensor2.to('cuda')

    # 在 GPU 上進行矩陣乘法並計時
    start_gpu = time.time()
    result_gpu = torch.matmul(tensor1_gpu, tensor2_gpu)
    end_gpu = time.time()
    print(f"GPU 矩陣乘法時間: {end_gpu - start_gpu} 秒")
else:
    print("沒有可用的 GPU，無法進行 GPU 計算。")
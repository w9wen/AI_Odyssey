import torch
import time
import platform

# 自動檢測最佳可用設備
def get_device():
    """自動檢測並返回最佳可用設備"""
    if torch.cuda.is_available():
        return torch.device('cuda'), 'NVIDIA CUDA GPU'
    elif torch.backends.mps.is_available():
        return torch.device('mps'), 'Apple Silicon GPU (MPS)'
    else:
        return torch.device('cpu'), 'CPU'

# 顯示系統資訊
print(f"作業系統: {platform.system()} {platform.machine()}")
print(f"Python 版本: {platform.python_version()}")
print(f"PyTorch 版本: {torch.__version__}")
print("-" * 50)

device, device_name = get_device()
print(f"使用設備: {device_name}")
print("-" * 50)

# 建立兩個形狀為 (10000, 10000) 的張量，先把他們放在 CPU 上
tensor1 = torch.randn(100000, 100000)
tensor2 = torch.randn(100000, 100000)

# 在 CPU 上進行矩陣乘法並計時
start_cpu = time.time()
result_cpu = torch.matmul(tensor1, tensor2)
end_cpu = time.time()
cpu_time = end_cpu - start_cpu
print(f"CPU 矩陣乘法時間: {cpu_time:.4f} 秒")

# 如果有可用的 GPU (CUDA 或 MPS)，將張量移動到 GPU 上
if device.type != 'cpu':
    tensor1_gpu = tensor1.to(device)
    tensor2_gpu = tensor2.to(device)

    # 暖機 (第一次運行可能較慢)
    _ = torch.matmul(tensor1_gpu, tensor2_gpu)
    
    # 同步確保 GPU 完成計算
    if device.type == 'cuda':
        torch.cuda.synchronize()
    elif device.type == 'mps':
        torch.mps.synchronize()

    # 在 GPU 上進行矩陣乘法並計時
    start_gpu = time.time()
    result_gpu = torch.matmul(tensor1_gpu, tensor2_gpu)
    
    # 同步確保 GPU 完成計算
    if device.type == 'cuda':
        torch.cuda.synchronize()
    elif device.type == 'mps':
        torch.mps.synchronize()
    
    end_gpu = time.time()
    gpu_time = end_gpu - start_gpu
    print(f"GPU 矩陣乘法時間: {gpu_time:.4f} 秒")
    
    # 計算加速比
    speedup = cpu_time / gpu_time
    print("-" * 50)
    print(f"🚀 GPU 加速比: {speedup:.2f}x")
else:
    print("沒有可用的 GPU，無法進行 GPU 計算。")
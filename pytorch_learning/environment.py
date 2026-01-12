import torch

# 1. 檢查版本
print("PyTorch 版本:", torch.__version__)

# 2. 檢查是否有可用的 GPU
print("是否有可用的 GPU:", torch.cuda.is_available())

# 3.列舉目前顯示卡
if torch.cuda.is_available():
    num_gpus = torch.cuda.device_count()
    print("可用的 GPU 數量:", num_gpus)
    for i in range(num_gpus):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
import numpy as np
import matplotlib.pyplot as plt

# 產生由-5到5的100個點
x = np.linspace(-5, 5, 100)
y = x ** 2 # 平方是 **2表示

plt.figure(figsize=(6, 4))
plt.plot(x, y, label='y = x^2(Loss Function)')

plt.title('The "Bowl" of Error')
plt.xlabel('Parameter (Weight)')
plt.ylabel('Error (Loss)')
plt.grid(True)
plt.legend()
plt.show()
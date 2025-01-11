import numpy as np

# ایجاد 10 نقطه تصادفی در فضای 2 بعدی
np.random.seed(0)  # برای تکرارپذیری
points = np.random.rand(10, 2)

print(points)

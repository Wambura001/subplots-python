import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(x / 10)

# Create a figure
plt.figure(figsize=(10, 8))

# Create subplots
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st subplot
plt.plot(x, y1)
plt.title('Sine Wave')

plt.subplot(2, 2, 2)  # 2 rows, 2 columns, 2nd subplot
plt.plot(x, y2)
plt.title('Cosine Wave')

plt.subplot(2, 2, 3)  # 2 rows, 2 columns, 3rd subplot
plt.plot(x, y3)
plt.title('Tangent Wave')

plt.subplot(2, 2, 4)  # 2 rows, 2 columns, 4th subplot
plt.plot(x, y4)
plt.title('Exponential Function')

# Adjust layout
plt.tight_layout()
plt.show()

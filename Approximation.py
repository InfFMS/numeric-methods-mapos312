import matplotlib.pyplot as plt
import numpy as np

I =([0.1, 0.311, 0.522, 0.733, 0.944, 1.156, 1.367, 1.578, 1.789, 2.0])
U =([0.599, 1.528, 2.741, 3.971, 4.675, 5.731, 7.149, 8.042, 8.851, 10.109])
fig = plt.figure()
plt.scatter(I, U, color="red")
A = 0
B = 0

for i in range(len(I)):
    A += I[i] ** 2
    B += I[i] * U[i] * 2

k = B/(2*A)
print(k)
x = np.linspace(0, I[-1], 1000)
y = np.array(x * k)
plt.plot(x, y, color="black")
plt.grid()
plt.show()
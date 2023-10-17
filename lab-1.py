import numpy as np
import matplotlib.pyplot as plt

a = 0.1
b = 2.0
# точність
eps = 0.001
max_iterations = 1000

y_values = []

def fun(x):
    return x**2 * np.e**(1-x**2)

#метод дихотомії
def dyhotomy(a, b, eps):
    while (b - a) >= eps:
        c = (a + b) / 2

        if fun(c) > fun(b):
            b = c
        else:
            a = c

    return (a + b) / 2

result_dyhotomy = dyhotomy(a, b, eps)
print(f"Максимальна точка в межах від {a} до {b} x = {result_dyhotomy}, y = {fun(result_dyhotomy)}")
plt.scatter(result_dyhotomy, fun(result_dyhotomy), color='red', s=20, zorder=2)

#метод ітерацій
def iteration(a, b, eps):
    x0 = fun(a)
    max_iterations = 1000
    i = 0

    while i < max_iterations:
        x1 = x0 + eps
        if x1 != b:
            if fun(x1) > fun(x0):
                x0 = x1
            else:
                break
        i += 1
    return abs(x0)

result_iteration = iteration(a, b, eps)
print(f"Максимальна точка в межах від {a} до {b} x = {result_iteration}, y = {fun(result_iteration)}")
plt.scatter(result_iteration, fun(result_iteration), color='green', s=70, alpha= 0.5, zorder=1)

#графік
x_value = np.linspace(-5, 5, 100)
for x in x_value:
    y_values.append(fun(x))

y_value = y_values
plt.plot(x_value, y_value, color='blue', zorder=0)
plt.axhline(y=0, color="red")
plt.legend(['By dyhotomy result', 'By iteration result'], loc='upper left')
plt.grid()
plt.show()








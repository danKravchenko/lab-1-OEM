import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [56.9, 67.3, 81.6, 201, 240, 474, 490, 518]

s_1 = 0
s_2 = 0
s_3 = 0
s_4 = 0

a = 0
b = 0

def build_regression_line(a, b):
    y_regression = []
    for i in x:
        y_regression.append(a * i + b)
    return y_regression

def total_least_squares(s_1, s_2, s_3, s_4, a, b):
    for i, j in zip(x, y):
        s_1 += i * j
        s_2 += i
        s_3 += j
        s_4 += i ** 2

        a = (len(x) * s_1 - s_2 * s_3) / (len(x) * s_4 - s_2 ** 2)
        b = (s_3 - (a * s_2)) / len(x)
    return s_1, s_2, s_3, s_4, a, b

def lagrange_interpolation(x, y, targetX):
    result = []
    n = len(x)

    for target in targetX:
        interp_value = 0
        for i in range(n):
            term = y[i]
            for j in range(n):
                if j != i:
                    term *= (target - x[j]) / (x[i] - x[j])
            interp_value += term
        result.append(interp_value)

    return result

root = tk.Tk()
root.geometry("600x600")
root.title("Інтерполяція та регресія")

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def build_graph(first_par, second_par, third_par):
    ax.clear()
    ax.scatter(x, y, color='red', s=30, zorder=2, label='Експериментальні точки')
    ax.legend()
    ax.grid()

    if first_par is not None:
        if first_par:
            ax.plot(x, second_par, color='blue', zorder=0, alpha=0.8, label='Пряма регресії', linewidth=2.5)
        else:
            ax.scatter(x, third_par, color='green', s=10, zorder=2)

    canvas.draw()

build_graph(None, None, None)

def res_total_least_squares():
    result = total_least_squares(s_1, s_2, s_3, s_4, a, b)
    update_result = build_regression_line(result[4], result[5])
    build_graph(True, update_result, None)

def res_lagrange_interpolation():
    result = lagrange_interpolation(x, y, x)
    build_graph(False, None, result)

tk.Button(text="Обчислити регресію", command=res_total_least_squares).pack()
tk.Button(text="Обчислити інтерполяцію", command=res_lagrange_interpolation).pack()

root.mainloop()

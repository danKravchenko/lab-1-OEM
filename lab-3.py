import numpy as np
import matplotlib.pyplot as plt
import math
import random
from matplotlib.patches import Polygon
import tkinter as tk

def fun(x):
    return (x**2)*(math.e**(1-x**2))

# Метод прямокутників
def rectangles_method():
    a = float(border_a_input_area.get())
    b = float(border_b_input_area.get())
    n = int(border_n_input_area.get())

    S = 0
    h = (b - a) / n
    x = a

    while x < b:
        F = fun(x)
        S += F
        x += h

    S = h * S
    result_1.config(text=f"Відповідь: = {S}", bg="yellow")
    plt.close()
    build_graph()

# Метод трапецій
def trapezium_method():
    a = float(border_a_input_area.get())
    b = float(border_b_input_area.get())
    n = int(border_n_input_area.get())

    S = 0
    h = (b - a) / n
    x = a + h

    while x < b:
        F = fun(x)
        S += F
        x += h

    S = (h / 2) * (fun(a) + fun(b) + 2 * S)
    result_2.config(text=f"Відповідь: = {S}", bg="yellow")
    plt.close()
    build_graph()

# Метод Монте-Карло
def monte_carlo_method():
    a = float(border_a_input_area.get())
    b = float(border_b_input_area.get())
    n = int(border_n_input_area.get())

    i = 0
    minX = a
    maxX = b
    S = 0
    while i != n:
         i += 1
         randX = minX + (maxX - minX) * random.uniform(0, 1)
         S += fun(randX)

    integrate = (b - a) * (S / n)
    result_3.config(text=f"Відповідь: = {integrate}", bg="yellow")
    plt.close()
    build_graph()

def build_graph():
    # Задаємо межі відображення графіку
    x_value = np.linspace(-5, 5, 100)
    y_values = []  # Очистити список перед використанням

    a = float(border_a_input_area.get())
    b = float(border_b_input_area.get())

    # Виводимо заштриховану площу
    fig, ax = plt.subplots()
    ax.plot(x_value, fun(x_value), linewidth=2)
    ax.set_ylim(bottom=0)

    ix = np.linspace(a, b)
    iy = fun(ix)
    verts = [(a, 0), *zip(ix, iy), (b, 0)]
    poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
    ax.add_patch(poly)

    # Графік
    for x in x_value:
        y_values.append(fun(x))

    y_value = y_values
    plt.plot(x_value, y_value, color='blue', zorder=0)
    plt.axhline(y=0, color="red", linewidth=3)
    plt.grid()
    plt.show()

def start():
    global border_a_input_area, border_b_input_area, border_n_input_area
    global result_1, result_2, result_3

    root = tk.Tk()
    root.geometry("430x450")
    root.title("Задання значень")

    tk.Label(text="Нижня межа a:").place(x=30, y=15)
    border_a_input_area = tk.Entry(root, width=10)
    border_a_input_area.place(x=130, y=15)

    tk.Label(text="Верхня межа b:").place(x=30, y=60)
    border_b_input_area = tk.Entry(root, width=10)
    border_b_input_area.place(x=130, y=60)

    tk.Label(text="N частин або кількість точок в методі Монте-Карло:").place(x=30, y=105)
    border_n_input_area = tk.Entry(root, width=10)
    border_n_input_area.place(x=330, y=105)

    tk.Label(text="Обчислити інтеграл методом прямокутників").place(x=30, y=150)
    tk.Button(text="Обчислити", command=rectangles_method).place(x=290, y=148)

    result_1 = tk.Label(root, text="")  # Створення Label
    result_1.place(x=30, y=180)

    tk.Label(text="Обчислити інтеграл методом трапецій").place(x=30, y=245)
    tk.Button(text="Обчислити", command=trapezium_method).place(x=290, y=245)

    result_2 = tk.Label(root, text="")  # Створення Label
    result_2.place(x=30, y=275)

    tk.Label(text="Обчислити інтеграл методом Монте-Карло").place(x=30, y=340)
    tk.Button(text="Обчислити", command=monte_carlo_method).place(x=290, y=340)

    result_3 = tk.Label(root, text="")  # Створення Label
    result_3.place(x=30, y=370)

    root.mainloop()

start()

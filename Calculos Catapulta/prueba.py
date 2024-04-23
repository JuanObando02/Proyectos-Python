from math import cos, sin, pi
from numpy import linspace
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button

def calcular_simulacion():
    θ = float(angle_entry.get())
    v0 = float(velocity_entry.get())
    yo = float(height_entry.get())

    g = 9.81  # Aceleración de la gravedad, m/s2
    k = 0.01  # Constante de fricción (ajustable)

    Iteraciones_total = 1000
    Iteraciones = linspace(0, Iteraciones_total, 10 * Iteraciones_total)

    Y = lambda t, v: -(0.5 * g * (t ** 2)) + (v0 * sin(θ * pi / 180) * t) + yo
    X = lambda t, v: (v0 * cos(θ * pi / 180) * t)

    y = [Y(t, v0) for t in Iteraciones if Y(t, v0) > 0 and X(t, v0) >= 0]
    x = [X(t, v0) for t in Iteraciones if Y(t, v0) > 0 and X(t, v0) >= 0]

    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)
    line, = ax.plot(x, y, 'b+')

    x_max = max(max(x), max(y))
    x_min = min(min(x), min(y))
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(x_min, x_max)

    ax.axhline(y=0, linewidth=20, color='gray', linestyle="-")

    plt.plot(0, yo, 'ko', markersize=50.0)

    for i in range(len(y)):
        v = v0 - k * i  # Reducción de velocidad debido a la fricción
        line.set_xdata(x[:i])
        line.set_ydata(y[:i])
        fig.canvas.draw()
        fig.canvas.flush_events()

        if i == len(y) - 1:
            plt.title('SIMULACIÓN DE UN PROYECTIL')
            plt.xlabel(f'Distancia de impacto: {round(max(x), 2)} metros', weight='bold', color='k')
            plt.ylabel(f'Altura máxima alcanzada: {round(max(y), 2)} metros', weight='bold', color='k')
            plt.plot(x[-1], y[-1], 'r*', markersize=100.0)

    input("Presiona Enter para salir...")

# Crear la ventana de la interfaz gráfica
root = Tk()
root.title("Simulación de Proyectil")

# Etiquetas y campos de entrada para los datos
angle_label = Label(root, text="Ángulo de tiro (grados):")
angle_label.pack()
angle_entry = Entry(root)
angle_entry.pack()

velocity_label = Label(root, text="Velocidad inicial (m/s):")
velocity_label.pack()
velocity_entry = Entry(root)
velocity_entry.pack()

height_label = Label(root, text="Altura inicial (metros):")
height_label.pack()
height_entry = Entry(root)
height_entry.pack()

# Botón para iniciar la simulación
simulate_button = Button(root, text="Simular", command=calcular_simulacion)
simulate_button.pack()

# Ejecutar la ventana principal
root.mainloop()

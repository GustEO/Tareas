import numpy as np
import matplotlib.pyplot as plt

def plot_circle(center, radius, edge_color, face_color):
    #Definicion de los puntos
    theta = np.linspace(0, 2*np.pi, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)

    #creacion de la figura y arrglos
    plt.plot(x, y,'--', color=edge_color, lw=2)
    plt.fill(x, y, facecolor=face_color)
    plt.axis('equal')
    plt.xlabel('Parte real')
    plt.ylabel('Parte Imaginaria ')
    plt.title('Gráfico del contorno "C" del problema. $|z| =2$')

    #agragar polos
    plt.scatter([-3, 3], [0, 0], color='red', marker='o')
    
    #textos
    plt.text(-3, -0.5, '$z_{1}$', fontsize=16, ha='center')
    plt.text(3, 0.5, '$z_{2}$', fontsize=16, ha='center')
    plt.text(1.5,1.5,'C',fontsize=16, ha='center')
    plt.text(0,-0.3,'(0,0)',fontsize=12, ha='center')
    plt.text(0.7,0.3,'z',fontsize=16, ha='center')
    plt.text(-1,0.2,'$|z| =2$',fontsize=12, ha='center')

    #vector que representa a z
    vector_start = (0, 0)  # Punto de inicio del vector
    vector = (1, 1)  # Componentes del vector
    vector_start = (0, 0)  # Punto de inicio del vector
    plt.arrow(vector_start[0], vector_start[1], vector[0], vector[1], color='black', width=0.03)


    #linea para mostrar el radio del contorno
    x_line = [-2, 0]  # Coordenadas x de la línea
    y_line = [0, 0]  # Coordenadas y de la línea
    plt.plot(x_line, y_line, color='purple', linestyle='--', linewidth=2)

    plt.show()

center = (0, 0)
radius = 2
edge_color = 'blue'
face_color = 'green'

plot_circle(center, radius, edge_color, face_color)
plt.show()




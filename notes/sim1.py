import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros do modelo
L = 1000  # Extensão da praia (m)
Nx = 200  # Número de pontos espaciais
dx = L / Nx  # Espaçamento espacial
dt = 1  # Passo de tempo (s)
T = 500  # Tempo total da simulação (s)
g = 9.81  # Aceleração gravitacional (m/s^2)
D = 0.1  # Coeficiente de difusão (m^2/s)

# Inicialização das variáveis
x = np.linspace(0, L, Nx)
h = np.exp(-((x - L/2) / 100) ** 2)  # Perfil inicial de sedimentos
Q_s = np.zeros(Nx)  # Fluxo de sedimentos

# Função para atualizar a topografia da praia
def update_topography(h, Q_s, dx, dt, D):
    dQ_s_dx = np.gradient(Q_s, dx)
    dh_dt = -dQ_s_dx
    h += dh_dt * dt
    
    # Difusão para suavizar o perfil da praia
    h += D * np.gradient(np.gradient(h, dx), dx) * dt
    
    return h

# Função para calcular fluxo de sedimentos (simplificado)
def compute_sediment_flux(h, dx):
    slope = np.gradient(h, dx)
    return -slope  # Fluxo proporcional à inclinação

# Configuração da animação
fig, ax = plt.subplots()
ax.set_xlim(0, L)
ax.set_ylim(-0.1, 1.2)
line, = ax.plot(x, h, label='Evolução da Praia')
ax.legend()

def animate(frame):
    global h, Q_s
    Q_s = compute_sediment_flux(h, dx)
    h = update_topography(h, Q_s, dx, dt, D)
    line.set_ydata(h)
    return line,

ani = FuncAnimation(fig, animate, frames=T, interval=50)
plt.xlabel('Posição (m)')
plt.ylabel('Elevação do fundo (m)')
plt.title('Evolução Morfodinâmica da Praia')
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros do modelo ajustados para a Praia do Cepilho
Lx, Ly = 1200, 500  # Extensão da praia (m) em x e y
Nx, Ny = 400, 250  # Número de pontos espaciais em x e y
dx, dy = Lx / Nx, Ly / Ny  # Espaçamento espacial
dt = 1  # Passo de tempo (s)
T = 1000  # Tempo total da simulação (s)
D = 0.15  # Coeficiente de difusão (m^2/s)
alpha = 0.02  # Coeficiente de transporte de sedimentos

# Inicialização das variáveis
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)

# Adicionando elementos topográficos específicos da Praia do Cepilho
h = 0.4 * np.exp(-((X - Lx/4) / 100) ** 2 - ((Y - Ly/2) / 80) ** 2)  # Formação rochosa sul
h += 0.3 * np.exp(-((X - 3*Lx/4) / 120) ** 2 - ((Y - Ly/3) / 90) ** 2)  # Formação rochosa norte
h -= 0.2 * np.exp(-((X - Lx/2) / 150) ** 2 - ((Y - 2*Ly/3) / 100) ** 2)  # Canal de escoamento

Q_sx = np.zeros((Ny, Nx))  # Fluxo de sedimentos em x
Q_sy = np.zeros((Ny, Nx))  # Fluxo de sedimentos em y

# Função para calcular fluxo de sedimentos baseado na inclinação
def compute_sediment_flux(h, dx, dy, alpha):
    # Calcula o fluxo de sedimentos nas direções x e y:
    # Q_sx = -\alpha \frac{\partial h}{\partial x}, \quad Q_sy = -\alpha \frac{\partial h}{\partial y}
    slope_x = np.gradient(h, axis=1) / dx
    slope_y = np.gradient(h, axis=0) / dy
    return -alpha * slope_x, -alpha * slope_y

# Função para atualizar a topografia
def update_topography(h, Q_sx, Q_sy, dx, dy, dt, D):
    # Atualiza a topografia com a equação da conservação de massa dos sedimentos em 2D:
    # \frac{\partial h}{\partial t} = -\nabla \cdot \vec{Q_s} + D \nabla^2 h 
    dQ_sx_dx = np.gradient(Q_sx, axis=1) / dx
    dQ_sy_dy = np.gradient(Q_sy, axis=0) / dy
    
    dh_dt = -(dQ_sx_dx + dQ_sy_dy)  # Variação da altura
    h += dh_dt * dt  # Atualização da topografia
    
    # Termo difusivo
    h += D * (np.gradient(np.gradient(h, axis=1), axis=1) / dx**2 +
              np.gradient(np.gradient(h, axis=0), axis=0) / dy**2) * dt
    
    return h

# Configuração da animação
fig, ax = plt.subplots()
cmap = ax.imshow(h, extent=[0, Lx, 0, Ly], origin='lower', cmap='terrain', vmin=-0.2, vmax=0.5)
plt.colorbar(cmap, label='Altura do fundo (m)')
plt.xlabel('Posição x (m)')
plt.ylabel('Posição y (m)')
plt.title('Evolução Morfodinâmica da Praia do Cepilho')

def animate(frame):
    global h, Q_sx, Q_sy
    Q_sx, Q_sy = compute_sediment_flux(h, dx, dy, alpha)  # Cálculo do fluxo de sedimentos
    h = update_topography(h, Q_sx, Q_sy, dx, dy, dt, D)  # Atualização da topografia
    cmap.set_data(h)
    return cmap,

# Criando animação da evolução da praia ao longo do tempo
ani = FuncAnimation(fig, animate, frames=T, interval=50)
plt.show()

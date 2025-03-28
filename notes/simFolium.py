#!pip install folium
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import folium
from folium.plugins import HeatMap

# Parâmetros do modelo ajustados para a Praia do Cepilho
Lx, Ly = 600, 200  # Extensão da praia (m) em x e y
Nx, Ny = 200, 100  # Número de pontos espaciais em x e y
dx, dy = Lx / Nx, Ly / Ny  # Espaçamento espacial
dt = 1  # Passo de tempo (s)
T = 500  # Tempo total da simulação (s)
D = 0.15  # Coeficiente de difusão (m^2/s)
alpha = 0.02  # Coeficiente de transporte de sedimentos

# Coordenadas aproximadas da Praia do Cepilho
lat_base, lon_base = -23.3525, -44.7206

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
    slope_x = np.gradient(h, axis=1) / dx
    slope_y = np.gradient(h, axis=0) / dy
    return -alpha * slope_x, -alpha * slope_y

# Função para atualizar a topografia
def update_topography(h, Q_sx, Q_sy, dx, dy, dt, D):
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

# Gerando um heatmap para visualização no Google Maps
heatmap_data = []
for i in range(Ny):
    for j in range(Nx):
        lat = lat_base + (i / Ny) * 0.002  # Pequena variação latitudinal
        lon = lon_base + (j / Nx) * 0.003  # Pequena variação longitudinal
        heatmap_data.append([lat, lon, h[i, j]])

# Criando o mapa
mapa = folium.Map(location=[lat_base, lon_base], zoom_start=16)
HeatMap(heatmap_data).add_to(mapa)
mapa.save("praia_cepilho_simulacao.html")

print("Mapa salvo como praia_cepilho_simulacao.html. Abra no navegador para visualizar.")

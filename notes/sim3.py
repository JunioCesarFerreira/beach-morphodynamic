import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parâmetros realísticos para Praia do Cepilho
Lx, Ly = 1200, 300  # Extensão da praia (m)
Nx, Ny = 600, 200   # Maior resolução espacial
dx, dy = Lx/Nx, Ly/Ny
dt = 3600           # Passo de tempo de 1 hora (em segundos)
T = 24*5            # Simulação de 5 dias (em passos de hora)

# Coeficientes ajustados com base em dados de campo
D = 0.05            # Coeficiente de difusão reduzido (m²/s)
alpha_wave = 0.01   # Transporte por ondas
alpha_tide = 0.005  # Transporte por maré
beta = 0.001        # Coeficiente não-linear

# Perfil de praia inicial baseado em dados reais
def initialize_beach_profile(X, Y, Lx, Ly):
    h = np.zeros_like(X)
    
    # Perfil de praia típico (face, berma, pós-praia)
    h += 0.5 * (1 - np.tanh((X - 0.7*Lx)/50))  # Face da praia
    h += 0.2 * np.exp(-((X - 0.8*Lx)/30)**2)    # Berma
    
    # Elementos geológicos específicos
    h += 0.4 * np.exp(-((X - Lx/4)/80)**2 - ((Y - Ly/2)/60)**2)  # Formação rochosa sul
    h += 0.3 * np.exp(-((X - 3*Lx/4)/100)**2 - ((Y - Ly/3)/70)**2)  # Formação rochosa norte
    h -= 0.3 * np.exp(-((X - Lx/2)/120)**2 - ((Y - 2*Ly/3)/80)**2)  # Canal de escoamento
        
    return h

# Fluxo de sedimentos aprimorado
def compute_sediment_flux(h, dx, dy, alpha_wave, alpha_tide, beta):
    slope_x, slope_y = np.gradient(h, dx, dy)
    
    # Transporte linear (ondas e marés)
    Q_sx = -alpha_wave * slope_x - alpha_tide * slope_x
    Q_sy = -alpha_wave * slope_y - alpha_tide * slope_y
    
    # Termo não-linear (transporte intenso em altas inclinações)
    slope_mag = np.sqrt(slope_x**2 + slope_y**2)
    Q_sx -= beta * slope_x * slope_mag
    Q_sy -= beta * slope_y * slope_mag
    
    return Q_sx, Q_sy

# Atualização da topografia com termos adicionais
def update_topography(h, Q_sx, Q_sy, dx, dy, dt, D):
    # Conservação de massa
    dQs_dx = np.gradient(Q_sx, dx, axis=1)
    dQs_dy = np.gradient(Q_sy, dy, axis=0)
    dh_dt = -(dQs_dx + dQs_dy)
    
    # Difusão
    lap_h = np.gradient(np.gradient(h, dx, axis=1), dx, axis=1) + np.gradient(np.gradient(h, dy, axis=0), dy, axis=0)
    dh_dt += D * lap_h
    
    # Atualização
    h += dh_dt * dt
    
    # Condição de contorno (sedimentos não saem do domínio)
   # h = np.clip(h, -2, 2)  # Limites físicos
    
    return h

# Inicialização
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)
h = initialize_beach_profile(X, Y, Lx, Ly)

# Visualização
fig, ax = plt.subplots(figsize=(12, 6))
img = ax.imshow(h, extent=[0, Lx, 0, Ly], origin='lower', 
               cmap='gist_earth', vmin=-0.5, vmax=1.0)
plt.colorbar(img, label='Elevação (m)')
plt.title('Simulação Morfodinâmica - Praia do Cepilho (Trindade, RJ)')
plt.xlabel('Distância ao Longo da Costa (m)')
plt.ylabel('Distância para o Mar (m)')

# Animação
def update(frame):
    global h
    Q_sx, Q_sy = compute_sediment_flux(h, dx, dy, alpha_wave, alpha_tide, beta)
    h = update_topography(h, Q_sx, Q_sy, dx, dy, dt, D)
    
    # Adicionando variação de maré periódica
    tide = 0.2 * np.sin(2*np.pi*frame/12)  # Ciclo de 12 horas
    h[:, :10] += tide * dt/3600 * 0.01  # Afetando a zona de arrebentação
    
    img.set_array(h)
    return img,

ani = FuncAnimation(fig, update, frames=T, interval=100, blit=True)
plt.show()


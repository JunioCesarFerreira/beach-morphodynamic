# Modelos de Evolução Morfodinâmica para Praias

A evolução morfodinâmica de uma praia pode ser modelada por equações diferenciais parciais (EDPs) que descrevem o transporte de sedimentos, a hidrodinâmica das ondas e marés, e as interações entre os processos costeiros. O modelo geral deve capturar três elementos essenciais:  

1. **Equação da Continuidade para Sedimentos**  
2. **Equação de Transporte de Sedimentos**  
3. **Equação da Hidrodinâmica Costeira (Shallow Water Equations - SWEs)**  

---

## 1. Equação da Continuidade para Sedimentos

A conservação da massa de sedimentos é descrita por:

$$
\frac{\partial h}{\partial t} + \nabla \cdot \mathbf{Q_s} = S
$$

onde:  

- $h: \mathbb{R}^2 \times \mathbb{R}^+ \to \mathbb{R}$  
  - $h(x,y,t)$ representa a altura do fundo marinho em relação a um nível de referência.  
  - Domínio: $(x,y) \in \Omega \subset \mathbb{R}^2$, $t \in \mathbb{R}^+$.  
  - Contradomínio: $h(x,y,t) \in \mathbb{R}$ (altura da topografia submersa).  

- $\mathbf{Q_s}: \mathbb{R}^2 \times \mathbb{R}^+ \to \mathbb{R}^2$  
  - $\mathbf{Q_s} = (Q_{sx}, Q_{sy})$ é o vetor de fluxo volumétrico de sedimentos.  
  - Domínio: $(x,y) \in \Omega \subset \mathbb{R}^2$, $t \in \mathbb{R}^+$.  
  - Contradomínio: $Q_{sx}, Q_{sy} \in \mathbb{R}$ (fluxo de sedimentos por unidade de tempo).  

- $S: \mathbb{R}^2 \times \mathbb{R}^+ \to \mathbb{R}$  
  - $S(x,y,t)$ representa fontes ou sumidouros de sedimentos devido a erosão e deposição.  
  - Domínio: $(x,y) \in \Omega \subset \mathbb{R}^2$, $t \in \mathbb{R}^+$.  
  - Contradomínio: $S(x,y,t) \in \mathbb{R}$ (taxa líquida de erosão ou deposição).  

  ---

  ## 2. Equação de Transporte de Sedimentos  

A equação de transporte de sedimentos inclui advecção e difusão:

$$
\frac{\partial C}{\partial t} + \nabla \cdot (C \mathbf{u}) = \nabla \cdot (D \nabla C) + S_s
$$

onde:

- $C: \mathbb{R}^2 \times \mathbb{R}^+ \to \mathbb{R}$  
  - $C(x,y,t)$ é a concentração volumétrica de sedimentos em suspensão.  
  - Domínio: $(x,y) \in \Omega \subset \mathbb{R}^2$, $t \in \mathbb{R}^+$.  
  - Contradomínio: $C(x,y,t) \in \mathbb{R}^+$ (fração de volume de sedimentos por unidade de volume de água).  

- $\mathbf{u}: \mathbb{R}^2 \times \mathbb{R}^+ \to \mathbb{R}^2$  
  - $\mathbf{u} = (u,v)$ é o vetor velocidade das correntes costeiras.  
  - Domínio: $(x,y) \in \Omega \subset \mathbb{R}^2$, $t \in \mathbb{R}^+$.  
  - Contradomínio: $u, v \in \mathbb{R}$ (velocidade da água em $m/s$).  

- $D: \mathbb{R}^2 \times \mathbb{R}^+ \to \mathbb{R}^+$  
  - $D(x,y,t)$ é o coeficiente de difusão turbulenta.  
  - Domínio: $(x,y) \in \Omega \subset \mathbb{R}^2$, $t \in \mathbb{R}^+$.  
  - Contradomínio: $D(x,y,t) \in \mathbb{R}^+$ (coeficiente de difusão em $m^2/s$).  

- $S_s: \mathbb{R}^2 \times \mathbb{R}^+ \to \mathbb{R}$  
  - $S_s(x,y,t)$ representa fontes ou sumidouros de sedimentos devido à ressuspensão e deposição.  
  - Domínio: $(x,y) \in \Omega \subset \mathbb{R}^2$, $t \in \mathbb{R}^+$.  
  - Contradomínio: $S_s(x,y,t) \in \mathbb{R}$.  

  ---

  ## 3. Equações Hidrodinâmicas Costeiras (Shallow Water Equations - SWEs)

As equações da hidrodinâmica costeira são:

$$
\frac{\partial \eta}{\partial t} + \nabla \cdot [(H+\eta) \mathbf{u}] = 0
$$

$$
\frac{\partial \mathbf{u}}{\partial t} + \mathbf{u} \cdot \nabla \mathbf{u} + g \nabla \eta + \frac{\tau_b}{\rho} = 0
$$

onde:

- $\eta: \mathbb{R}^2 \times \mathbb{R}^+ \to \mathbb{R}$  
  - $\eta(x,y,t)$ é a elevação da superfície da água.  
  - Domínio: $(x,y) \in \Omega \subset \mathbb{R}^2$, $t \in \mathbb{R}^+$.  
  - Contradomínio: $\eta(x,y,t) \in \mathbb{R}$ (altura da água em relação ao nível médio).  

- $H: \mathbb{R}^2 \to \mathbb{R}^+$  
  - $H(x,y)$ é a profundidade média do fundo oceânico.  
  - Domínio: $(x,y) \in \Omega \subset \mathbb{R}^2$.  
  - Contradomínio: $H(x,y) \in \mathbb{R}^+$.  

- $g \in \mathbb{R}^+$  
  - Aceleração gravitacional ($g \approx 9.81 \, m/s^2$).  

- $\tau_b: \mathbb{R}^2 \times \mathbb{R}^+ \to \mathbb{R}$  
  - $\tau_b(x,y,t)$ é a tensão de cisalhamento do fundo.  
  - Contradomínio: $\tau_b(x,y,t) \in \mathbb{R}$.  

- $\rho \in \mathbb{R}^+$  
  - Densidade da água.  

  ---
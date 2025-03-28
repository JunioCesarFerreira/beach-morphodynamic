# beach-morphodynamics

A evolução morfodinâmica de uma praia pode ser modelada por equações diferenciais parciais (EDPs) que descrevem o transporte de sedimentos, a hidrodinâmica das ondas e marés, e as interações entre os processos costeiros. O modelo geral deve capturar três elementos essenciais:  

1. **Equação da Continuidade para Sedimentos**  
2. **Equação de Transporte de Sedimentos**  
3. **Equação da Hidrodinâmica Costeira (Shallow Water Equations)**  

---

## 1. Equação da Continuidade para Sedimentos
O balanço de massa dos sedimentos pode ser expresso como:  

$$
\frac{\partial h}{\partial t} + \nabla \cdot \mathbf{Q_s} = S
$$

onde:  
- $h(x,y,t)$ é a elevação do fundo em relação a um nível de referência.  
- $\mathbf{Q_s} = (Q_{sx}, Q_{sy})$ é o fluxo volumétrico de sedimentos.  
- $S(x,y,t)$ representa fontes ou sumidouros de sedimentos (por exemplo, erosão ou deposição).  

Essa equação expressa a conservação de massa dos sedimentos ao longo do tempo, considerando a taxa de transporte ($\mathbf{Q_s}$) e a deposição/erosão ($S$).  

---

## 2. Equação de Transporte de Sedimentos  
O fluxo de sedimentos pode ser modelado pela equação de advecção-difusão:

$$
\frac{\partial C}{\partial t} + \nabla \cdot (C \mathbf{u}) = \nabla \cdot (D \nabla C) + S_s
$$

onde:  
- $C(x,y,t)$ é a concentração volumétrica de sedimentos em suspensão.  
- $\mathbf{u} = (u,v)$ é o campo de velocidade da corrente.  
- $D(x,y,t)$ é o coeficiente de difusão turbulenta.  
- $S_s(x,y,t)$ representa fontes ou sumidouros de sedimentos devido à ressuspensão e deposição.  

Esse modelo representa o transporte de sedimentos por advecção e difusão, levando em conta a influência de correntes costeiras e dispersão turbulenta.  

---

## 3. Equações Hidrodinâmicas Costeiras (Shallow Water Equations - SWEs)
A evolução da superfície da água e das correntes litorâneas é governada pelas equações de águas rasas:

$$
\frac{\partial \eta}{\partial t} + \nabla \cdot [(H+\eta) \mathbf{u}] = 0
$$

$$
\frac{\partial \mathbf{u}}{\partial t} + \mathbf{u} \cdot \nabla \mathbf{u} + g \nabla \eta + \frac{\tau_b}{\rho} = 0
$$

onde:  
- $\eta(x,y,t)$ é a elevação da superfície livre da água.  
- $H(x,y)$ é a profundidade média do fundo oceânico.  
- $g$ é a aceleração gravitacional.  
- $\tau_b$ é o atrito no fundo.  
- $\rho$ é a densidade da água.  

Essas equações descrevem a interação entre o nível da água, as correntes e a topografia costeira.  

---

## Acoplamento das Equações
O modelo completo combina as três equações anteriores de forma acoplada:  
1. A hidrodinâmica costeira (equações de águas rasas) define $\mathbf{u}$.  
2. O transporte de sedimentos depende de $\mathbf{u}$ e influencia a topografia do fundo $h$.  
3. A evolução do fundo oceânico afeta a hidrodinâmica, criando um sistema retroalimentado.

O acoplamento é resolvido numericamente via métodos como diferenças finitas, volumes finitos ou elementos finitos.

---

## Aplicações e Simulações
Esse modelo pode ser aplicado para:
- **Previsão de erosão costeira** causada por tempestades ou marés altas.  
- **Impacto de obras marítimas** (molhes, quebra-mares) na redistribuição de sedimentos.  
- **Evolução de bancos de areia e dunas costeiras**.  

A resolução numérica dessas equações é desafiadora, exigindo esquemas estáveis para lidar com as não-linearidades e acoplamentos. Métodos como esquemas de volumes finitos em malhas não estruturadas são comuns para simulações realistas.  

Esse modelo fornece um quadro teórico poderoso para entender a dinâmica das praias e sua evolução sob influência das ondas, correntes e marés.

Simulações e mais delhes em [src](./src/).

---


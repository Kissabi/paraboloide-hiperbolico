import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

x = np.arange(-5, 5, 0.25) # pontos do eixo x
y = np.arange(-5, 5, 0.25) # pontos do eixo y

x1, y1 = np.meshgrid(x, y) # cria uma grade retangular
z = x1**2 - y1**2 # pontos do eixo z

fig = plt.figure()
ax = fig.gca(projection='3d') # plota uma projeção 3D
surf = ax.plot_surface(x1, y1, z, # conjunto de matrizes 2Ds
rstride=2, # tamanho da linha
cstride=2, # tamanho da coluna
cmap=cm.Wistia, # cor de mapeamento
linewidth=1, # largura da linha
antialiased=True)

ax.set_title('Parabolóide Hiberbólico') # título
ax.set_xlabel('Eixo X') # eixo X
ax.set_ylabel('Eixo Y') # eixo Y
ax.set_zlabel('Eixo Z') # eixo Z
fig.colorbar(surf, shrink=0.5, aspect=5) # cor da barra
ax.view_init(elev=30,azim=70) # elevação e ângulo
ax.dist=8 # distância dos eixos
plt.show()

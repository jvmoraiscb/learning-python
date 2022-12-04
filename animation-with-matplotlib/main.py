# Autores: João Victor Morais e Talles Cavalleiro Weiler

# Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  
from matplotlib import animation, rc

# Definição do objeto
class Object():
    def __init__(self, points = [], center = []):
        self.center = center
        self.points = points

# Função de translação
def trans3D(dx,dy,dz):
  T3D = np.array([[1, 0, 0, dx],[0, 1, 0, dy],[0, 0, 1, dz], [0, 0, 0, 1]])
  return T3D

# Função de escala
def scale3D(sx,sy,sz):
  S3D = np.array([[sx, 0, 0, 0],[0, sy, 0, 0],[0, 0, sz, 0], [0, 0, 0, 1]])
  return S3D

# Função de rotação
def rot3D(angle,axis):
  ang_rad = (angle/180)*np.pi
  if axis == 'z':
    R3D = np.array([[np.cos(ang_rad),-np.sin(ang_rad),0,0],[np.sin(ang_rad),np.cos(ang_rad),0,0],[0,0,1,0],[0,0,0,1]])
  elif axis == 'x':
    R3D = np.array([[1,0,0,0],[0,np.cos(ang_rad),-np.sin(ang_rad),0],[0,np.sin(ang_rad),np.cos(ang_rad),0],[0,0,0,1]])
  elif axis == 'y':
    R3D = np.array([[np.cos(ang_rad),0,np.sin(ang_rad),0],[0,1,0,0],[-np.sin(ang_rad),0,np.cos(ang_rad),0],[0,0,0,1]])
  else:
    R3D = np.eye(4,4)
  return R3D


#Criando vetor das posicoes do fiat uno
uno_array = np.array([
  [0, 0, 0],
  [2.9740, 0, 0],
  [2.9740, 2, 0],
  [2.9740, 2, 1],
  [2.9740, 2, -1],
  [2.9740, 2, 1],
  [6.9740, 2, 1],
  [6.9740, 2, -1],
  [6.9740, 2, 1],
  [6.9740, -2, 1],
  [6.9740, -2, -1],
  [6.9740, -2, 1],
  [2.9740, -2, 1],
  [2.9740, -2, -1],
  [2.9740, -2, 1],
  [2.9740, 2, 1],
  [2.9740, 2, -1],
  [6.9740, 2, -1],
  [6.9740, -2, -1],
  [2.9740, -2, -1],
  [2.9740, 2, -1],
  [2.9740, 2, 0],
  [2.9740, 0, 0],
  [2.9740, 2, 0],
  [6.9740, 2, 0],
  [6.9740, 0, 0],
  [18.1378, 0, 0],
  [18.1378, 2, 0],
  [18.1378, 2, 1],
  [18.1378, 2, -1],
  [18.1378, 2, 1],
  [22.1378, 2, 1],
  [22.1378, 2, -1],
  [22.1378, 2, 1],
  [22.1378, -2, 1],
  [22.1378, -2, -1],
  [22.1378, -2, 1],
  [18.1378, -2, 1],
  [18.1378, -2, -1],
  [18.1378, -2, 1],
  [18.1378, 2, 1],
  [18.1378, 2, -1],
  [22.1378, 2, -1],
  [22.1378, -2, -1],
  [18.1378, -2, -1],
  [18.1378, 2, -1],
  [18.1378, 2, 0],
  [18.1378, 0, 0],
  [18.1378, 2, 0],
  [22.1378, 2, 0],
  [22.1378, 0, 0],
  [24.9122, 0, 0],
  [22.1378, 0, 0],
  [22.1378, 2, 0],
  [18.1378, 2, 0],
  [18.1378, 0, 0],
  [6.9740, 0, 0],
  [6.9740, 2, 0],
  [2.9740, 2, 0],
  [2.9740, 0, 0],
  [0, 0, 0],
  [0, 0, 10],
  [2.9740, 0, 10],
  [2.9740, 2, 10],
  [2.9740, 2, 11],
  [2.9740, 2, 9],
  [2.9740, 2, 11],
  [6.9740, 2, 11],
  [6.9740, 2, 9],
  [6.9740, 2, 11],
  [6.9740, -2, 11],
  [6.9740, -2, 9],
  [6.9740, -2, 11],
  [2.9740, -2, 11],
  [2.9740, -2, 9],
  [2.9740, -2, 11],
  [2.9740, 2, 11],
  [2.9740, 2, 9],
  [6.9740, 2, 9],
  [6.9740, -2, 9],
  [2.9740, -2, 9],
  [2.9740, 2, 9],
  [2.9740, 2, 10],
  [2.9740, 0, 10],
  [2.9740, 2, 10],
  [6.9740, 2, 10],
  [6.9740, 0, 10],
  [18.1378, 0, 10],
  [18.1378, 2, 10],
  [18.1378, 2, 11],
  [18.1378, 2, 9],
  [18.1378, 2, 11],
  [22.1378, 2, 11],
  [22.1378, 2, 9],
  [22.1378, 2, 11],
  [22.1378, -2, 11],
  [22.1378, -2, 9],
  [22.1378, -2, 11],
  [18.1378, -2, 11],
  [18.1378, -2, 9],
  [18.1378, -2, 11],
  [18.1378, 2, 11],
  [18.1378, 2, 9],
  [22.1378, 2, 9],
  [22.1378, -2, 9],
  [18.1378, -2, 9],
  [18.1378, 2, 9],
  [18.1378, 2, 10],
  [18.1378, 0, 10],
  [18.1378, 2, 10],
  [22.1378, 2, 10],
  [22.1378, 0, 10],
  [24.9122, 0, 10],
  [24.9122, 0, 0],
  [24.9122, 5, 0],
  [0, 5, 0],
  [0, 0, 0],
  [0, 5, 0],
  [0, 5, 10],
  [0, 0, 10],
  [0, 5, 10],
  [24.9122, 5, 10],
  [24.9122, 0, 10],
  [24.9122, 5, 10],
  [24.9122, 5, 0],
  [21.9122, 10, 0],
  [15.9122, 10, 0],
  [15.9122, 5, 0],
  [15.9122, 10, 0],
  [9.9122, 10, 0],
  [6.5086, 5, 0],
  [6.5086, 5, 10],
  [6.5086, 5, 0],
  [9.9122, 10, 0],
  [9.9122, 10, 10],
  [6.5086, 5, 10],
  [9.9122, 10, 10],
  [15.9122, 10, 10],
  [15.9122, 5, 10],
  [15.9122, 10, 10],
  [21.9122, 10, 10],
  [24.9122, 5, 10],
  [21.9122, 10, 10],
  [21.9122, 10, 0]        
])

#Criando vetor das posicoes do caminhão
truck_array = np.array([
  [0, 0, 0],
  [3.2471, 0, 0],
  [3.2471, 2, 0],
  [3.2471, 2, 1],
  [3.2471, 2, -1],
  [3.2471, 2, 1],
  [7.2471, 2, 1],
  [7.2471, 2, -1],
  [7.2471, 2, 1],
  [7.2471, -2, 1],
  [7.2471, -2, -1],
  [7.2471, -2, 1],
  [3.2471, -2, 1],
  [3.2471, -2, -1],
  [3.2471, -2, 1],
  [3.2471, 2, 1],
  [3.2471, 2, -1],
  [7.2471, 2, -1],
  [7.2471, -2, -1],
  [3.2471, -2, -1],
  [3.2471, 2, -1],
  [3.2471, 2, 0],
  [3.2471, 0, 0],
  [3.2471, 2, 0],
  [7.2471, 2, 0],
  [7.2471, 0, 0],
  [13.7225, 0, 0],
  [13.7225, 2, 0],
  [13.7225, 2, 1],
  [13.7225, 2, -1],
  [13.7225, 2, 1],
  [17.7225, 2, 1],
  [17.7225, 2, -1],
  [17.7225, 2, 1],
  [17.7225, -2, 1],
  [17.7225, -2, -1],
  [17.7225, -2, 1],
  [13.7225, -2, 1],
  [13.7225, -2, -1],
  [13.7225, -2, 1],
  [13.7225, 2, 1],
  [13.7225, 2, -1],
  [17.7225, 2, -1],
  [17.7225, -2, -1],
  [13.7225, -2, -1],
  [13.7225, 2, -1],
  [13.7225, 2, 0],
  [13.7225, 0, 0],
  [13.7225, 2, 0],
  [17.7225, 2, 0],
  [17.7225, 0, 0],
  [19.7262, 0, 0],
  [19.7262, 2, 0],
  [19.7262, 2, 1],
  [19.7262, 2, -1],
  [19.7262, 2, 1],
  [23.7262, 2, 1],
  [23.7262, 2, -1],
  [23.7262, 2, 1],
  [23.7262, -2, 1],
  [23.7262, -2, -1],
  [23.7262, -2, 1],
  [19.7262, -2, 1],
  [19.7262, -2, -1],
  [19.7262, -2, 1],
  [19.7262, 2, 1],
  [19.7262, 2, -1],
  [23.7262, 2, -1],
  [23.7262, -2, -1],
  [19.7262, -2, -1],
  [19.7262, 2, -1],
  [19.7262, 2, 0],
  [19.7262, 0, 0],
  [19.7262, 2, 0],
  [23.7262, 2, 0],
  [23.7262, 0, 0],
  [29.6990, 0, 0],
  [29.6990, 2, 0],
  [29.6990, 2, 1],
  [29.6990, 2, -1],
  [29.6990, 2, 1],
  [33.6990, 2, 1],
  [33.6990, 2, -1],
  [33.6990, 2, 1],
  [33.6990, -2, 1],
  [33.6990, -2, -1],
  [33.6990, -2, 1],
  [29.6990, -2, 1],
  [29.6990, -2, -1],
  [29.6990, -2, 1],
  [29.6990, 2, 1],
  [29.6990, 2, -1],
  [33.6990, 2, -1],
  [33.6990, -2, -1],
  [29.6990, -2, -1],
  [29.6990, 2, -1],
  [29.6990, 2, 0],
  [29.6990, 0, 0],
  [29.6990, 2, 0],
  [33.6990, 2, 0],
  [33.6990, 0, 0],
  [35.5359, 0, 0],
  [35.5359, 2, 0],
  [35.5359, 2, 1],
  [35.5359, 2, -1],
  [35.5359, 2, 1],
  [39.5359, 2, 1],
  [39.5359, 2, -1],
  [39.5359, 2, 1],
  [39.5359, -2, 1],
  [39.5359, -2, -1],
  [39.5359, -2, 1],
  [35.5359, -2, 1],
  [35.5359, -2, -1],
  [35.5359, -2, 1],
  [35.5359, 2, 1],
  [35.5359, 2, -1],
  [39.5359, 2, -1],
  [39.5359, -2, -1],
  [35.5359, -2, -1],
  [35.5359, 2, -1],
  [35.5359, 2, 0],
  [35.5359, 0, 0],
  [35.5359, 2, 0],
  [39.5359, 2, 0],
  [39.5359, 0, 0],
  [43.0000, 0, 0],
  [39.5359, 0, 0],
  [39.5359, 2, 0],
  [35.5359, 2, 0],
  [35.5359, 0, 0],
  [33.6990, 0, 0],
  [33.6990, 2, 0],
  [29.6990, 2, 0],
  [29.6990, 0, 0],
  [23.7262, 0, 0],
  [23.7262, 2, 0],
  [19.7262, 2, 0],
  [19.7262, 0, 0],
  [17.7225, 0, 0],
  [17.7225, 2, 0],
  [13.7225, 2, 0],
  [13.7225, 0, 0],
  [7.2471, 0, 0],
  [7.2471, 2, 0],
  [3.2471, 2, 0],
  [3.2471, 0, 0],
  [0, 0, 0],
  [0, 0, 15],
  [3.2471, 0, 15],
  [3.2471, 2, 15],
  [3.2471, 2, 16],
  [3.2471, 2, 14],
  [3.2471, 2, 16],
  [7.2471, 2, 16],
  [7.2471, 2, 14],
  [7.2471, 2, 16],
  [7.2471, -2, 16],
  [7.2471, -2, 14],
  [7.2471, -2, 16],
  [3.2471, -2, 16],
  [3.2471, -2, 14],
  [3.2471, -2, 16],
  [3.2471, 2, 16],
  [3.2471, 2, 14],
  [7.2471, 2, 14],
  [7.2471, -2, 14],
  [3.2471, -2, 14],
  [3.2471, 2, 14],
  [3.2471, 2, 15],
  [3.2471, 0, 15],
  [3.2471, 2, 15],
  [7.2471, 2, 15],
  [7.2471, 0, 15],
  [13.7225, 0, 15],
  [13.7225, 2, 15],
  [13.7225, 2, 16],
  [13.7225, 2, 14],
  [13.7225, 2, 16],
  [17.7225, 2, 16],
  [17.7225, 2, 14],
  [17.7225, 2, 16],
  [17.7225, -2, 16],
  [17.7225, -2, 14],
  [17.7225, -2, 16],
  [13.7225, -2, 16],
  [13.7225, -2, 14],
  [13.7225, -2, 16],
  [13.7225, 2, 16],
  [13.7225, 2, 14],
  [17.7225, 2, 14],
  [17.7225, -2, 14],
  [13.7225, -2, 14],
  [13.7225, 2, 14],
  [13.7225, 2, 15],
  [13.7225, 0, 15],
  [13.7225, 2, 15],
  [17.7225, 2, 15],
  [17.7225, 0, 15],
  [19.7262, 0, 15],
  [19.7262, 2, 15],
  [19.7262, 2, 16],
  [19.7262, 2, 14],
  [19.7262, 2, 16],
  [23.7262, 2, 16],
  [23.7262, 2, 14],
  [23.7262, 2, 16],
  [23.7262, -2, 16],
  [23.7262, -2, 14],
  [23.7262, -2, 16],
  [19.7262, -2, 16],
  [19.7262, -2, 14],
  [19.7262, -2, 16],
  [19.7262, 2, 16],
  [19.7262, 2, 14],
  [23.7262, 2, 14],
  [23.7262, -2, 14],
  [19.7262, -2, 14],
  [19.7262, 2, 14],
  [19.7262, 2, 15],
  [19.7262, 0, 15],
  [19.7262, 2, 15],
  [23.7262, 2, 15],
  [23.7262, 0, 15],
  [29.6990, 0, 15],
  [29.6990, 2, 15],
  [29.6990, 2, 16],
  [29.6990, 2, 14],
  [29.6990, 2, 16],
  [33.6990, 2, 16],
  [33.6990, 2, 14],
  [33.6990, 2, 16],
  [33.6990, -2, 16],
  [33.6990, -2, 14],
  [33.6990, -2, 16],
  [29.6990, -2, 16],
  [29.6990, -2, 14],
  [29.6990, -2, 16],
  [29.6990, 2, 16],
  [29.6990, 2, 14],
  [33.6990, 2, 14],
  [33.6990, -2, 14],
  [29.6990, -2, 14],
  [29.6990, 2, 14],
  [29.6990, 2, 15],
  [29.6990, 0, 15],
  [29.6990, 2, 15],
  [33.6990, 2, 15],
  [33.6990, 0, 15],
  [35.5359, 0, 15],
  [35.5359, 2, 15],
  [35.5359, 2, 16],
  [35.5359, 2, 14],
  [35.5359, 2, 16],
  [39.5359, 2, 16],
  [39.5359, 2, 14],
  [39.5359, 2, 16],
  [39.5359, -2, 16],
  [39.5359, -2, 14],
  [39.5359, -2, 16],
  [35.5359, -2, 16],
  [35.5359, -2, 14],
  [35.5359, -2, 16],
  [35.5359, 2, 16],
  [35.5359, 2, 14],
  [39.5359, 2, 14],
  [39.5359, -2, 14],
  [35.5359, -2, 14],
  [35.5359, 2, 14],
  [35.5359, 2, 15],
  [35.5359, 0, 15],
  [35.5359, 2, 15],
  [39.5359, 2, 15],
  [39.5359, 0, 15],
  [43.0000, 0, 15],
  [43.0000, 0, 0],
  [43.0000, 4, 0],
  [13.0000, 4, 0],
  [13.0000, 4, 15],
  [43.0000, 4, 15],
  [43.0000, 0, 15],
  [43.0000, 4, 15],
  [43.0000, 4, 0],
  [43.0000, 15, 0],
  [13.0000, 15, 0],
  [13.0000, 4, 0],
  [13.0000, 15, 0],
  [13.0000, 15, 15],
  [13.0000, 4, 15],
  [13.0000, 15, 15],
  [43.0000, 15, 15],
  [43.0000, 4, 15],
  [43.0000, 15, 15],
  [43.0000, 15, 0],
  [43.0000, 4, 0],
  [10.0000, 4, 0],
  [10.0000, 4, 15],
  [13.0000, 4, 15],
  [13.0000, 4, 0],
  [10.0000, 4, 0],
  [10.0000, 12, 0],
  [0, 12, 0],
  [0, 0, 0],
  [0, 12, 0],
  [0, 12, 15],
  [0, 0, 15],
  [0, 12, 15],
  [10.0000, 12, 15],
  [10.0000, 4, 15],
  [10.0000, 12, 15],
  [10.0000, 12, 0],
  [10.0000, 4, 0],
  [3.0000, 4, 0],
  [3.0000, 12, 0],
  [3.0000, 4, 0],
  [0, 4, 0],
  [0, 4, 15],
  [3.0000, 4, 15],
  [3.0000, 12, 15],
  [3.0000, 4, 15],
  [10.0000, 4, 15],
])

# Tornando a matriz do uno e do caminhão possíveis de serem alteradas pelas funções (escala, rotação e translação)
uno_array = np.transpose(uno_array)
num_columns = np.size(uno_array,1)
ones_line = np.ones(num_columns)

uno_array = np.vstack([uno_array, ones_line])
uno_object = Object(uno_array,[12.4561, 4, 5, 1])
# Aumentando o uno
uno_object.points=trans3D(uno_object.center[0],uno_object.center[1],uno_object.center[2]) @ scale3D(2.5,2.5,2.5) @ trans3D(-uno_object.center[0],-uno_object.center[1],-uno_object.center[2]) @ uno_object.points
uno_object.center=trans3D(uno_object.center[0],uno_object.center[1],uno_object.center[2]) @ scale3D(2.5,2.5,2.5) @ trans3D(-uno_object.center[0],-uno_object.center[1],-uno_object.center[2]) @ uno_object.center

truck_array = np.transpose(truck_array)
num_columns = np.size(truck_array,1)
ones_line = np.ones(num_columns)

truck_array = np.vstack([truck_array, ones_line])
truck_object = Object(truck_array,[12.4561, 4, 5, 1])
# Aumentando o caminhão
truck_object.points=trans3D(truck_object.center[0],truck_object.center[1],truck_object.center[2]) @ scale3D(2.5,2.5,2.5) @ trans3D(-truck_object.center[0],-truck_object.center[1],-truck_object.center[2]) @ truck_object.points
truck_object.center=trans3D(truck_object.center[0],truck_object.center[1],truck_object.center[2]) @ scale3D(2.5,2.5,2.5) @ trans3D(-truck_object.center[0],-truck_object.center[1],-truck_object.center[2]) @ truck_object.center

# Definindo a figura e os eixos
fig = plt.figure(figsize=(10,10))
ax0 = plt.axes(projection='3d')
plt.close()

# Definindo os limites do gráfico
ax0.set_xlim3d((-100, 100))
ax0.set_ylim3d((-100, 100))
ax0.set_zlim3d((-20, 100))

# Listando os objetos que serão utilizados (uno e caminhão)
Uno, = ax0.plot3D([], [], [], lw=2,color='#410002' )
Truck, = ax0.plot3D([], [], [], lw=2,color='#011E09' )  

# Função de inicialização: 
def init():
  T=trans3D(uno_object.center[0],uno_object.center[1],uno_object.center[2]) @ rot3D(45,'x') @ trans3D(-uno_object.center[0],-uno_object.center[1],-uno_object.center[2])
  uno_object.points = T @ uno_object.points
  uno_object.center = T @ uno_object.center
  Uno.set_data(uno_object.points[0,:], uno_object.points[1,:])
  Uno.set_3d_properties(uno_object.points[2,:])

  T=trans3D(100, 30, 0)
  uno_object.points = T @ uno_object.points
  uno_object.center = T @ uno_object.center
  Uno.set_data(uno_object.points[0,:], uno_object.points[1,:])
  Uno.set_3d_properties(uno_object.points[2,:])

  T=trans3D(truck_object.center[0],truck_object.center[1],truck_object.center[2]) @ rot3D(45,'x') @ trans3D(-truck_object.center[0],-truck_object.center[1],-truck_object.center[2])
  truck_object.points = T @ truck_object.points
  truck_object.center = T @ truck_object.center
  Truck.set_data(truck_object.points[0,:], truck_object.points[1,:])
  Truck.set_3d_properties(truck_object.points[2,:])

  T=trans3D(-140, -60, 0)
  truck_object.points = T @ truck_object.points
  truck_object.center = T @ truck_object.center
  Truck.set_data(truck_object.points[0,:], truck_object.points[1,:])
  Truck.set_3d_properties(truck_object.points[2,:])

  return (Uno, Truck,)
    
# Função que roda a animação (o valor de 'i' equivale ao frame atual)
def animate(i):
  # Uno se aproxima do centro
  if i <15:
    T=trans3D(-2*i, 0, 0)

    uno_object.points = T @ uno_object.points
    uno_object.center = T @ uno_object.center
    Uno.set_data(uno_object.points[0,:], uno_object.points[1,:])
    Uno.set_3d_properties(uno_object.points[2,:])

  # Uno rotaciona 90 graus, o caminhão também rotaciona (mas em segredo)
  elif i < 20 :
    T=trans3D(uno_object.center[0],uno_object.center[1],uno_object.center[2]) @ rot3D(18,'z') @ trans3D(-uno_object.center[0],-uno_object.center[1],-uno_object.center[2])
    uno_object.points = T @ uno_object.points
    uno_object.center = T @ uno_object.center
    Uno.set_data(uno_object.points[0,:], uno_object.points[1,:])
    Uno.set_3d_properties(uno_object.points[2,:])

    T=trans3D(truck_object.center[0],truck_object.center[1],truck_object.center[2]) @ rot3D(36,'z') @ trans3D(-truck_object.center[0],-truck_object.center[1],-truck_object.center[2])
    truck_object.points = T @ truck_object.points
    truck_object.center = T @ truck_object.center
    Truck.set_data(truck_object.points[0,:], truck_object.points[1,:])
    Truck.set_3d_properties(truck_object.points[2,:])

  # Uno se aproxima do caminhão por 'y', enquanto o caminhão se aproxima do uno em 'x' (se aproximam em função de 'i', para que seja perceptível a aceleração)
  elif i < 25:
    T=trans3D(0, -1.5*i, 0)
    uno_object.points = T @ uno_object.points
    uno_object.center = T @ uno_object.center
    Uno.set_data(uno_object.points[0,:], uno_object.points[1,:])
    Uno.set_3d_properties(uno_object.points[2,:])

    T=trans3D(2*i, 0, 0)

    truck_object.points = T @ truck_object.points
    truck_object.center = T @ truck_object.center
    Truck.set_data(truck_object.points[0,:], truck_object.points[1,:])
    Truck.set_3d_properties(truck_object.points[2,:])

  # Segue uma série de movimentos
  elif i < 35:
    # Uno recebe a batida e se afasta um pouco
    if i < 30:
      T=trans3D(0.8*i, 0, 0)
      uno_object.points = T @ uno_object.points
      uno_object.center = T @ uno_object.center
      Uno.set_data(uno_object.points[0,:], uno_object.points[1,:])
      Uno.set_3d_properties(uno_object.points[2,:])

    # Caminhão perde grande parte da velocidade, mas avança um pequeno trecho antes de parar completamente
    if i < 28:
      T=trans3D(0.2*i, 0, 0)
      truck_object.points = T @ truck_object.points
      truck_object.center = T @ truck_object.center
      Truck.set_data(truck_object.points[0,:], truck_object.points[1,:])
      Truck.set_3d_properties(truck_object.points[2,:])
      # Caminhao balanca um pouco devido a batida
      if i % 2:
        T=trans3D(truck_object.center[0],truck_object.center[1],truck_object.center[2]) @ rot3D(2,'y') @ trans3D(-truck_object.center[0],-truck_object.center[1],-truck_object.center[2])
        truck_object.points = T @ truck_object.points
        truck_object.center = T @ truck_object.center
        Truck.set_data(truck_object.points[0,:], truck_object.points[1,:])
        Truck.set_3d_properties(truck_object.points[2,:])
      else:
        T=trans3D(truck_object.center[0],truck_object.center[1],truck_object.center[2]) @ rot3D(-2,'y') @ trans3D(-truck_object.center[0],-truck_object.center[1],-truck_object.center[2])
        truck_object.points = T @ truck_object.points
        truck_object.center = T @ truck_object.center
        Truck.set_data(truck_object.points[0,:], truck_object.points[1,:])
        Truck.set_3d_properties(truck_object.points[2,:])
    
    # Uno rotaciona bastante devido a batida
    if i < 30:
      T=trans3D(uno_object.center[0],uno_object.center[1],uno_object.center[2]) @ rot3D(54,'y') @ trans3D(-uno_object.center[0],-uno_object.center[1],-uno_object.center[2])
      uno_object.points = T @ uno_object.points
      uno_object.center = T @ uno_object.center
      Uno.set_data(uno_object.points[0,:], uno_object.points[1,:])
      Uno.set_3d_properties(uno_object.points[2,:])
  # Após um momento, o caminhão acelera
  elif i > 40:
    T=trans3D(10, 0, 0)
    truck_object.points = T @ truck_object.points
    truck_object.center = T @ truck_object.center
    Truck.set_data(truck_object.points[0,:], truck_object.points[1,:])
    Truck.set_3d_properties(truck_object.points[2,:])

    # Quando o caminhão encosta no carro, ele o empurra
    if i > 50:
      T=trans3D(10, 0, 0)
      uno_object.points = T @ uno_object.points
      uno_object.center = T @ uno_object.center
      Uno.set_data(uno_object.points[0,:], uno_object.points[1,:])
      Uno.set_3d_properties(uno_object.points[2,:])
  
  return (Uno, Truck,)

# Faz a animação
anim = animation.FuncAnimation(fig, animate, init_func=init,
                             frames=70, interval=100, blit=True)

# Note: below is the part which makes it work on Colab
rc('animation', html='jshtml')
anim

#Save video in mp4 format
#f = r"./sample_data/animation.mp4" 
#writervideo = animation.FFMpegWriter(fps=30) 
#anim.save(f, writer=writervideo)
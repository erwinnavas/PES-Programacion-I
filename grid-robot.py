#!/usr/bin/env python
# coding: utf-8

# ### Programa de Estudios Superiores 2019-2020
# ### Programación I - proyecto final
# #### Elaborado por <span class="alert alert-info"> ***Erwin Roberto Navas Solis*** </span><br>
# ***
# ***Instrucciones generales:*** resuelve el siguiente problema de acuerdo a la especificación dada. 
# - El código debe ir comentado para explicar la lógica y debe ser totalmente funcional para ser considerado correcto. De lo contrario, la calificación podrá ser subjetiva.
# - Al final de la definición de la clase, obtenga una instancia y muestra que el objeto se comporta de acuerdo a las especificaciones deseadas, para poder calificarte más rápidamente.
# ***

# # *Drunken robot*
# 
# Considere un robot que sigue una caminata aleatoria dentro de una cuadícula unidimensional, como se muestra a continuación. En cada período, el robot se mueve aleatoriamente hacia la izquierda o hacia la derecha (siempre y cuando sea posible), para ocupar una casilla diferente. Cuando el robot ocupa una casilla, esta casilla se marca de color amarillo.  
# 
# ![grid-robot.png](attachment:grid-robot.png)
# 
# Un amigo suyo, economista, cree que este proceso estocástico puede ayudarle a entender un problema de reversión a la media de una serie de tiempo con la que está teniendo problemas recientemente, por lo que le interesa el problema de este robot. Para esto, su amigo necesita entender cuántos períodos le puede tomar a este robot marcar toda la cuadrícula de color amarillo. Entonces, le ha pedido ayuda a usted para que le ayude con algunas simulaciones.
# 
# Usted ha llevado recientemente un curso de programación y pretende resolver este problema a través de la implementación de una clase de Python. 
# 
# ## Descripción de la clase
# 
# Usted va a implementar la simulación a través de la clase `DrunkenRobot` de la siguiente forma:
# 
# - Al crear un objeto de esta clase, el constructor debe recibir la cantidad $n$ de casillas para crear la cuadrícula y posicionará al robot en una de estas casillas de forma aleatoria.
# 
# Además, deberá implementar los siguientes métodos:
# 
# - Método `takeStep` que lleve a cabo un paso del robot y marque la nueva casilla como visitada. El robot debe llevar un registro de todos los pasos que ha tomado y en qué período lo ha hecho.
# 
# - `conquerAll` que utilice el método `takeStep` para mover el robot hasta visitar toda la cuadrícula.
# 
# - `plotSteps` que haga una gráfica de la posición del robot (número de casilla) en cada período. Debe llamarse posterior a la ejecución de `conquerAll`.
#     - Deberá agregar una opción booleana `savePlot` para escoger si guardar la gráfica en un formato de alta calidad.
# 
# - `getTrajectory` que devolverá un `DataFrame` de pandas con la posición del robot en cada período. Debe llamarse posterior a la ejecución de `conquerAll`.
# 
# - **Extra**: `getCumulativeTrajectory` que devolverá un `DataFrame` de pandas con el número de casillas visitadas en cada período.

# <div class="alert alert-info">
# <b>Importe los paquetes que sean necesarios</b>: <br>
# 
# 
# </div>

# In[2]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import random


# <div class="alert alert-info">
# <b>Escriba su código en la celda siguiente</b>: <br>
# 
# 
# </div>

# In[7]:


class DrunkenRobot:
    ''' 
        Recibe la cantidad de casillas n de la cuadrícula y 
        posiciona aleatoriamente al robot.
    '''
    
    
    def __init__(self, n):
        '''
        Lleva a cabo un paso del robot y marca la nueva casilla 
        como visitada. El robot debe llevar un registro de todos
        los pasos que ha tomado y en qué período lo ha hecho.
        '''
        
        inicio=np.array([[0]])
        self.pasos = np.random.normal(0,1,(1,n-1))
        self.steps = np.ravel(pasos.pasos)
        self.x=np.concatenate((inicio, np.cumsum(steps, axis=0)),axis=0)
        self.plot=plt.plot(x[:],"ro-")
    
    def takeStep(self):
        '''
            Utiliza el método `takeStep` para mover el robot hasta 
            visitar toda la cuadrícula.
        '''
        return self.x
        
    def conquerAll(self):
        pass
    
        '''
            Realiza una gráfica de la posición del robot (número de casilla)
            en cada período. La opción booleana `savePlot` permite
            escoger si guardar la gráfica en un formato de alta calidad.
        '''
        return self.plot
        
    def plotSteps(self, savePlot=False):
        pass
    
    '''
        Devuelve un `DataFrame` de pandas con la posición del 
        robot en cada período.
    '''
    def getTrajectory(self):
        pass
    
    '''
        EXTRA.
        Devuelve un `DataFrame` de pandas con el número de 
        casillas visitadas en cada período.
    '''
    def getCumulativeTrajectory(self):
        pass


# ***
# ## Área de pruebas personal
# 
# Utilice el siguiente espacio para llevar a cabo **sus** pruebas.
# 

# In[9]:


n=10
inicio=np.array([0])
pasos = np.random.normal(0,1,(1,n-1))
steps = np.ravel(pasos)
x=np.concatenate((inicio, np.cumsum(steps, axis=0)),axis=0)
plot=plt.plot(x[:],"ro-")


# In[10]:


df=pd.DataFrame({"x" : x})
df


# In[ ]:


contar=df["x"].count
contar


# In[ ]:





# In[ ]:





# ***
# ## Área de pruebas para calificación
# 
# Utilice el siguiente espacio para mostrarnos su implementación terminada.

# <div class="alert alert-info">
# <b>Pruebe el método "takeStep"</b>: <br>
# </div>

# In[8]:


Robot=DrunkenRobot(10)
Robot.x


# <div class="alert alert-info">
# <b>Pruebe el método "conquerAll"</b>: <br>
# </div>

# In[ ]:





# <div class="alert alert-info">
# <b>Pruebe el método "plotSteps"</b>: <br>
# </div>

# In[ ]:





# <div class="alert alert-info">
# <b>Pruebe el método "getTrajectory"</b>: <br>
# </div>

# In[ ]:





# <div class="alert alert-info">
# <b>Muestre cada uno de los atribujos del objeto utilizado en el ejemplo</b>: <br>
# </div>

# In[ ]:





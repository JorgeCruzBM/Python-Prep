#!/usr/bin/env python
# coding: utf-8

# ## Iteradores e iterables

# 1) A partir de una lista vacía, utilizar un ciclo while para cargar allí números negativos del -15 al -1

# In[1]:
minus = list()
num = -15
while (num < 0):
    minus.append(nun)
    num += 1
print(minus)


# 2) ¿Con un ciclo while sería posible recorrer la lista para imprimir sólo los números pares?

# In[3]:
{n=0
while (n<16):
    if minus[n]%2==0:
        NLpair.append(minus[n])
        n+=1
    else:
        n+=1
print (NLpair)}
#El código entre llaves no puede ser ejecutado correctamente. Tengo un error «list index out of range» pero mi while condiciona todo al n<16. Aún así, he comprobado que mi lista NLpair si adquiere los números pares de
#la lista minus. Lo he comprobado con una siguiente línea de código:

print (NLpair)
NLpair = list()

#Coloqué y retiré un numeral al principio de uno de los dos para reiniciar los valores de la lista, ejecutar el código con error en el índice y luego imprimir los valores de la lista. Estos son los valores:
[-14, -12, -10, -8, -6, -4, -2]


# 3) Resolver el punto anterior sin utilizar un ciclo while

# In[4]:
for elemento in minus:
    if elemento % 2 == 0:
        NLpair.append(elemento)




# 4) Utilizar el iterable para recorrer sólo los primeros 3 elementos

# In[7]:
for elemento in minus[:3]:
  print (elemento)



# 5) Utilizar la función **enumerate** para obtener dentro del iterable, tambien el índice al que corresponde el elemento

# In[9]:
for elemento, klave in enumerate(minus)
  print (elemento, klave)



# 6) Dada la siguiente lista de números enteros entre 1 y 20, crear un ciclo donde se completen los valores faltantes: lista = [1,2,5,7,8,10,13,14,15,17,20]

# In[10]:
n=0
while n<20:
    if lista[n]==n+1:
        n+=1
    else:
        lista.insert(n,n+1)
  
n+=1


# In[11]:


n = 1



# 7) La sucesión de Fibonacci es un listado de números que sigue la fórmula: <br>
# n<sub>0</sub> = 0<br>
# n<sub>1</sub> = 1<br>
# n<sub>i</sub> = n<sub>i-1</sub> + n<sub>i-2</sub><br>
# Crear una lista con los primeros treinta números de la sucesión.<br>

# In[23]:





# 8) Realizar la suma de todos elementos de la lista del punto anterior

# In[24]:




# 9) La proporción aurea se expresa con una proporción matemática que nace el número irracional Phi= 1,618… que los griegos llamaron número áureo. El cuál se puede aproximar con la sucesión de Fibonacci. Con la lista del ejercicio anterior, imprimir el cociente de los últimos 5 pares de dos números contiguos:<br>
# Donde i es la cantidad total de elementos<br>
# n<sub>i-1</sub> / n<sub>i</sub><br>
# n<sub>i-2</sub> / n<sub>i-1</sub><br>
# n<sub>i-3</sub> / n<sub>i-2</sub><br>
# n<sub>i-4</sub> / n<sub>i-3</sub><br>
# n<sub>i-5</sub> / n<sub>i-4</sub><br>
#  

# In[38]:




# 10) A partir de la variable cadena ya dada, mostrar en qué posiciones aparece la letra "n"<br>
# cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

# In[39]:





# 11) Crear un diccionario e imprimir sus claves utilizando un iterador

# In[40]:





# 12) Convertir en una lista la variable "cadena" del punto 10 y luego recorrerla con un iterador 

# In[41]:





# In[45]:





# 13) Crear dos listas y unirlas en una tupla utilizando la función zip

# In[48]:





# 14) A partir de la siguiente lista de números, crear una nueva sólo si el número es divisible por 7<br>
# lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]

# In[49]:





# 15) A partir de la lista de a continuación, contar la cantidad total de elementos que contiene, teniendo en cuenta que un elemento de la lista podría ser otra lista:<br>
# lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

# In[56]:




# In[51]:





# In[57]:





# 16) Tomar la lista del punto anterior y convertir cada elemento en una lista si no lo es

# In[58]:




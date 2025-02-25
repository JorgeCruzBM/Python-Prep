#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:
WC = ["Monaco", "Dublin", "San Cristobal", "Ottawa", "Comitan", "Pujiltik"]
print (WC)



# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:
print (WC[1])



# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:
print (WC[1:3])




# 4) Visualizar el tipo de dato de la lista

# In[12]:
type(WC)




# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:
print (WC[2:])




# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:
print (WC[:3])


    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:
"Si, por el elemento repetido








# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:
WC.insert(2, "Konohagakure")




# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:

Nar= ["Kamartaj", "Kirigakure", "Marisma Criminal"]
NL = WC + Nar

# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:

#No se agregó



# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:
#Error de sintaxis




# 12) Eliminar un elemento de la lista

# In[25]:
WC.pop()




# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:

Erro



# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:
LE=WC.pop()
print (LE)



# 15) Mostrar la lista multiplicada por 4

# In[29]:
print (WC*4)



# 16) Crear una tupla que contenga los números enteros del 1 al 20

# In[32]:
NE=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)



# 17) Imprimir desde el índice 10 al 15 de la tupla

# In[35]:
print (NE[10:15])



# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:
20 in NE
30 in NE



# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[48]:
if "Paris" in WC:
    print ("Paris is already in WC")
   
else:
	print ("Paris wasn't found in WC. Paris is going to be added")
	WC.append("Paris")
    

print (WC)


# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:
	NE.count(15)
WC.count("Paris")


# 21) Convertir la tupla en una lista

# In[52]:

list(NE)



# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:
Prim, Seg, Ter= NE[:3]




# 23) Crear un diccionario utilizando la lista crada en el punto 1, asignandole la clave "ciudad". Agregar tambien otras claves, como puede ser "Pais" y "Continente".

# In[57]:
dicc=dict()
dicc["Ciudad"]= WC
dicc[57]=
dicc[5opper]




# 24) Imprimir las claves del diccionario

# In[59]:

dicc.keys()


# 25) Imprimir las ciudades a través de su clave

# In[61]:
print (dicc[Ciudad])




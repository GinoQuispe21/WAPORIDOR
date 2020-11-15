import random


#Esta funcion retorna un valor entre 0 a 1 (incluidos decimales)
#ergo, existe una probabilidad igual de que retorne cualquier posible valor entre 0 y 1
#Sin embargo, nosotros podemos utilizar esa igualdad de probabilidad para definir limites/cotas de decision
#osea ifs
#Ejemplo:


my_id = 0 #Azul 0 1 2 3

#Un random en el caso de 4 players
my_rival_id = 1 #Verde
#Pos rival
posx = 2
posy = 8

#Player 0
#mat[0]

#Player 1
#mat[1]

#Player 2
#mat[0]

#Player 3
#mat[1]

mat = [
    [0.8,0.8,0.8,0.5,0.5,0.5,0.2,0.2,0.2],
    [0.2,0.2,0.2,0.5,0.5,0.5,0.8,0.8,0.8],
]

index = 0
posi = 0

if (my_rival_id % 2 == 0): #Azul Amarillo
    index = 1
else: #Verde Rosado
    index = 0

if(my_rival_id == 0 or my_rival_id == 1): #Azul Verde
    posi = posx
else: #Amarillo Rosado
    posi = posy

mat[index][posi//2]
cont1 = 0
cont2 = 0
for i in range(100):
    val = random.random() #0 y 1
    if(val < mat[index][posi//2]):
        print("Poner pared")
        cont1+=1
    else:
        print("Avanzar")
        cont2+=1
print(cont1)
print(cont2)
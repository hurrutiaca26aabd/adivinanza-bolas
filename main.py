import bola
import random
import balanza

# Hegoiren ariketa

bolas = [bola.Bola(1) for _ in range(8)]
posicion_aleatoria = random.randint(0,8)
bolas.insert(posicion_aleatoria, bola.Bola(1.1))  # Bola más pesada

balanza = balanza.Balanza()

bolaPisutxuena = 0

i = 0

emaitza = balanza.pesar(bolas[:3], bolas[3:6])

if emaitza == 1:
    emaitza = balanza.pesar([bolas[0]], [bolas[1]])

    if emaitza == 1:
        bolaPisutxuena = 0
    elif emaitza == -1:
        bolaPisutxuena = 1
    else:
        bolaPisutxuena = 2

elif emaitza == -1:
    emaitza = balanza.pesar([bolas[3]], [bolas[4]])

    if emaitza == 1:
        bolaPisutxuena = 3
    elif emaitza == -1:
        bolaPisutxuena = 4
    else:
        bolaPisutxuena = 5

else:
    emaitza = balanza.pesar([bolas[6]], [bolas[7]])
    
    if emaitza == 1:
        bolaPisutxuena = 6
    elif emaitza == -1:
        bolaPisutxuena = 7
    else:
        bolaPisutxuena = 8


print(balanza.emaitza(bolas[bolaPisutxuena]))

#print(balanza.pesar(bolas[:4], bolas[4:8]))  # Compara las primeras 4 bolas con las últimas 4
#print(balanza.emaitza(bolas[4]))  # Muestra el resultado de la comparación
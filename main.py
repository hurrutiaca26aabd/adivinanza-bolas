import bola
import random
import balanza

# Hegoiren ariketa

bolas = [bola.Bola(1) for _ in range(8)]
posicion_aleatoria = random.randint(0,8)
bolas.insert(posicion_aleatoria, bola.Bola(1.1))  # Bola más pesada

balanza = balanza.Balanza()

print(balanza.pesar(bolas[:4], bolas[4:8]))  # Compara las primeras 4 bolas con las últimas 4

print(balanza.emaitza(bolas[4]))  # Muestra el resultado de la comparación
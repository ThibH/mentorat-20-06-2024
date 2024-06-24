# Création d'un grand dictionnaire
import time

large_dict = {i: i**2 for i in range(1000000)}

# Mesure du temps d'accès à une valeur
start_time = time.time()
value = large_dict[999999]
end_time = time.time()
print(f"Valeur : {value}, Temps d'accès : {end_time - start_time} secondes")

# Ajout d'une nouvelle paire clé-valeur
start_time = time.time()
large_dict[1000000] = 1000000**2
end_time = time.time()
print(f"Temps d'insertion : {end_time - start_time} secondes")

# Suppression d'une paire clé-valeur
start_time = time.time()
del large_dict[500000]
end_time = time.time()
print(f"Temps de suppression : {end_time - start_time} secondes")


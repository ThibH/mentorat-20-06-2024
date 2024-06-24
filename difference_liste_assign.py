liste = [1, 2, 3]
seq = [4, 5, 6]

# Initial ID de la liste
print("ID initial de la liste :", id(liste))

# Utilisation de liste = liste + seq
liste = liste + seq
print("Après liste = liste + seq :", liste)
print("ID après liste = liste + seq :", id(liste))  # L'ID change

# Réinitialisation de la liste
liste = [1, 2, 3]

# Initial ID de la liste
print("ID initial de la liste :", id(liste))

# Utilisation de liste += seq
liste += seq
print("Après liste += seq :", liste)
print("ID après liste += seq :", id(liste))  # L'ID reste le même


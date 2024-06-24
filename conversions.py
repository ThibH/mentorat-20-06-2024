# Conversion avec int()
try:
    num = int("123abc")
except ValueError as e:
    print(f"Erreur de conversion: {e}")

# Conversion avec float()
try:
    flt = float("123.45.67")
except ValueError as e:
    print(f"Erreur de conversion: {e}")

# Conversion avec list()
try:
    lst = list("4853242")
except TypeError as e:
    print(f"Erreur de conversion: {e}")

# Conversion avec dict()
try:
    d = dict([('a', 1), ('b', 2), ([1], 3)])
except TypeError as e:
    print(f"Erreur de conversion: {e}")

# Pour les dictionnaires, explication de l'erreur avec les hash.
x = 42
print(hash(x))  # Output: un entier (valeur de hachage)

y = 3.14
print(hash(y))  # Output: un entier (valeur de hachage)

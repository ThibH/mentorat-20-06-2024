import sys

# Création d'un objet
a = []


def foo(arg):
    print(id(arg))
    print(sys.getrefcount(arg))  # Output: 3 (2 + l'argument de getrefcount)


print(id(a))
foo(arg=a)


def change_liste(arg):
    b = arg + " tout le monde"
    print(b)


b = "Bonjour"
change_liste(arg=b)
print(b)  # Output: [1]

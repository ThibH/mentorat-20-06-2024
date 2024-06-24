# Conversion de types
num_str = "123"
num_int = int(num_str)
print(num_int)  # Output: 123

# 👉 Attention, il faut bien créer une nouvelle variable pour stocker la conversion
num_str = "123"
print(type(num_str))  # Output: <class 'str'>

# Vérification de type
print(isinstance(num_int, int))  # Output: True
print(isinstance(num_str, str))  # Output: True

"""
Fonction type()
La fonction type() est utilisée pour obtenir le type exact d'un objet.
Elle retourne l'objet de type de l'objet passé en argument.
"""

x = 5
print(type(x))  # Output: <class 'int'>

y = "hello"
print(type(y))  # Output: <class 'str'>

"""
Fonction isinstance()
La fonction isinstance() est utilisée pour vérifier si un objet est une instance d'une classe ou d'une sous-classe de celle-ci.
Elle prend deux arguments : l'objet et la classe (ou un tuple de classes) à vérifier.
"""

x = 5
print(isinstance(x, int))  # Output: True

y = "hello"
print(isinstance(y, str))  # Output: True

"""
Utilisez type() lorsque vous avez besoin de vérifier que l'objet est d'un type précis et uniquement ce type.
"""


def check_type(obj):
    if type(obj) is int:
        print("L'objet est un entier")
    elif type(obj) is str:
        print("L'objet est une chaîne de caractères")
    else:
        print("L'objet est d'un autre type")


check_type(10)  # Output: L'objet est un entier
check_type("hello")  # Output: L'objet est une chaîne de caractères

"""
Vérification de l'Instance ou de la Sous-classe :
Utilisez isinstance() lorsque vous avez besoin de vérifier que l'objet est une instance d'une classe
ou d'une sous-classe de celle-ci.
"""


class Animal:
    pass


class Dog(Animal):
    pass


dog = Dog()

print(isinstance(dog, Dog))  # Output: True
print(isinstance(dog, Animal))  # Output: True
print(type(dog) is Animal)  # Output: False

"""
Vérification Multiple :
isinstance() peut également vérifier si un objet appartient à l'un des types dans un tuple de types.
"""


def check_instance(obj):
    if isinstance(obj, (int, float)):
        print("L'objet est un nombre (int ou float)")
    else:
        print("L'objet n'est pas un nombre")


check_instance(10)  # Output: L'objet est un nombre (int ou float)
check_instance(10.5)  # Output: L'objet est un nombre (int ou float)
check_instance("hello")  # Output: L'objet n'est pas un nombre

"""
Pourquoi Utiliser l'Un ou l'Autre
Utilisez type() :

- Lorsque vous devez vérifier le type exact d'un objet sans tenir compte des sous-classes.
- Pour des vérifications précises où les sous-classes ne sont pas pertinentes.

Utilisez isinstance() :

- Lorsque vous devez vérifier si un objet est une instance d'une classe ou d'une sous-classe.
- Lorsque vous travaillez avec une hiérarchie de classes et que vous souhaitez inclure les instances des sous-classes.
- Pour des vérifications de types multiples à l'aide de tuples.
"""

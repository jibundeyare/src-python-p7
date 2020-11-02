# dictionnaire / dictionary
# tableau associatif / associative array
# hash map
# couple clé / valeur
my_dict = {}

my_dict = {
    'foo': 42,
    'bar': 3.14,
    'baz': True,
    'lorem': 'lorem ipsum',
    True: 'lorem ipsum',
    True: 'sit dolores',
    False: 'foo bar baz',
    42: 'un int',
    3.14: 'un float',
    None: 'un none',
    (): 'un tuple',
}

print(my_dict)

# valeurs possibles pour une clé :
# - numérique
# - alpha numérique == alphabet + nombre + autre caractères
# - valeur booléenne
# - None
# - tuple

# ajouter un nouveau couple clé / valeur
my_dict['ipsum'] = 'lorem ipsum'
print(my_dict)

# modifier la valeur associée à une clé existante
my_dict['lorem'] = 'sit dolores'
print(my_dict)

# supprimer un couple clé / valeur
del(my_dict['ipsum'])
print(my_dict)

# afficher les clés
for key in my_dict:
    print(key)

# afficher les valeurs
for key in my_dict:
    print(my_dict[key])

# afficher les clés et les valeurs
for key in my_dict:
    print(f"{key}: {my_dict[key]}")

# afficher les clés et les valeurs
# méthode alternative
for key, value in my_dict.items():
    print(f"{key}: {value}")

# récupérer la liste des clés
my_keys = list(my_dict.keys())
print(my_keys)

# récupérer la liste des valeurs
my_values = list(my_dict.values())
print(my_values)

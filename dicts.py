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

my_dict['ipsum'] = 'lorem ipsum'
print(my_dict)

my_dict['lorem'] = 'sit dolores'
print(my_dict)

del(my_dict['ipsum'])
print(my_dict)

for key in my_dict:
    print(key)

for key in my_dict:
    print(my_dict[key])

for key in my_dict:
    print(f"{key}: {my_dict[key]}")

for key, value in my_dict.items():
    print(f"{key}: {value}")

my_keys = list(my_dict.keys())
print(my_keys)

my_values = list(my_dict.values())
print(my_values)

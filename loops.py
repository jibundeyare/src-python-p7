# while
# for
# foreach

# boucle infinie
# while True:
#     print('foo')

# boucle qui affiche les nombres de 0 à 9
i = 0

while i < 10:
    print(i)
    i += 1

# boucle qui affiche les nombres de 100 à 1
i = 100

while i > 0:
    print(i)
    i -= 1

# boucle qui affiche les nombres de 0 à 9
for i in range(0, 10):
    print(i)

print()

# boucle qui répête 5 fois une action
i = 0

while i < 5:
    print('foo')
    i += 1

print()

# boucle qui répête 5 fois une action
for i in range(0, 5):
    print('foo')

print()

# boucle qui n'affiche que les nombres plus grands ou égaux à 5
for i in range(0, 10):
    if i >= 5:
        print(i)

# tous les endroit où on peut rajouter du code
print('foo')

for i in range(0, 10):
    print('bar')

    if i < 5:
        print('baz')
        # indique de « ne rien faire »
        pass
        print('lorem')

    print('ipsum')

print('sic')

# indique de « ne rien faire »
# pass

# interrompt une boucle
# break

for i in range(0, 100):
    print(i)
    if i == 42:
        break

number = 0
while True:
    number += 10
    if number > 100:
        break

# passe à l'étape suivante
# continue

for i in range(0, 100):
    if i != 42:
        continue

    print(i)

number = 42

if number % 2 == 0:
    print(f"le nombre {number} est pair")

# une boucle avec un pas de 2
for i in range(0, 100, 2):
    print(i)
    print(i + 1)

# itération
# (récursion)

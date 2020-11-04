import random

# 4.1
def foo():
    """Affiche la chaîne de caractères 'foo' dans le terminal"""
    print('foo')

# 4.4 (en réalité 4.5)
my_text = """foo. lorem.
bar. ipsum.
baz"""

print(len(my_text.split('.')))
print(len(my_text.split('\n')))

# 6.10
# compléxité algorithmique
# O(c)
# O(n)
# O(2n - 1)
# (42 + 123 + 3.14) / 3 == 42 / 3 + 123 / 3 + 3.14 / 3

# startTimer

# for i in range(1000000):
#     my_list = [42, 123, 3.14]
#     avg = 0

#     for value in my_list:
#         avg += value

#     # avg = avg / len(my_list)
#     avg /= len(my_list)
#     print(avg)

# stopTimer
# printTimer

# 6.13
my_list = [42, 123, 3.14]

for i in range(0, len(my_list)):
    # my_list[i] = my_list[i] * 100
    my_list[i] *= 100
    print(my_list[i])


# 6.15
my_list = ['a', 'b', 'c', 'd']

for i in range(0, 4):
    print(i)

print()

for i in range(0, 4, 2):
    print(my_list[i])
    print(my_list[i + 1])

# 6.16
my_list = [123, 42, 3.14]

# - loop = False
# - 123 > 42 == true:
#     loop = True
#     inverser 123 et 42
# - 123 > 3.14 == true:
#     loop = True
#     inverser 123 et 3.14
# - if loop:
#     on repart depuis le début
# - loop = False
# - 42 > 3.14 == true:
#     loop = True
#     inverser 42 et 3.14
# - 42 > 123 == false:
#     on ne fait rien
# - if loop:
#     on repart depuis le début
# - loop = False
# - 3.14 > 42 == false:
#     on ne fait rien
# - 42 > 123 == false:
#     on ne fait rien
# - if loop:
#     on repart depuis le début

while True:
    loop = False

    for i in range(0, len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            loop = True
            my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i] 

    if not loop:
        break

print(my_list)

# 6.18
size = 3
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# lignes
for i in range(0, size):
    # colonnes
    for j in range(0, size):
        print(i, j, matrix[i][j])

# 7.18
while True:
    r = random.randint(0, 100)

    if r == 100:
        print('ok')
        break

# f-string
foo = 123 * 100
print(f"foo: {foo}")

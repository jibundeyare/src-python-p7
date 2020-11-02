# liste == tableau
# list == array

my_list = []
my_list2 = [42, 123, 2, 3.14]

my_list = list()
# pas autorisé !
# my_list2 = list(42, 123, 2, 3.14)

# len == length
print(len(my_list))
print(len(my_list2))

print(my_list2[0])
# l'index du dernier élément = longueur du tableau - 1
print(my_list2[len(my_list2) - 1])

my_list2[0] = 'foo'
print(my_list2)

# [42, 123, 2, 3.14]
tmp = my_list2[1]
my_list2[1] = my_list2[2]
my_list2[2] = tmp
print(my_list2)

# destructured assignment == affectation destructurée
my_list2[1], my_list2[2] = my_list2[2], my_list2[1]
print(my_list2)

del(my_list2[0])
print(my_list2)

my_list2.append(2.71)
print(my_list2)

my_list2 += [1.61, 456, 789]
# même chose que
# my_list2 = my_list2 + [1.61, 456, 789]
print(my_list2)

my_list2.insert(3, 'foo')
print(my_list2)

# foreach
for value in my_list2:
    print(value)

print()

# foreach
for value in my_list2:
    if type(value) is not str:
        print(value * 100)

for i, value in enumerate(my_list2):
    print(i, value)

for i in range(0, len(my_list2)):
    print(i, my_list2[i])

# PHP
# for ($i = 0; $i < count($my_list); $i++) {
#     echo $i.' '.$my_list[$i];
# }

for i, value in enumerate(my_list2):
    # on peut utiliser `is not` ou `!=` comme opérateur
    if type(value) != str:
        my_list2[i] = value * 100
        print(i, my_list2[i])

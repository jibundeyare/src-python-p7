# définition
def my_function1():
    pass

# appel
my_function1()

def my_function2():
    print('foo')

my_function2()

def my_function3(my_list):
    sum = 0

    for value in my_list:
        sum += value

    return sum / len(my_list)

my_data = [123, 42, 3.14]
print(my_data)

average = my_function3(my_data)
print(average)

my_data = [123, 42, 3.14, 2.71]

average = my_function3(my_data)
print(average)

# liste des paramètres et type hinting + le type de données renvoyé == signature d'une fonction
# le type hinting est optionnel
def my_function4(my_list: list) -> float:
    sum = 0

    for value in my_list:
        sum += value

    return sum / len(my_list)

# sans type hinting
# def function5(a, b):
# avec type hinting
def function5(a: float, b: float) -> float:
    return a * b

print(function5(3.14, 2.71))

my_data = [1, 2, 3]

# en python, les variables sont passées « par référence » aux fonctions
# en php, les variables sont passées « par valeur » (c-à-d une copie des données) aux fonctions
def function6(my_list: list):
    if len(my_list) != 0:
        my_list[len(my_list) - 1] = 'foo'

print(my_data)
function6(my_data)
print(my_data)

my_data = [1, 2, 3]

def function7(my_list: list):
    # création d'une copie de la variable originale
    _my_list = my_list.copy()
    if len(_my_list) != 0:
        _my_list[len(_my_list) - 1] = 'foo'
    
    return _my_list

print(my_data)
my_data_copy = function7(my_data)
print(my_data)
print(my_data_copy)

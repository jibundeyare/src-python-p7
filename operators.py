foo = 123

foo = 123 + 456
foo = 123 - 456
foo = 123 * 4
foo = 10 / 3
print(foo)
foo = 10 // 3
print(foo)
# modulo : le reste de la division
# 10 = 3 * 3 + 1
foo = 10 % 3
print(foo)

foo = 2 % 2
print(foo)
foo = 256 % 2
print(foo)
foo = 3 % 2
print(foo)

# 2 ** 3 == 2 * 2 * 2
foo = 2 ** 3
print(foo)

foo = (123 + 2) * 456

a = 123
b = 456

print(a < b)
print(a <= b)
print(a > b)
print(a >= b)
print(a == b)
print(a != b)

# n'existe pas en python mais valide dans d'autres langages
# a = 123
# b = '123'
# a === b
# a !== b
# a <== b
# a >== b

# incrémenter
c = 0
c = c + 1
# n'existe pas en python mais valide dans d'autres langages
# c++
c += 1

# décrémenter
c = c - 1
# n'existe pas en python mais valide dans d'autres langages
# c--
c -= 1

c *= 2
c /= 2

foo = "lorem ipsum"
# foo = ["l", "o", "r", "e", "m", " ", ...]
print("m" in foo)
print("a" in foo)

fruits = ["ananas", "banane", "cerise"]
print("banane" in fruits)
print("cassis" in fruits)

my_numeric1 = 123
print(type(my_numeric1) is int)
print(type(my_numeric1) is float)
print(type(my_numeric1) is str)
print(type(my_numeric1) is bool)

# opérateur de concaténation
print("Vous avez reçu " + str(mails) + " mails")

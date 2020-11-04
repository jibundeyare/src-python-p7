# scope global
my_var1 = 123

# scope global
print(my_var1)

if True:
    # du scope local on voit le scope global
    print(my_var1)

    # scope local d'un if
    my_var2 = 456

    # on voit les variables en provenance du même scope
    print(my_var2)

# du scope global on voit le scope local d'un if
print(my_var2)

for i in range(0, 10):
    # du scope local on voit le scope global
    print(my_var1)

    # scope local d'un for
    my_var3 = 789

    # on voit les variables en provenance du même scope
    print(my_var3)

# du scope global on voit le scope local d'un for
print(my_var3)

def my_function():
    # vrai en python : du scope local on voit le scope global
    # mais faux en php !
    print(my_var1)

    # scope local d'une fonction
    my_var4 = 963

    # on voit les variables en provenance du même scope
    print(my_var4)

my_function()

# du scope global on ne voit pas le scope local d'une fonction
# provoque l'erreur : name 'my_var4' is not defined
# print(my_var4)

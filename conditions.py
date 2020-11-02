import random

morning = True

if morning:
    print("c'est le matin")
else:
    print("ce n'est pas le matin")

product_quantity = random.randint(0, 5)
print(product_quantity)

if product_quantity == 0:
    print("rupture de stock")
elif product_quantity == 1:
    print("il reste 1 produit")
else:
    print(f"il reste {product_quantity} produits")

electricity_off = True
water_off = True
# partir en vacances : True

electricity_off = False
water_off = True
# partir en vacances : False

electricity_off = True
water_off = False
# partir en vacances : False

electricity_off = False
water_off = False
# partir en vacances : False

# table de vérité de l'opérateur ET logique
# A       B       A and B
# True    True    True
# False   True    False
# True    False   False
# False   False   False

electricity_off = bool(random.randint(0, 1)) 
water_off = bool(random.randint(0, 1)) 

print(electricity_off)
print(water_off)

if electricity_off and water_off:
    print("vous pouvez partir en vacances")
else:
    print("vous ne pouvez pas partir en vacances")

# table de vérité de l'opérateur de négation
# A     not A
# True  False
# False True

if electricity_off and water_off:
    print("vous pouvez partir en vacances")
elif not electricity_off and water_off:
    print("il faut éteindre l'électricité")
elif electricity_off and not water_off:
    print("il faut couper l'eau")
else:
    print("il faut éteindre l'électricité et couper l'eau")

has_bank_card = True
has_cash = True
# partir faire les courses : True

has_bank_card = False
has_cash = True
# partir faire les courses : True

has_bank_card = True
has_cash = False
# partir faire les courses : True

has_bank_card = False
has_cash = False
# partir faire les courses : False

# table de vérité de l'opérateur OU logique
# A       B       A or B
# True    True    True
# False   True    True
# True    False   True
# False   False   False

has_bank_card = bool(random.randint(0, 1))
has_cash = bool(random.randint(0, 1))
print(has_bank_card)
print(has_cash)

if has_bank_card or has_cash:
    print("vous pouvez partir faire les courses")
else:
    print("vous ne pouvez pas partir faire les courses")

if has_bank_card and has_cash:
    print("vous avez une carte bancaire et du cash")
elif has_bank_card:
    print("vous avez une carte bancaire")
elif has_cash:
    print("vous avez de cash")
else:
    print("vous ne pouvez pas partir faire les courses")

number = random.randint(0, 100)

# vérifier qu'un nombre est compris entre 25 et 75 inclus
if 25 <= number and number <= 75:
    print("le nombre est compris entre 25 et 75 inclus")
else:
    print("le nombre n'est pas compris entre 25 et 75 inclus")

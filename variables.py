my_number1 = 123
my_number2 = 3.14
my_text1 = "foo bar baz"
my_boolean1 = True
my_boolean2 = False
my_null_value = None

print(my_number1)
print(my_number2)
print(my_text1)
print(my_boolean1)
print(my_boolean2)
print(my_null_value)

my_number1 = 2.7182
print(my_number1)

my_text2 = "<h1>an html title</h1>"
print(my_text2)

my_text3 = "texte\nsur\nplusieurs\nlignes"
print(my_text3)

my_text4 = "dwayne \"the rock\" johnson"
my_text5 = "this is a backslash \\n"
print(my_text4)
print(my_text5)

my_text6 = 'lorem ipsum'
my_text7 = 'dwayne "the rock" johnson'
my_text8 = "dwayne 'the rock' johnson"
print(my_text6)
print(my_text7)
print(my_text8)

my_text9 = """texte
"sur"
'plusieurs'
lignes"""
print(my_text9)

print(type(my_number1))
print(type(my_number2))
print(type(my_text1))
print(type(my_boolean1))
print(type(my_boolean2))
print(type(my_null_value))

my_number3 = int(my_number2)
my_text2 = '123'
my_number4 = int(my_text2)
my_text3 = '123.45'
my_number5 = float(my_text3)
my_text10 = str(my_number1)
my_text11 = str(my_boolean1)

print(bool(0))
print(bool(1))
print(bool(-1))
print(bool(3.14))
print(bool(""))
print(bool("foo bar baz"))
print(bool(None))
print(bool([]))
print(bool([1, 2, 3]))

# provoque l'erreur : TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
# print(int(None))
# provoque l'erreur : TypeError: float() argument must be a string or a number, not 'NoneType'
# print(float(None))

a = 123
b = 456
print(a, b)

tmp = a
a = b
b = tmp
print(a, b)

a, b = b, a
print(a, b)

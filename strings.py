my_string = "lorem\nipsum"
my_string = 'lorem\nipsum'
# string heredoc
my_string = """lorem ipsum
sic dolores
amet bla bla bla
"""
my_string = '''lorem ipsum
sic dolores
amet bla bla bla
'''

print(len(my_string))
position = my_string.find('ipsum')
print(position)

# les index fonctionnent comme les paramètres de la fonction range()
print(my_string[6:11])

print(my_string.replace('ipsum', 'foo'))

my_string = my_string.replace('ipsum', 'foo')
print(my_string)

def my_function():
    """Documentation for my_function"""
    pass

# help(my_function)

mails = 5

print("Vous avez reçu " + str(mails) + " mails")
print(f"Vous avez reçu {mails} mails")

class Person:
    def __init__(self, firstname: str='', lastname: str='', birth_year: int=0):
        self._firstname = firstname
        self._lastname = lastname
        self._birth_year = birth_year

    def get_firstname(self) -> str:
        return self._firstname

    # une fonction qui ne renvoit rien renvoit en :
    # - python : None
    # - java : void
    # - php : null
    # - js : undefined
    def set_firstname(self, firstname: str) -> None:
        self._firstname = firstname

    def get_lastname(self) -> str:
        return self._lastname

    def set_lastname(self, lastname: str) -> None:
        self._lastname = lastname

    def get_birth_year(self) -> int:
        return self._birth_year

    def set_birth_year(self, birth_year: int) -> None:
        self._birth_year = birth_year

p1 = Person('Hedy', 'Lamarr', 1914)
# p1.set_firstname('Hedy')
# p1.set_lastname('Lamarr')
# p1.set_bidth_year(1914)
print(p1.get_firstname())
print(p1.get_lastname())
print(p1.get_birth_year())

p2 = Person()
print(p2.get_firstname())
print(p2.get_lastname())
print(p2.get_birth_year())

class CarFoo:
    def __init__(self):
        """Constructeur de la classe CarFoo"""
        # self désigne l'instance de la classe (ou objet)
        # self == this
        # attribut == variable rattachée à une instance de classe (ou objet)
        self.wheels = 4
        self.engine_on = False
        self.seats = 4
        self.passengers = 0

class CarBar:
    def __init__(self):
        """Constructeur de la classe CarBar"""
        # un _ devant le nom d'un attribut == attribut privé
        self._wheels = 4
        self._engine_on = False
        self._seats = 4
        self._passengers = 0

    # méthode == fonction dans une classe
    # un getter == une méthode qui permet de récupérer la valeur d'un attribut
    # un setter == une méthode qui permet de modifier la valeur d'un attribut

    # getter pour l'attribut _wheels
    def get_wheels(self):
        return self._wheels

    # pas besoin de setter pour l'attribut _wheels
    # car le nombre de roues ne change jamais

    # getter pour l'attribut _engine_on
    # les méthodes qui renvoient un booléen, peuvent être préfixées d'un `is_` ou d'un `has_` au lieu d'un `get_`
    def is_engine_on(self):
        return self._engine_on

    # setter pour l'attribut _engine_on qui permet d'allumer ou éteindre le moteur
    def set_engine_on(self, engine_on):
        if type(engine_on) is bool:
            self._engine_on = engine_on

    # setter pour l'attribut _engine_on qui permet seulement d'allumer le moteur
    def start_engine(self):
        self._engine_on = True

    # setter pour l'attribut _engine_on qui permet seulement d'éteindre le moteur
    def stop_engine(self):
        self._engine_on = False

    # setter pour l'attribut _seats
    def get_seats(self):
        return self._wheels

    # pas besoin de setter pour l'attribut _seats
    # car le nombre de sièges ne change jamais

    # getter qui calcule à la volée le nombre de places libres
    def get_free_seats(self):
        return self._seats - self._passengers

    # pas besoin de setter pour le nombre de places libres
    # car n'est pas un attribut

    # getter pour l'attribut _passengers
    def get_passengers(self):
        return self._passengers

    # ce setter « basique » pour l'attribut _passengers
    # n'est pas utile car il ne permet pas de choisir
    # le nombre de passagers en fonction des places disponibles
    # def set_passengers(self, passengers):
    #     self._passengers = passengers

    # ce setter « personnalisé » pour l'attribut _passengers
    # permet d'ajouter des passagers en fonction des places disponibles
    def add_passengers(self, passengers):
        if passengers > self.get_free_seats():
            self._passengers += self.get_free_seats()
        else:
            self._passengers += passengers

    # ce deuxième setter « personnalisé » pour l'attribut _passengers
    # permet de retirer des passagers en fonction des passagers du véhicule
    def remove_passengers(self, passengers):
        if passengers > self._passengers:
            self.all_passengers_off()
        else:
            self._passengers -= passengers

    # ce troisième setter « personnalisé » pour l'attribut _passengers
    # permet de faire décendre tout le monde sans se préoccuper
    # du nombre de passagers du véhicule
    def all_passengers_off(self):
        self._passengers = 0

# instance d'une classe == objet == une variable contenant une valeur du type de la classe
v1 = CarFoo()
print(v1.wheels)
print(v1.engine_on)
print(v1.seats)
print(v1.passengers)
print()

v2 = CarFoo()
print(v2.wheels)
print(v2.engine_on)
print(v2.seats)
print(v2.passengers)
print()

v1.engine_on = True
print(v1.engine_on)
print()

print(v2.engine_on)
print()

v3 = CarBar()
v3.start_engine()
print(v3.is_engine_on())
v3.add_passengers(3)
print(v3.get_passengers())

v4 = CarBar()
print(v4.is_engine_on())
v4.add_passengers(10)
print(v4.get_passengers())
v4.remove_passengers(2)
print(v4.get_passengers())
v4.all_passengers_off()
print(v4.get_passengers())

class CarFoo:
    def __init__(self):
        """Constructeur de la classe CarFoo"""
        # self == this
        # attribut == variable rattachée à une instance de classe / un objet
        self.wheels = 4
        self.engine_on = False
        self.seats = 4
        self.passengers = 0

# instance d'une classe == objet
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

class CarBar:
    def __init__(self):
        """Constructeur de la classe CarBar"""
        # un _ devant le nom d'un attribut == attribut privé
        self._wheels = 4
        self._engine_on = False
        self._seats = 4
        self._passengers = 0

    # un getter == une méthode qui permet de récupérer la valeur d'un attribut
    # un setter == une méthode qui permet de modifier la valeur d'un attribut

    # méthode == fonction dans une classe
    def get_wheels():
        return self._wheels

    def set_engine_on(self, engine_on):
        if type(engine_on) is bool:
            self._engine_on = engine_on

    def start_engine(self):
        self._engine_on = True

    def stop_engine(self):
        self._engine_on = False

    # les méthodes qui renvoient un booléen, peuvent être préfixées d'un `is_` ou d'un `has_` au lieu d'un `get_`
    def is_engine_on(self):
        return self._engine_on

    def get_seats():
        return self._wheels

    def get_free_seats(self):
        return self._seats - self._passengers

    def get_passengers(self):
        return self._passengers

    # cette méthode @todo
    # def set_passengers(self, passengers):
    #     self._passengers = passengers

    def add_passengers(self, passengers):
        if passengers > self.get_free_seats():
            self._passengers += self.get_free_seats()
        else:
            self._passengers += passengers

    def remove_passengers(self, passengers):
        pass

    def all_passengers_off():
        self._passengers = 0

v3 = CarBar()
v3.start_engine()
print(v3.is_engine_on())
v3.add_passengers(3)
print(v3.get_passengers())

v4 = CarBar()
print(v4.is_engine_on())
v4.add_passengers(10)
print(v4.get_passengers())

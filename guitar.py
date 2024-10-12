# Clase con herencia
from string_instrument import String_Instrument


class Guitar(String_Instrument):
    def __init__(self, _strings, tuner, _material, frets, __model):
        super().__init__(_strings, tuner, _material)
        self.frets = frets
        self.__model = __model

    def kick_body(self):
        print('POP')

    def cut_strings(self, value):
        if value < self.strings:
            self.strings -= value
            print(f'Se cortaron {value} cuerdas. Quedan {self.strings} cuerdas')
        else:
            print('No puedes cortar más cuerdas de las que tiene la guitarra.')

    @property
    def model(self):
        return self.__model.title

    @model.setter
    def model(self, new):
        self.__model = new


Fender = Guitar(6, 'Clavijero', 'Arce', '22', 'Stratocaster')

print(Fender.model())
Fender.model = 'Telecaster'
print(Fender.model())
Fender.tune_up()
Fender.play()
Fender.kick_body()
print(f'{Fender.model()} tiene {Fender.strings} cuerdas')
Fender.strings = 5
print(f'{Fender.model()} ahora tiene {Fender.strings} cuerdas')
Fender.cut_strings(1)
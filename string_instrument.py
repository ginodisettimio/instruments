#Clase con encapsulamiento

from instrument import Instrument

class String_Instrument(Instrument):
    def __init__(self, _strings, tuner, _material):
        super().__init__()
        self._strings = _strings
        self.tuner = tuner
        self._material = _material

    def tune_up(self):
        return print('Afinado correctamente') 
    
    def play(self):
        return print('twang')

    @property
    def strings(self):
        return self._strings

    @strings.setter
    def strings(self, strings):
        self._strings = strings


Violin = String_Instrument(4, 'Clavijas', 'Pino')

Violin.tune_up()
Violin.play()
print(f'Tiene {Violin.strings} cuerdas')
Violin.strings = 5
print(f'Tiene {Violin.strings} cuerdas')
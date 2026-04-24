"""
Fichero: aleatorios.py
Nombre: Mireia Ureña López
"""

class Aleat:
    """
    Clase que implementa un generador de números aleatorios usando el método LGC.

    Atributos:
        m (int): Módulo.
        a (int): Multiplicador.
        c (int): Incremento.
        x (int): Semilla/Estado actual.

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> next(rand)
    16
    >>> next(rand)
    29
    >>> next(rand)
    18
    >>> next(rand)
    15
    >>> rand(29)
    >>> next(rand)
    18
    >>> next(rand)
    15
    >>> next(rand)
    20
    >>> next(rand)
    1
    """
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        """Inicializa el generador con parámetros POSIX por defecto."""
        self.m, self.a, self.c, self.x = m, a, c, x0

    def __next__(self):
        """Genera el siguiente número de la secuencia."""
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __iter__(self):
        return self

    def __call__(self, x0):
        """Reinicia la semilla."""
        self.x = x0

def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora de números aleatorios LGC.

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> next(rand)
    34
    >>> next(rand)
    24
    >>> next(rand)
    38
    >>> next(rand)
    44
    >>> rand.send(24)
    38
    >>> next(rand)
    44
    >>> next(rand)
    10
    >>> next(rand)
    32
    >>> next(rand)
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        nuevo = yield x
        if nuevo is not None:
            x = nuevo
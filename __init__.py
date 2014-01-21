from trytond.pool import Pool
from .library import *


def register():
    Pool.register(
        Library,
        module='library', type_='model'
    )

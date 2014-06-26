# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.pool import Pool
from .activity import *


def register():
    Pool.register(
        Rating,
        Activity,
        module='activity_rating', type_='model')

# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pool import PoolMeta

__all__ = ['Rating', 'Activity']
__metaclass__ = PoolMeta


class Rating(ModelSQL, ModelView):
    'Activity Rating'
    __name__ = 'activity.rating'

    name = fields.Char('Name', required=True)


class Activity:
    __name__ = 'activity.activity'

    rating = fields.Many2One('activity.rating', 'Rating')

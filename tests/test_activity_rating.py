# This file is part of the product_sequence module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class ActivityRatingTestCase(ModuleTestCase):
    'Test Activity Rating module'
    module = 'activity_rating'

def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        ActivityRatingTestCase))
    return suite

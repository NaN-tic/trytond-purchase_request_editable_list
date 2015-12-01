# This file is part of the purchase_request_editable_list module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class PurchaseRequestEditableListTestCase(ModuleTestCase):
    'Test Purchase Request Editable List module'
    module = 'purchase_request_editable_list'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        PurchaseRequestEditableListTestCase))
    return suite
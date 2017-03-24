import unittest
from debit import Debit


class DebitTestCase(unittest.TestCase):
    def setUp(self):
        self._debit = Debit(100)

    def test_extend_debit(self):
        money = 50
        self.assertEqual(self._debit.extend_debit(money), 0)
        self.assertEqual(self._debit.get_current_debit(), money)

    def test_extend_debit_too_much(self):
        money = 101
        self.assertEqual(self._debit.extend_debit(money), 1)
        self.assertEqual(self._debit.get_current_debit(), 0)

    def test_extend_debit_twice(self):
        first_extend = 50
        second_extend = 20
        self.assertEqual(self._debit.extend_debit(first_extend), 0)
        self.assertEqual(self._debit.extend_debit(second_extend), 0)
        self.assertEqual(self._debit.get_current_debit(), first_extend+second_extend)

    def test_extend_debit_twice_to_much(self):
        first_extend = 50
        second_extend = 70
        self.assertEqual(self._debit.extend_debit(first_extend), 0)
        self.assertEqual(self._debit.extend_debit(second_extend), 1)
        self.assertEqual(self._debit.get_current_debit(), first_extend)

    def test_cut_debit(self):
        extend = 25
        cut = 10
        self._debit.extend_debit(extend)
        self.assertEqual(self._debit.cut_debit(cut), 0)
        self.assertEqual(self._debit.get_current_debit(), extend-cut)

    def test_cut_debit_to_zero(self):
        money = 25
        self._debit.extend_debit(money)
        self.assertEqual(self._debit.cut_debit(money), 0)
        self.assertEqual(self._debit.get_current_debit(), 0)

    def test_cut_debit_rest(self):
        money = 25
        self._debit.extend_debit(money)
        self.assertEqual(self._debit.cut_debit(money*2), money)
        self.assertEqual(self._debit.get_current_debit(), 0)

    def test_cut_debit_with_minus_value(self):
        money = -25
        try:
            self._debit.cut_debit(money)
        except ValueError:
            pass
        else:
            self.fail('ValueError not raised')

    def test_extend_debit_with_minus_value(self):
        money = -25
        try:
            self._debit.extend_debit(money)
        except ValueError:
            pass
        else:
            self.fail('ValueError not raised')

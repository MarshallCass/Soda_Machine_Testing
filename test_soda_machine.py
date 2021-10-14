from logging import RootLogger
import unittest
from coins import Coin, Dime, Nickel, Penny, Quarter
from soda_machine import SodaMachine
from coins import Coin, Quarter, Dime, Nickel, Penny


class TestSodaMachine(unittest.TestCase):
    """Tests for Customer's Soda Machine method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

# fill_register test
    def test_register_len(self):
        """Instantiate Soda Machine, test that its register list has len of 88"""
        self.assertEqual(len(self.soda_machine.register), 88)

# fill_inventory test
    def test_inventory_len(self):
        """Instantiate Soda Machine, test that its inventory list has len of 30"""
        self.assertEqual(len(self.soda_machine.inventory), 30)

# register_has_coing 5 tests
    def test_get_quarter_from_register(self):
        """Test that a quarter can be returned from the register"""
        returned_coin = self.soda_machine.get_coin_from_register('Quarter')
        self.assertEqual(returned_coin.value, .25)

    def test_get_dime_from_register(self):
        """Test that a dime can be returned from the register"""
        returned_coin = self.soda_machine.get_coin_from_register('Dime')
        self.assertEqual(returned_coin.value, .10)

    def test_get_nickel_from_register(self):
        """Test that a nickel can be returned from the register"""
        returned_coin = self.soda_machine.get_coin_from_register('Nickel')
        self.assertEqual(returned_coin.value, .05)

    def test_get_penny_from_register(self):
        """Test that a penny can be returned from the register"""
        returned_coin = self.soda_machine.get_coin_from_register('Penny')
        self.assertEqual(returned_coin.value, .01)

    def test_string_input_return_none(self):
        """Pass in a 'String' and return none"""
        returned_coin = self.soda_machine.get_coin_from_register('Cool Runnings')
        self.assertIsNone(returned_coin, None)

# register_has_coin 5 tests  
    def test_register_has_quarter(self):
        """Test that a quarter can be returned from the register"""
        has_quarter = self.soda_machine.register_has_coin('Quarter')
        self.assertTrue(has_quarter)

    def test_register_has_dime(self):
        """Test that a dime can be returned from the register"""
        has_dime = self.soda_machine.register_has_coin('Dime')
        self.assertTrue(has_dime)

    def test_register_has_nickel(self):
        """Test that a nickel can be returned from the register"""
        has_nickel = self.soda_machine.register_has_coin('Nickel')
        self.assertTrue(has_nickel)

    def test_register_has_penny(self):
        """Test that a penny can be returned from the register"""
        has_penny = self.soda_machine.register_has_coin('Penny')
        self.assertTrue(has_penny)

    def test_non_valid_coin_name(self):
        """Pass in a non valid coin name to return false"""
        has_pennies = self.soda_machine.register_has_coin('Pennies')
        self.assertFalse(has_pennies)  

# determine_change_value 3 tests
    def test_refund_change_overpay(self):
        """Test that when you overpay you get the correct change"""
        change_returned = self.soda_machine.determine_change_value(.75, .60)
        self.assertEqual(change_returned, .15)

    def test_refund_change_underpay(self):
        """Test that when you underpay you get a negative return"""
        change_returned = self.soda_machine.determine_change_value(.50, .60)
        self.assertEqual(change_returned, -.10)

    def test_refund_correct_payment(self):
        """Test that when you give correct change there is no refund"""
        change_returned = self.soda_machine.determine_change_value(.60, .60)
        self.assertEqual(change_returned, 0)

# calculate_coin_value 2 tests
    def test_calulate_coin_value_with_list(self):
        """Test that when you put in a list of coins, it calculates the right value"""
        dime = Dime()
        nickel = Nickel()
        quarter = Quarter()
        penny = Penny()
        new_coin_list = [dime, nickel, quarter, penny]
        correct_change = self.soda_machine.calculate_coin_value(new_coin_list)
        self.assertEqual(correct_change, .41)

    def test_calulate_coin_value_without_list(self):
        """Test that when you don't input a list, it calculates the right value"""
        new_coin_list = []
        correct_change = self.soda_machine.calculate_coin_value(new_coin_list)
        self.assertEqual(correct_change, 0)

    def test_git_inventory_soda(self):
        """Pass in each soda name and insure return of same name"""
        soda_names_match = self.soda_machine.register_has_coin('Quarter')
#       self.assertTrue(has_quarter)



if __name__ == '__main__':
    unittest.main()
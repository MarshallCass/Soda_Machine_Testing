from logging import RootLogger
import unittest
from cans import Can, Cola, OrangeSoda, RootBeer
from coins import Coin, Dime, Nickel, Penny, Quarter
from soda_machine import SodaMachine



class TestSodaMachine1(unittest.TestCase):
    """Tests for Customer's Soda Machine method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

# fill_register test
    def test_register_len(self):
        """Instantiate Soda Machine, test that its register list has len of 88"""
        self.assertEqual(len(self.soda_machine.register), 88)

class TestSodaMachine2(unittest.TestCase):
    """Tests for Customer's Soda Machine method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

# fill_inventory test
    def test_inventory_len(self):
        """Instantiate Soda Machine, test that its inventory list has len of 30"""
        self.assertEqual(len(self.soda_machine.inventory), 30)

class TestSodaMachine3(unittest.TestCase):
    """Tests for Customer's Soda Machine method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

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

class TestSodaMachine4(unittest.TestCase):
    """Tests for Customer's Soda Machine method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

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

class TestSodaMachine5(unittest.TestCase):
    """Tests for Customer's Soda Machine method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

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

class TestSodaMachine6(unittest.TestCase):
    """Tests for Customer's Soda Machine method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

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

class TestSodaMachine7(unittest.TestCase):
    """Tests for Customer's Soda Machine method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

# Test passing in a soda name 4 tests
    def test_get_inventory_cola(self):
        """Pass in Cola soda name and insure return of same name"""
        cola_check = self.soda_machine.get_inventory_soda('Cola')
        self.assertEqual(cola_check.name, 'Cola')

    def test_get_inventory_orangesoda(self):
        """Pass in Orange Soda name and insure return of same name"""
        orangesoda_check = self.soda_machine.get_inventory_soda('Orange Soda')
        self.assertEqual(orangesoda_check.name, 'Orange Soda')

    def test_get_inventory_rootbeer(self):
        """Pass in Root Beer name and insure return of same name"""
        rootbeer_check = self.soda_machine.get_inventory_soda('Root Beer')
        self.assertEqual(rootbeer_check.name, 'Root Beer')

    def test_get_inventory_mtdew(self):
        """Pass in Mountain Dew name and insure return of same name"""
        mtdew_check = self.soda_machine.get_inventory_soda('Mountain Dew')
        self.assertEqual(mtdew_check, None)    

class TestSodaMachine8(unittest.TestCase):
    """Tests for Customer's Soda Machine method"""

    def setUp(self):
        self.soda_machine = SodaMachine()
    
# Test passing a can in the inventory method 1 test
    def test_return_inventory(self):
        """Instanciate a can and pass it into the method insure inventory increases to 31"""
        can = 'Cola'
        self.soda_machine.inventory.append(can)
        self.assertEqual(len(self.soda_machine.inventory), 31)

class TestSodaMachine9(unittest.TestCase):
    """Tests for Customer's Soda Machine method"""

    def setUp(self):
        self.soda_machine = SodaMachine()

# Test 4 different types of coins in a list and passing it into the register
    def test_deposit_coins_into_register(self):
        """Insert 4 different coins and make sure it reflects in the len of self.register"""
        dime = Dime()
        nickel = Nickel()
        quarter = Quarter()
        penny = Penny()
        new_coin_list = [dime, nickel, quarter, penny]
        self.soda_machine.deposit_coins_into_register(new_coin_list)
        self.assertEqual(len(self.soda_machine.register), 92)

if __name__ == '__main__':
    unittest.main()
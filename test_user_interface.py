import unittest
import user_interface
import os
from cans import Can, Cola, OrangeSoda, RootBeer
from coins import Coin, Quarter, Dime, Nickel, Penny

class TestValidateMainMenu(unittest.TestCase):
    """Tests for Customer's User Interface Module"""

    def test_validate_main_menu_num_one(self):
        """Pass in number 1 ensure (true,number) is returned"""
        number_one = user_interface.validate_main_menu(1)
        self.assertEqual(number_one, (True, 1))
    
    def test_validate_main_menu_num_two(self):
        """Pass in number 2 ensure (true,number) is returned"""
        number_two = user_interface.validate_main_menu(2)
        self.assertEqual(number_two, (True, 2))

    def test_validate_main_menu_num_three(self):
        """Pass in number 3 ensure (true,number) is returned"""
        number_three = user_interface.validate_main_menu(3)
        self.assertEqual(number_three, (True, 3))

    def test_validate_main_menu_num_four(self):
        """Pass in number 4 ensure (true,number) is returned"""
        number_four = user_interface.validate_main_menu(4)
        self.assertEqual(number_four, (True, 4))

    def test_validate_main_menu_num_five(self):
        """Pass in number 5 ensure (true,number) is returned"""
        number_five = user_interface.validate_main_menu(5)
        self.assertEqual(number_five, (False, None))

class TestTryParseInt(unittest.TestCase):
    """Test to turn string into integer"""
    def test_try_parse_int(self):
        """Test to see if number string changes to integer"""
        parse_check = user_interface.try_parse_int("10")
        self.assertEqual(parse_check, 10)
    def test_try_parse_int_word(self):
        """Test to see if entering anything orther than a number string will return 0"""
        parse_check = user_interface.try_parse_int("hello")
        self.assertEqual(parse_check, 0)

class TestGetUniqueCanNames(unittest.TestCase):
    """"Instantiate 6 cans or 2 types and append then to a list return list only 3 names"""
    def test_get_unique_can_names(self):
        cola = Cola()
        orangesoda = OrangeSoda()
        rootbeer = RootBeer()
        self.soda_list = [cola, cola, orangesoda, orangesoda, rootbeer, rootbeer]
        unique_cans = user_interface.get_unique_can_names(self.soda_list)
        self.assertEqual(len(unique_cans), 3)

    def test_get_unique_can_names_one(self):
        self.empty_list = []
        unique_cans = user_interface.get_unique_can_names(self.empty_list)
        self.assertEqual(len(unique_cans), 0)

class TestDisplayPaymentValue(unittest.TestCase):

    def test_display_payment_value(self):
        """"Pass 4 coin types in a list and ensure they return a value of .41"""
        dime = Dime()
        nickel = Nickel()
        quarter = Quarter()
        penny = Penny()
        new_coin_list = [dime, nickel, quarter, penny]
        correct_change = user_interface.display_payment_value(new_coin_list)
        self.assertEqual(correct_change, .41)

    def test_display_payment_value_one(self):
        """"Pass 0 coin types in a list and ensure they return a value of 0"""
        new_coin_list = []
        correct_change = user_interface.display_payment_value(new_coin_list)
        self.assertEqual(correct_change, 0)

class TestValidateCoinSeletction(unittest.TestCase):
    """Pass in each int 1-5, ensure the correct tuple is returned"""
    def test_1_validate_coin_selection(self):
        """"Pass in 1, ensure the correct tuple is returned"""
        number_one = user_interface.validate_coin_selection(1)
        self.assertEqual(number_one, (True, 'Quarter'))
        
    def test_2_validate_coin_selection(self):
        """"Pass in 2, ensure the correct tuple is returned"""
        number_two = user_interface.validate_coin_selection(2)
        self.assertEqual(number_two, (True, 'Dime'))
    
    def test_3_validate_coin_selection(self):
        """"Pass in 3, ensure the correct tuple is returned"""
        number_three = user_interface.validate_coin_selection(3)
        self.assertEqual(number_three, (True, 'Nickel'))
    
    def test_4_validate_coin_selection(self):
        """"Pass in 4, ensure the correct tuple is returned"""
        number_four = user_interface.validate_coin_selection(4)
        self.assertEqual(number_four, (True, 'Penny'))

    def test_5_validate_coin_selection(self):
        """"Pass in 5, ensure the correct tuple is returned"""
        number_five = user_interface.validate_coin_selection(5)
        self.assertEqual(number_five, (True, 'Done'))

    def test_6_validate_coin_selection(self):
        """"Pass in 6, ensure the correct tuple is returned"""
        number_six = user_interface.validate_coin_selection(6)
        self.assertEqual(number_six, (False, None))



if __name__ == '__main__':
    unittest.main()
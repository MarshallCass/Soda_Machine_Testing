import unittest
import user_interface
import os
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

    def test_display_payment_value(self):
        """"Pass 0 coin types in a list and ensure they return a value of 0"""
        new_coin_list = []
        correct_change = user_interface.display_payment_value(new_coin_list)
        self.assertEqual(correct_change, 0)

if __name__ == '__main__':
    unittest.main()
import unittest
import user_interface
import os
from cans import Can, Cola, OrangeSoda, RootBeer

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
    def test_get_unique_can_Names(self):
        cola = Cola()
        orangesoda = OrangeSoda()
        rootbeer = RootBeer()
        self.soda_list = [cola, cola, orangesoda, orangesoda, rootbeer, rootbeer]
        unique_cans = user_interface.get_unique_can_names(self.soda_list)
        self.assertEqual(len(unique_cans), 3)

if __name__ == '__main__':
    unittest.main()
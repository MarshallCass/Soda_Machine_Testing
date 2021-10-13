from logging import RootLogger
import unittest
from customer import Customer

class TestGetWalletCoin(unittest.TestCase):
    """Tests for Customer's get_wallet_coin method"""

    def setUp(self):
        self.customer = Customer()

    def test_can_return_quarter(self):
        """Pass in 'Quarter', method should return a Quarter instance"""
        returned_coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(returned_coin.value, .25)
    
    def test_can_return_dime(self):
        """Pass in 'Dime', method should return a Dime instance"""
        return_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(return_coin.value, .10)

    def test_can_return_nickel(self):
        """Pass in 'Nickel', method should return a Nickel instance"""
        return_coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(return_coin.value, .05)    

    def test_can_return_penny(self):
        """Pass in 'penny', method should return a penny instance"""
        return_coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(return_coin.value, .01)

    def test_string_input_return_none(self):
        """Pass in a 'String' and return none"""
        return_coin = self.customer.get_wallet_coin('Running')
        self.assertIsNone(return_coin, None)


    def test_add_can_to_backpack(self, cola):
        """Pass in a Cola object and check backpack purchased cans list """
        return_backpack_len = self.backpack.purchased_cans.append(self.can.name(cola))
        self.assertEqual(return_backpack_len, self.can.name(cola))

if __name__ == '__main__':
    unittest.main()
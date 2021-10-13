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
    
    def test_can_return_quarter(self):
        """Pass in 'Dime', method should return a Dime instance"""
        return_coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(return_coin.value, .10)


if __name__ == '__main__':
    unittest.main()
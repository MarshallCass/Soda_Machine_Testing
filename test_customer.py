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



    def test_coins_








if __name__ == '__main__':
    unittest.main()
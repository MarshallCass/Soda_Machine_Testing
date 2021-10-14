from logging import RootLogger
import unittest
from coins import Coin
from customer import Customer

class TestGetWalletCoin1(unittest.TestCase):
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


class TestGetWalletCoin2(unittest.TestCase):
    """Tests for Customer's get_wallet_coin method"""

    def setUp(self):
        self.customer = Customer()

    def test_3_coins_add_to_wallet(self):
        """Pass in a list of 3 coins, len of customers wallets money list coincides"""
        current_number_of_coins = len(self.customer.wallet.money)
        self.customer.add_coins_to_wallet(['Quarter', 'Nickel', 'Dime'])
        self.assertEqual(len(self.customer.wallet.money), current_number_of_coins + 3)

    def test_0_coins_add_to_wallet(self):
        """Pass in a list of 0 coins, len of customers wallets money list coincides"""
        current_number_of_coins = len(self.customer.wallet.money)
        self.customer.add_coins_to_wallet([])
        self.assertEqual(len(self.customer.wallet.money), current_number_of_coins)


class TestGetWalletCoin3(unittest.TestCase):
    """Tests for Customer's get_wallet_coin method"""

    def setUp(self):
        self.customer = Customer()

    def test_add_cola_can_to_backpack(self):
        """Pass in a cola object and make sure the len of customers backpack coincides"""
        current_number_of_cola_cans = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack('Cola')
        self.assertEqual(len(self.customer.backpack.purchased_cans), current_number_of_cola_cans + 1)

    def test_add_root_beer_can_to_backpack(self):
        """Pass in a Root Beer object and make sure the len of customers backpack coincides"""
        current_number_of_root_beer_cans = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack('Root Beer')
        self.assertEqual(len(self.customer.backpack.purchased_cans), current_number_of_root_beer_cans + 1)

    def test_add_orange_soda_can_to_backpack(self):
        """Pass in a Orange Soda object and make sure the len of customers backpack coincides"""
        current_number_of_orange_soda_cans = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack('Orange Soda')
        self.assertEqual(len(self.customer.backpack.purchased_cans), current_number_of_orange_soda_cans + 1)

if __name__ == '__main__':
    unittest.main()
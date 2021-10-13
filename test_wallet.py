from logging import RootLogger
import unittest
from wallet import Wallet

class TestWalletlen(unittest.TestCase):
    """Tests for Customer's get_wallet_coin method"""

    def setUp(self):
        self.wallet_len = Wallet()
        
    def test_wallet_len(self):
        """Instantiate a Wallet object, test that its money list has len of 88"""

        current_wallet_len = len(self.wallet_len.money)
        self.assertEqual(len(self.wallet_len.money), 88)
        

if __name__ == '__main__':
    unittest.main()
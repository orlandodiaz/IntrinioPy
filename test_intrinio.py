import unittest
from IntrinioPy import Intrinio
import os

class TestIntrinio(unittest.TestCase):

    def setUp(self):
        self.intrinio = Intrinio()

    def tearDown(self):
        pass

    def test_get_stocks_for_given_url(self):
        stocks = self.intrinio.get_stocks()

    def test_save(self):
        stocks = self.intrinio.get_stocks()
        pickle_name = "stocks_250_to_1b.p"
        self.intrinio.save(stocks, pickle_name)

        assert os.path.isfile(pickle_name)
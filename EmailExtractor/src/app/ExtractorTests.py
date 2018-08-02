import unittest
from .EmailExtractor import EmailExtractor


class MyTestCase(unittest.TestCase):
    def test_something(self):
        extractor = EmailExtractor()
        extractor.extractAddresses('app/data/messages/')
        extractor.exportAddresses()

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

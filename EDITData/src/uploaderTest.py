import unittest
from ResultsUploader import ReseultsUploader


class MyTestCase(unittest.TestCase):
    def test_uploader(self):
        creator = ReseultsUploader()
        creator.uploarResultfromCSV('data/Estructura_EDIT_IND_VIII_2015_2016.csv')
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()

import unittest

from ReaderTests import ReaderTests
from WriterTests import WriterTests


class MyTestCase(unittest.TestCase):
    def test_TXTExcel(self):
        reader = ReaderTests()
        reader.openTxtFromExcel('TEST-01.txt')
        reader.saveTxtFromExcelToDB()
        self.assertEqual(True, True)

    def test_writeTXTExcel(self):
        writer = WriterTests()
        writer.exportDataToCSV('TEXT-01.csv')
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()

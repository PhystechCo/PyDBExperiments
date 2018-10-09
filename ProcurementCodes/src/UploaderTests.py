import unittest

from .CodeUploader import CodeUploader
from .UNSPSCCodesMatcher import UNSPSCCodeMatcher


class UploaderTestCase(unittest.TestCase):
    def test_codeuploader(self):

        uploader = CodeUploader()
        uploader.uploadCodefromCSV('./data/CERN_Procurement_Codes_EN.txt')
        uploader.uploadCodefromCSV('./data/CERN_Procurement_Codes_ES.txt')
        uploader.uploadCodefromCSV('./data/CERN_Procurement_Codes_FR.txt')
        self.assertEqual(True, True)

    def test_unspscCodeuploader(self):

        uploader = CodeUploader()
        uploader.uploadUNSPSCCodefromCSV('./data/unspsc_codes_3.csv')
        self.assertEqual(True, True)

    def test_unspcsCodereadout(self):

        uploader = CodeUploader()
        uploader.queryCodes('41')

    def test_unspcsCodeMatcher(self):

        matcher = UNSPSCCodeMatcher()
        matcher.match()




if __name__ == '__main__':
    unittest.main()

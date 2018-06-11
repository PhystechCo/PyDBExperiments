import unittest
from .ResultsUploader import ReseultsUploader
from .ParametersUploader import ParametersUploader
from .CIIURev4Uploader import CIIUUploader
from .AfiliadosUploader import AfiliadosUploader


class MyTestCase(unittest.TestCase):
    def test_uploader(self):
        creator = ReseultsUploader()
        #creator.uploarResultfromCSV('data/Estructura_EDIT_IND_VIII_2015_2016.csv')
        self.assertEqual(True, True)

    def test_param_uploader(self):
        creator = ParametersUploader()
        creator.uploarResultfromCSV('src/data/didi-variables-01.csv')

    def test_ciiu_uploader(self):
        creator = CIIUUploader()
        creator.uploarResultfromCSV('src/data/ciiu_rev4.csv')

    def test_param_exporter(self):
        creator = ParametersUploader()
        creator.exportResultsCSV(["Nombre", "Etiqueta", "Pregunta"])

    def test_ccbdata_uploader(self):
        creator = AfiliadosUploader()
        creator.uploarResultfromCSV('src/data/Afiliados-2018.csv')

if __name__ == '__main__':
    unittest.main()

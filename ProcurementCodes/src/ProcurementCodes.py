class ProcurementCodes:
    def __init__(self):
        """basic class for CERN based procurement codes"""
        self.segment = "01"
        self.family = "00"
        self.category = "00"
        self.commodity = "00"
        self.code = "00000000"
        self.locale = "X"
        self.description = "X"
        self.segment_description = ""
        self.family_description = ""
        self.category_description = ""

    def setSegment(self, segment):
        self.segment = segment

    def setFamily(self, family):
        self.family = family

    def setCategory(self, category):
        self.category = category

    def setCommodity(self, commodity):
        self.commodity = commodity

    def setCode(self, code):
        self.code = code

    def setLocale(self, locale):
        self.locale = locale

    def setDescription(self, description):
        self.description = description

    def setSegmentDescription(self, description):
        self.segment_description = description

    def setFamilyDescription(self, description):
        self.family_description = description

    def setCategoryDescription(self, description):
        self.category_description = description

    def __str__(self):
        printout = self.family + ' ' + self.code + ' ' + self.description
        return printout

class Email:
    def __init__(self):
        self.subject = ''
        self.email_from = ''
        self.email_date = ''

    def setSubject(self,subject):
        self.subject = subject

    def setFrom(self, email_from):
        self.email_from = email_from

    def setDate(self, email_date):
        self.email_date = email_date

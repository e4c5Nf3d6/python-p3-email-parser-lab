import re

class EmailAddressParser:
    def __init__(self, email_addresses):
        self.email_addresses = email_addresses

    def parse(self):

        email_format = re.compile(r'[A-Za-z][a-zA-Z0-9_\.]+\@\w+\.\w+')
        valid_emails = re.findall(email_format, self.email_addresses)

        return sorted(list(set(valid_emails)))

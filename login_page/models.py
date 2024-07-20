# Mock User model
class User:
    def __init__(self, username, email, password, full_name='', contact_info=''):
        self.username = username
        self.email = email
        self.password = password
        self.full_name = full_name
        self.contact_info = contact_info

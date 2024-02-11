# == INSTRUCTIONS ==
#
# Purpose: Manage a user's (valid) passwords
#
# Methods:
#   1. Name: __init__
#      Arguments: none
#   2. Name: add
#      Purpose: add a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   3. Name: remove
#      Purpose: remove a password for a service
#      Arguments: one string representing a service name
#      Returns: None
#   4. Name: update
#      Purpose: update a password for a service IF it is valid, otherwise do nothing
#      Arguments: one string representing a service name,
#                 one string representing a password
#      Returns: None
#   5. Name: list_services
#      Arguments: none
#      Returns: a list of all the services for which the user has a password
#   6. Name: sort_services_by
#      Arguments: A string, either 'service' or 'added_on',
#                 (Optional) A string 'reverse' to reverse the order
#      Returns: a list of all the services for which the user has a password
#               in the order specified
#   7. Name: get_for_service
#      Arguments: one string representing a service name
#      Returns: the password for the given service, or None if none exists
#
# A reminder of the validity rules:
#   1. A password must be at least 8 characters long
#   2. A password must contain at least one of the following special characters:
#      `!`, `@`, `$`, `%` or `&`
#
# And a new rule: passwords must be unique (not reused in other services).
#
# Example usage:
#   > password_manager = PasswordManager2()
#   > password_manager.add('gmail', '12ab5!678')   # Valid password
#   > password_manager.add('facebook', '$abc1234') # Valid password
#   > password_manager.add('youtube', '3@245256')  # Valid password
#   > password_manager.add('twitter', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('facebook')
#   '$abc1234'
#   > password_manager.list_services()
#   ['gmail', 'facebook', 'youtube']
#   > password_manager.remove('facebook')
#   > password_manager.list_services()
#   ['gmail', 'youtube']
#   > password_manager.update('gmail', '12345678')  # Invalid password, so ignored
#   > password_manager.get_for_service('gmail')
#   '12ab5!678'
#   > password_manager.update('gmail', '%21321415')  # Valid password
#   > password_manager.get_for_service('gmail')
#   '%21321415'
#   > password_manager.sort_services_by('service')
#   ['gmail', 'youtube']
#   > password_manager.sort_services_by('added_on', 'reverse')
#   ['youtube', 'gmail']

# There are many more examples possible but the above should give you a good
# idea.

# == YOUR CODE ==

from datetime import datetime
class PasswordManager2():
    def __init__(self) -> None:
        self.passwords = {}

    def add(self, service, password):
        if self.is_overall_a_valid_password(password):
            self.passwords[service] = password

    def list_services(self):
        return list(self.passwords.keys())
    
    def is_long_enough(self, password):
        return len(password) > 7
    
    def is_spec_char_in_password(self, password):
        spec_characters = ['!', '@', '$', '%', '&']
        if any(char in password for char in spec_characters):
            return True
        return False
    
    def is_password_unique(self, password):
        if password in self.passwords.values():
            return False
        return True
    
    def remove(self, service):
        del self.passwords[service]

    def update(self, service, password):
        if self.is_overall_a_valid_password(password):
            self.passwords.update({service: password})

    def get_for_service(self, service):
        return self.passwords.get(service)
    
    def is_overall_a_valid_password(self, password):
        return self.is_long_enough(password) and self.is_spec_char_in_password(password) and self.is_password_unique(password)
    
    def sort_services_by(self, sort_by, order='alphabetical'):
        if sort_by == 'service' and order == 'reverse':
            return sorted(self.passwords.keys())[::-1]
        if sort_by == 'added_on' and order == 'reverse':
            return list(self.passwords.keys())[::-1]
        if sort_by == 'added_on':
            return list(self.passwords.keys())
        else:
            return sorted(self.passwords.keys())
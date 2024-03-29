import hashlib
import unittest

# Create user database
users = {}

# Sha3-512 hashing function
def hash(input):
    hash = hashlib.sha3_512()
    hash.update(bytes(input, 'utf-8'))
    return hash.hexdigest()

# Register a user with username and password
def register(username, password):

    # Update users database
    users.update({username: hash(password)})

# Login with username and password
def login(username, password):

    # Check credentials
    if username in users and hash(password) == users[username]:
        return True
    else:
        return False

# Testing
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        register("michael", "ehre")
        register("daniel", "030")

    def test_login_success(self):
        self.assertEqual(login("daniel", "030"), True, "incorrect credentials")

    def test_login_fail(self):
        self.assertEqual(login("daniel", "040"), False, "incorrect credentials")
 
# run the test
unittest.main()


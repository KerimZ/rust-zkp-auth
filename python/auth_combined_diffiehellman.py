# Imports
import hashlib
import unittest
import random

# Set up auth parameters
p = 1907 # Order of G
q = 953 # Subgroup prime factor
g = 23 # generator of subgroup (really?)

x = random.randint(2**31, 2**32) % p
y = random.randint(2**31, 2**32) % p

X = pow(g,x,p)
Y = pow(g,y,p)

key1 = pow(X,y,p)
key2 = pow(Y,x,p)

print(key1)
print(key2)

# Create user database
users = {}

# Sha3-512 hashing function
def hash(input):
    hash = hashlib.sha3_512()
    hash.update(bytes(input, 'utf-8'))
    return hash.hexdigest()

# Register a user with username and password
# Server/Verifier
def register(username, password):

    # Update users database
    users.update({username: hash(password)})

# Login with username and password
# Client/Prover
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
# unittest.main()



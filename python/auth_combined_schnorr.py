# Imports
import hashlib
import unittest

# Set up auth parameters
p = 23 # Order of G
q = 11 # Subgroup prime factor
g = 2 # generator of subgroup


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
    p = 23
    q = 11

    # Check credentials
    if username in users and hash(password) == users[username]:
        print("FOUND")
    else:
        print("NOT FOUND")

# Testing
register("tom", "password123")
register("peter", "pizzaazzip")
login("peter", "pizzaazzip")




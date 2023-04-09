# Networking imports
import socket

# Cryptography imports
import random

target_host = "127.0.0.1"
target_port = 9999

# Set up auth parameters
p = 1907 # Order of G
q = 953 # Subgroup prime factor
g = 23 # generator of subgroup (really?)

# Generate client key material
client_private_key = random.randint(2**31, 2**32) % p
client_public_key = pow(g, client_private_key, p)
print("[CLIENT] Keys generated") # TODO: remove this in prod?
print(f"[CLIENT] Client private key: {client_private_key}")
print(f"[CLIENT] Client public key: {client_public_key}")

print("[CLIENT] Connecting...")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

print("[CLIENT] Sending key parameters...")
client.send(f"{client_public_key}".encode())

server_public_key = client.recv(1024)
server_public_key = int(server_public_key.decode())
print(f"[CLIENT] Received server public key: {server_public_key}")
key = pow(server_public_key, client_private_key, p)
print(f"[CLIENT] Shared key established: {key}")



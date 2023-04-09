# Networking imports
import socket
import threading

# Cryptography imports
import random # TODO: Implement secure randomness

bind_ip = "0.0.0.0"
bind_port = 9999

# Set up auth parameters
p = 1907 # Order of G
q = 953 # Subgroup prime factor
g = 23 # generator of subgroup (TODO: really?)

print("[*] Server starting...") # TODO: Add string template so generic part of the server message (e.g. [*]) isn't repeated in every string
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip,bind_port))
server.listen(5)
print(f"[*] Listening on {bind_ip}:{bind_port}")

def handle_client(client_socket):

    # Generate server key material for connected client
    server_private_key = random.randint(2**31, 2**32) % p # TODO: Use secure bit sizes, but also add the capability to switch to toy numbers (e.g. group = 23)
    server_public_key = pow(g, server_private_key, p)
    print("[*] Keys generated") # TODO: remove this in prod?
    print(f"[*] Server private key: {server_private_key}")
    print(f"[*] Server public key: {server_public_key}")


    client_public_key = client_socket.recv(1024)
    client_public_key = int(client_public_key.decode())
    print(f"[*] Received client public key: {client_public_key}")
    client_socket.send(f"{server_public_key}".encode())
    client_socket.close()

    key = pow(client_public_key, server_private_key, p)
    print(f"[*] Shared key established: {key}")

while True:
    client,addr = server.accept()
    print(f"[*] Acepted connection from: {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
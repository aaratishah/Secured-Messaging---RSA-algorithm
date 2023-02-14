import socket
import json
from socket_server import PUBLIC_KEY, YOUR_KEY
import generate_key
import generate_symmetric_key

def run_client():
    # Create a dictionary to store secrets (public key)
    secrets = {}
    # Create a dictionary to store the encryption key
    encryption_key = {}

    # Hostname of the server to connect to
    host = socket.gethostname()
    # Port to use for the connection
    port = 4001

    # Create a socket for the client
    client = socket.socket()
    # Connect to the server using the host and port
    client.connect((host, port))

    # Get the first message from the user
    message = input(" -> ")

    # Continuously send messages to the server until the user enters 'bye'
    while message.lower().strip() != 'bye':
        # If there is an encryption key, encrypt the message and send it
        if "encryption_key" in encryption_key:
            encrypted_message = generate_symmetric_key.encrypt_message(encryption_key["encryption_key"], message)
            client.send(encrypted_message)
        # If there is a public key, generate a symmetric key, encrypt it with the public key, and send it to the server
        else:
            if "public_key" in secrets:
                encryption_key = {"encryption_key" : generate_symmetric_key.generate_symmetric_key().decode("utf-8")}
                encrypted_message = generate_key.encrypt(encryption_key["encryption_key"], secrets["public_key"])
                client.send(json.dumps({YOUR_KEY: encrypted_message}).encode())
                secrets = {}
            # If there is no public key, send the message unencrypted
            else:
                print(message.encode())
                client.send(message.encode())

        # Receive the response from the server
        data = client.recv(1024).decode()

        # If the response from the server is a public key, store it in the secrets dictionary
        if "public_key" in data:
            secrets = json.loads(data)

        try:
            # Try to decrypt the message from the server
            print('###ENCRYPTED MSG FROM SERVER: ' + data)
            data = generate_symmetric_key.decrypt_message(encryption_key["encryption_key"], data)
        except:
            # If decryption fails, pass (do nothing)
            pass
        finally:
            # Print the received message, either decrypted or not
            print('Received from server: ' + data)
            message = input(" :: ")

    # Close the client socket
    client.close()

if __name__ == "__main__":
    run_client()

import socket
import json
import prime_generator
import generate_key
import generate_symmetric_key

# Define two constant strings to be used as markers in the communication
PUBLIC_KEY = "Send Public Key"
YOUR_KEY = "YOUR_KEY"

def server_program():
    # Initialize two dictionaries to store the public and private keys, and the decryption key
    public_private_key = {}
    my_decryption_key = {}

    # Get the host name and the port to be used for the server
    host = socket.gethostname()
    port = 4001

    # Create a socket for the server
    server_socket = socket.socket()
    # Bind the socket to the host and port
    server_socket.bind((host, port))
    # Listen for incoming connections
    server_socket.listen(2)
    # Accept the incoming connection
    conn, address = server_socket.accept()
    print(f"Connected with {address}")

    # Continuously receive messages from the client
    while True:
        msg_from_client = conn.recv(1024).decode()
        # If the received message is empty, break the loop
        if not msg_from_client:
            break

        # If the message is equal to the PUBLIC_KEY constant, generate a new public/private key pair
        if msg_from_client == PUBLIC_KEY:
            prime1 = prime_generator.get_random_prime(100, 200)
            prime2 = prime_generator.get_random_prime(100, 200)
            
            # Make sure that prime1 and prime2 are different
            if prime1 != prime2:
                public_private_key = generate_key.generate_key(prime1, prime2)
            else:
                prime2 = prime_generator.get_random_prime(100, 200)
            
            # Send the public key to the client
            conn.send(json.dumps({"public_key": public_private_key["public_key"]}).encode())
            continue
        
        # If the decryption key is already stored in the my_decryption_key dictionary,
        # the received message is encrypted and needs to be decrypted before being processed
        if YOUR_KEY in my_decryption_key:
            print(f"Received encrypted message: {msg_from_client}")
            msg_from_client = generate_symmetric_key.decrypt_message(my_decryption_key[YOUR_KEY], msg_from_client)
            print(f"Message from client: {msg_from_client}")
            # Read a message from the user to send to the client
            data = input(" -> ")
            # Encrypt the message before sending
            data = generate_symmetric_key.encrypt_message(my_decryption_key[YOUR_KEY], data)
            conn.send(data)
        else:
            # If the decryption key is not stored, the received message is the client's public key
            # Decrypt the message to get the decryption key
            if "private_key" in public_private_key:
                msg_from_client = json.loads(msg_from_client)[YOUR_KEY]
                msg_from_client = generate_key.decrypt(msg_from_client, public_private_key["private_key"])
                my_decryption_key = {YOUR_KEY: msg_from_client}
                public_private_key = {}
            
            print(f"Message from client: {msg_from_client}")
            data = input(" -> ")
            conn.send(data.encode())

    conn.close()

if __name__ == "__main__":
    server_program()

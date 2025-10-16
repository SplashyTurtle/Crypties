
# Library imports for cryptography operations
# Using ecc and serialization

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

# Wallet Class 
class Wallet:

    # Initialize the wallet with no keys
    def __init__(self):
        self.private_key = None
        self.public_key = None

    # Create a new pair of keys using generate_private_key method via SECP256K1 curve
    def create_keys(self):
        # Generate a new private key using the SECP256K1 curve
        self.private_key = ec.generate_private_key(ec.SECP256K1())

        # Generate a new public key from private key
        self.public_key = self.private_key.public_key()

    # Get the private key in PEM format
    def get_private_key(self):
        # If private key does not exist, return None 
        if self.private_key is None:
            return None
        # Serialize the private key to PEM format
        pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM, # Converting the private key bytes to PEM format. Bytes since the serialization library works with bytes.
            format=serialization.PrivateFormat.PKCS8, # Using the PKCS8 for PEM private formating to serialize in order to turn it into byte.
            encryption_algorithm=serialization.NoEncryption() # No encryption for simplicity
        )
        return pem.decode('utf-8')
    
    def get_public_key(self):
        if self.public_key is None:
            return None
        # Serialize the public key to PEM format
        pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return pem.decode('utf-8')
    

if __name__ == "__main__":#
    wallet = Wallet()
    wallet.create_keys()
    print("Private Key:")
    print(wallet.get_private_key())
    print("Public Key:")
    print(wallet.get_public_key())
    


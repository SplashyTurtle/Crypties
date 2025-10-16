
# Library imports for cryptography operations
# Using hashes and serialization, padding, and exceptions

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.exceptions import InvalidSignature

# Transaction Class
class Transaction:
    # Initialize the transaction with sender, receiver, amount, signature, and transaction ID
    def __init__(self, sender_public_key, receiver_public_key, amount):
        self.sender_public_key = sender_public_key # public key in PEM format
        self.receiver_public_key = receiver_public_key # public key in PEM format
        self.amount = amount # amount to be transferred
        self.signature = None  # to be filled once signed
        self.transaction_id = None # to be filled once transaction ID is generated

    # Convert transaction details to a string for signing
    def to_string(self):
        return f"{self.sender_public_key}{self.receiver_public_key}{self.amount}"  # Concatenate the transaction details into a single string

    # Sign the transaction using the sender's private key
    def sign_transaction(self, sender_private_key):
        # Sign the transaction using the sender's private key
        message = self.to_string().encode('utf-8') # Encode the transaction string to bytes
        self.signature = sender_private_key.sign( # sender_private_key is an object of type ec.EllipticCurvePrivateKey
            message, # The message to be signed
            ec.ECDSA(hashes.SHA256()) # Using ECDSA with SHA256 for signing
        )

    # Generate a unique transaction ID by hashing the transaction details and signature
    def get_transaction_id(self):
        # Create a SHA256 hash of the transaction details and signature to generate a unique transaction ID
        digest = hashes.Hash(hashes.SHA256()) 
        digest.update(self.to_string().encode('utf-8')) # Update the hash with the transaction details
        if self.signature:
            digest.update(self.signature) # Update the hash with the signature if it exists
        return digest.finalize().hex() # Return the hexadecimal representation of the hash

    # Generate a unique transaction ID by hashing the transaction details and signature
    def verify_signature(self):
        public_key = serialization.load_pem_public_key( # Load the sender's public key from PEM format
            self.sender_public_key.encode() # Encode the PEM string to bytes
        )
        # Verify the signature using the public key (returns True if valid, False otherwise)
        try:
            public_key.verify( 
                self.signature, # The signature to be verified
                self.to_string().encode(), # The original message (transaction details) encoded to bytes
                ec.ECDSA(hashes.SHA256()) # Using ECDSA with SHA256 for verification
            )
            return True
        except InvalidSignature:
            return False
        except Exception as e:
            print(f"Error during signature verification: {e}")
            return False




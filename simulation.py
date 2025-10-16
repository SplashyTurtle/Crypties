import wallet_simulation, transaction_simulation

# Simulate creating wallets and a transaction
def simulate_transaction():
    # Create sender and receiver wallets
    sender_wallet = wallet_simulation.Wallet()
    sender_wallet.create_keys()
    
    receiver_wallet = wallet_simulation.Wallet()
    receiver_wallet.create_keys()
    
    # Display keys
    print("Sender Private Key:")
    print(sender_wallet.get_private_key())
    print("Sender Public Key:")
    print(sender_wallet.get_public_key())
    
    print("Receiver Public Key:")
    print(receiver_wallet.get_public_key())
    
    # Create a transaction
    amount = 10.0
    transaction = transaction_simulation.Transaction(
        sender_public_key=sender_wallet.get_public_key(),
        receiver_public_key=receiver_wallet.get_public_key(),
        amount=amount
    )
    
    # Sign the transaction with the sender's private key
    transaction.sign_transaction(sender_wallet.private_key)
    
    # Generate and display the transaction ID
    transaction_id = transaction.get_transaction_id()
    print(f"Transaction ID: {transaction_id}")
    
    # Verify the transaction signature
    is_valid = transaction.verify_signature()
    print(f"Is the transaction signature valid? {is_valid}")

if __name__ == "__main__":  
    simulate_transaction()
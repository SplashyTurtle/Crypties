# Libraries needed for the Blockchain

import hashlib
import datetime


# Block Class
class Block:

    # Initiliazation of the Block - Combining the all the datas to make a block
    def __init__(self, previous_hash, timestamp, data):
        self.previous_hash = previous_hash  # Hash of the previous block
        self.timestamp = timestamp # Timestamp of the block creation
        self.data = data # Data contained in the block eg. transactions
        self.hash = self.generate_hash() # Accessing the generate_hash method to create the hash of the block
    
    # Generating the hash of the block using SHA-256
    def generate_hash(self):
        block_string = f"{self.previous_hash}{self.timestamp}{self.data}" # Concatenating the previous hash, timestamp and data to create a unique string
        return hashlib.sha256(block_string.encode()).hexdigest() # Generating the SHA-256 hash of the block string
    
    # String representation of the block for easy reading    
    def __str__(self):
        return (f"Timestamp: {self.timestamp}\n"
                f"Data: {self.data}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Hash: {self.hash}\n")


# Blockchain Class
class Blockchain:
    
    # Initiliazation of the chain by creating the genesis block
    def __init__(self):
        self.chain = [] # Creating a list to hold the chain of blocks 
        self.chain.append(self.create_genesis_block()) # and adding the genesis block to it
    
    # Creating the genesis block - The first block in the blockchain
    def create_genesis_block(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p") # Getting the current timestamp in 12-hour format
        return Block("0", timestamp, "Genesis Block") # Previous hash is "0" for the genesis block
    
    # Getting the latest block in the chain
    def get_latest_block(self):
        return self.chain[-1] # Returning the last block in the chain

    # Adding a new block to the chain
    def add_block(self, data):
        previous_block = self.get_latest_block() # Getting the latest block which will be the previous block for the new block
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p") # Getting the current timestamp in 12-hour format
        new_block = Block(previous_block.hash, timestamp, data) # Creating a new block with the previous block's hash, current timestamp and data
        self.chain.append(new_block) # Adding the new block to the chain

    # Validating the integrity of the blockchain
    def is_chain_valid(self):  
        for i in range(1, len(self.chain)): # Starting from the second block to the end of the chain since the first block is the genesis block
            current_block = self.chain[i] # Current block 
            previous_block = self.chain[i - 1] # Previous block

            # Checking if the current block's hash is correct or Checking if the current block's previous hash matches the previous block's hash
            if current_block.hash != current_block.generate_hash() or current_block.previous_hash != previous_block.hash: 
                return False # If any of the conditions fail, return False
        
        return True # If all blocks are valid, return True
    
    # Printing the entire blockchain
    def print_chain(self):
        for block in self.chain: # Iterating through each block in the chain
            print(block) # Printing the block using its string representation
            print("-" * 50) # Printing a separator for better readability
    

# Example usage
if __name__ == "__main__":
    blockchain = Blockchain()

    # Add some sample transactions
    blockchain.add_block("Sean pays Son 100 BTC")
    blockchain.add_block("Elijah pays Igon 0.5 Pesos")
    blockchain.add_block("Son pays Sean 3 BTC")

    blockchain.print_chain()

    print("Blockchain valid?", blockchain.is_chain_valid()) # Checking if the blockchain is valid
    


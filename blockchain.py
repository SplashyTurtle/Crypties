
# TODO: Implement a THE ALGORITHM Blockchain with Proof of Work WITH WALLET PRIVATE KEY


# Libraries import need for the Blockchain with Proof of Work
import hashlib
import time

# Block Class with Proof of Work

class Block:

    # Initiliazation of the Block - Combining the all the datas to make a block to add pa ang Wallet private key
    def __init__(self, index, previous_hash, timestamp, data):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = 0 # Nonce for Proof of Work, this is the variable that will change everytime we try to mine a block
        self.hash = self.generate_hash()

    # Generating the hash of the block using SHA-256 with nonce for Proof of Work
    def generate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.timestamp}{self.data}{self.nonce}"
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    # Mining the block by finding a hash that starts with a certain number of leading zeros (difficulty)
    def mine_block(self, difficulty):
        print(f"Mining block {self.index}...")
        while not self.hash.startswith('0' * difficulty): # Checking if the hash starts with the required number of leading zeros times the difficulty
            self.nonce += 1 # Incrementing the nonce to change the hash
            self.hash = self.generate_hash() # Generating the new hash with the new nonce
        print(f"Block {self.index} mined: {self.hash} nonce: {self.nonce}\n") 

    # String representation of the block for easy reading
    def __str__(self):
        return (f"Index: {self.index}\n"
                f"Timestamp: {self.timestamp}\n"
                f"Data: {self.data}\n"
                f"Previous Hash: {self.previous_hash}\n"
                f"Hash: {self.hash}\n")

# Blockchain Class with Proof of Work  
class Blockchain:

    # Initiliazation of the chain by creating the genesis block with difficulty level
    def __init__(self, difficulty):
        self.chain = []
        self.difficulty = difficulty
        self.chain.append(self.create_genesis_block())

    # Creating the genesis block - The first block in the blockchain setting the index to 0 and previous hash to "0"
    def create_genesis_block(self):
        return Block(0, "0", time.strftime("%Y-%m-%d %H:%M:%S"), "Genesis Block")

    # Getting the latest block in the chain
    def get_latest_block(self):
        return self.chain[-1]

    # Adding a new block to the chain with mining process and getting the difficulty level
    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_index = previous_block.index + 1
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        new_block = Block(new_index, previous_block.hash, timestamp, data)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block) # Adding the new block to the chain if mined successfully

    # Validating the integrity of the blockchain
    def is_chain_valid(self):
        for i in range(1, len(self.chain)): # Starting from the second block to the end of the chain  or until the length of the chain since the first block is the genesis block
            current_block = self.chain[i] # Current block
            previous_block = self.chain[i - 1] # Previous block

            # Checking if the current block's hash is correct or Checking if the current block's previous hash matches the previous block's hash
            if current_block.hash != current_block.generate_hash() or current_block.previous_hash != previous_block.hash: 
                return False
        return True
    
    # Print the entire blockchain
    def print_chain(self):
        for block in self.chain:
            print(block)


# Example usage
if __name__ == "__main__":
    blockchain = Blockchain(4)
    blockchain.add_block("Sean pays Son 100 BTC")
    blockchain.add_block("Elijah pays Igon 0.5 Pesos")
    blockchain.add_block("Son pays Sean 3 BTC")

    blockchain.print_chain()
    print("Is blockchain valid?", blockchain.is_chain_valid())

    

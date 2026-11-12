"""simple blockchain in python"""

import hashlib

class CoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_has = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{'-'.join(transaction_list)} -{previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


t1 = "Noah sends 5 coins to Mark"
t2 = "Mark sends 2.3 coins to James"
t3 = "James sends 4.2 coins to Alisson"
t4 = "Alisson sends 1.1 coins to Noah"


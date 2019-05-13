from typing import List, Dict
import datetime, hashlib, json

"""
Created on Sun May 12 17:49:41 2019
@author: si3mshady
https://www.udemy.com/share/1001jeA0UTdV1UQQ==/
"""

class Blockchain:

    def __init__(self):
        self.chain = []  #initialize empty list that will contain blockchain blocks
        self.create_block(proof=1, previous_hash='0')  #creates Genesis_block

    #create_block called after a block is mined and adds the block to the block_chain includes 4 essential keys
    def create_block(self, proof: int , previous_hash: str) -> List:
        block = {"index": self.chain.__len__() + 1,
                 "timestamp": datetime.datetime.now().__str__(),
                 "proof": proof,
                 "previous_hash": previous_hash }
        self.chain.append(block)
        return block

    def get_previous_block(self) -> List:
        previous_block = self.chain[-1]
        return previous_block

    def proof_of_work(self, previous_proof: str) -> str:
        new_proof = 1
        check_proof = False
        #while loop will iterate until it finds a nonce needed to generate a sha256 hash string that has 4-leading zeros.
        #must be non symmetrical - must subtract each proofs
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    #takes a block as input and return sha256 hash of the block
    def hash(self, block: Dict) -> str:
        encoded_block = json.dumps(block, sort_keys=True).encode() #hashlib.sha256 requires encoded input
        return hashlib.sha256(encoded_block).hexdigest()  #returns the cryptographic hash of the block

    # checks that previous_hash of each block is equal to the hash of the previous block and the proof of each block is valid
    # iterates over each block of the chain and initialize checks
    def is_chain_valid(self, chain: List):
        previous_block = chain[0]
        block_index = 1
        while block_index < chain.__len__():
            current_block = chain[block_index]
            if current_block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block["proof"]
            current_proof = current_block['proof']
            hash_operation = hashlib.sha256(str(current_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = current_block  #update loop variables
            block_index += 1
        return True



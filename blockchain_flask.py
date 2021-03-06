from blockchain_backbone import Blockchain
from typing import Dict
from flask import Flask, jsonify

app=application=Flask(__name__)

blockchain = Blockchain()

@app.route('/mine_block', methods = ['GET'])
def mine_block() -> Dict:
    #mine a block - solve proof of work - create a block
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    current_proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    current_block = blockchain.create_block(current_proof,previous_hash)
    response = {"message": f"Congratulations, you have just mined block #{len(blockchain.chain)} in the blockchain!",
                "index": current_block['index'],
                "timestamp": current_block['timestamp'],
                "proof": current_block['proof'],
                "previous_hash": current_block['previous_hash']}
    return jsonify(response) , 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    #displays full blockchain
    response = {"chain": blockchain.chain,
                "length": len(blockchain.chain)}
    return jsonify(response) , 200



@app.route('/is_valid', methods=['GET'])
def valid_check():
    if blockchain.is_chain_valid(blockchain.chain):
        return "The Blockchain is valid"
    else:
        return "The Blockchain is NOT valid"




from blockchain_backbone import Blockchain
from typing import Dict
from flask import Flask, jsonify

app=application=Flask(__name__)

blockchain = Blockchain()

@app.route('/mine_block', methods = ['GET'])
def mine_block() -> Dict:
    #mine a block - solve proof of work - create a block
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    current_proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    current_block = blockchain.create_block(current_proof,previous_hash)
    response = {"message": f"Congratulations, you have just mined block #{len(blockchain.chain)} in the blockchain!",
                "index": current_block['index'],
                "timestamp": current_block['timestamp'],
                "proof": current_block['proof'],
                "previous_hash": current_block['previous_hash']}
    return jsonify(response) , 200

@app.route('/get_chain', methods=['GET'])
def get_chain():
    #displays full blockchain
    response = {"chain": blockchain.chain,
                "length": len(blockchain.chain)}
    return jsonify(response) , 200



@app.route('/is_valid', methods=['GET'])
def valid_check():
    if blockchain.is_chain_valid(blockchain.chain):
        response = {"status": "The Blockchain is valid!"}
    else:
        response = { "status": "The Blockchain is NOT valid!"}

    return jsonify(response), 200

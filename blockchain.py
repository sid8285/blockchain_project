import datetime as _date
import hashlib as _hashlib
import json as _json

class Blockchain:
    
    #instantiates the blockchain. Sets up the genesis block.
    def __init__(self) -> None:
        self.chain = list()     #the chain is basically a reversed linked list. Thats why we instantiate it as such.
        genesisBlock = self._create_block(data="This is the genesis block", proof=1, previousHash="0", index=1)
        self.chain.append(genesisBlock)
        
    #this function is to add a block to the chain. It takes in data and returns the block.
    #it first gets the previous block, then it gets the proof of work, then it gets the previous hash, then it creates the block and finally it appends the block to the chain.
    def mine_block(self, data: str) -> dict:
        prevBlock = self.getPreviousBlock()
        prevProof = prevBlock["proof"]
        index = len(self.chain) + 1
        proof = self.proofOfWork(prevProof, index, data)
        prevHash = self._hash(block=prevBlock)
        block = self._create_block(data=data, proof=proof, previousHash=prevHash, index=index)
        self.chain.append(block)
        return block
    
    #this function is to hash a block
    def _hash(self, block: dict) -> str:
        encodedBlock = _json.dumps(block, sort_keys=True).encode() #dumps is used to serialize a object into a json string, with the keys set to True, the keys are always sorted before returning; for consistent hashing. encode is to translate the string into bytes as sha-256 only takes in bytes
        
        return _hashlib.sha256(encodedBlock).hexdigest() #feeds the json string into a cryptographic hashing algorithm and then hexidigest is used to put it back into a tangible string.
    
    
    #not really sure what this is for either
    def toDigest(self, newProof: int, prevProof: int, index: str, data: str) -> bytes:
        to_digest = str(newProof ** 2 - prevProof ** 2 + index) + data #this is the formula. This is usually kept secret.
        return to_digest.encode()
    
    #this function is to solve for the proof
    def proofOfWork(self, prevProof: str, index: int, data: str) -> int:
        newProof = 1
        checkProof = False
        
        while not checkProof:
            toDigest = self.toDigest(newProof=newProof, prevProof=prevProof, index=index, data=data)
            hashVal = _hashlib.sha256(toDigest).hexdigest()
            if hashVal[:4] == "0000": #the amount of zeros dictate the complexity of your proof. less zeros are lighter, more are heavier
                checkProof = True
            else:
                newProof += 1
        
        return newProof
    
    #helper function to find the hash of the previous block in the chain
    def getPreviousBlock(self) -> dict:
        return self.chain[-1]
    
    #this method creates a block. The data, proof, prev hash and index are all passed in and a dictionary is returned.
    def _create_block(self, data: str, proof: int, previousHash: str, index: int) -> dict:
        block = {
            "index": index,
            "timestamp": str(_date.datetime.now()),
            "data": data,
            "proof": proof,
            "previousHash": previousHash,
        }
        
        return block
    
    #this method validates the chain. It checks if the hashes are correct and if the proof of work is valid.
    def isChainValid(self) -> bool:
        currentBlock = self.chain[0]
        blockIndex = currentBlock.get("index")
        while blockIndex < len(self.chain):
            nextBlock = self.chain[blockIndex]
            if nextBlock["previousHash"] != self._hash(currentBlock):
                return False
            currProof = currentBlock["proof"]
            nextIndex, nextData, nextProof = nextBlock["index"], nextBlock["data"], nextBlock["proof"]
            hashValue = _hashlib.sha256(self.toDigest(newProof=nextProof, prevProof=currProof, index=nextIndex, data=nextData)).hexdigest()
            
            if hashValue[:4] != "0000":
                return False
            
            currentBlock = nextBlock
            blockIndex += 1
            
        return True
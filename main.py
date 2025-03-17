import fastapi as _fastapi
import blockchain as _blockchain

blockchain = _blockchain.Blockchain() #instantiates the blockchain

app = _fastapi.FastAPI() #instantiates the fastapi app

#endpoint to mine a block
@app.post("/mine_block")
def mine_block(data: str):
    if blockchain.isChainValid() is True:
        block = blockchain.mine_block(data=data)
        return block
    else:
        raise _fastapi.HTTPException(status_code=400, detail="Chain is not valid")
    
#this is the endpoint to return the entire blockchain
@app.get("/blockchain/")
def get_chain():
    if blockchain.isChainValid() is True:
        return blockchain.chain
    else:
        raise _fastapi.HTTPException(status_code=400, detail="Chain is not valid")
    
#this endpoint returns the previous block within the chain
@app.get("/previous_block/")
def get_previous_block():
    if blockchain.isChainValid() is True:
        return blockchain.getPreviousBlock()
    else:
        raise _fastapi.HTTPException(status_code=400, detail="The chain is not valid.")
    
#this endpoint is to see if the blockchain is valid
@app.get("/isChainValid/")
def is_chain_valid():
    if blockchain.isChainValid() is True:
        return "The chain is valid."
    else:
        raise "The chain is not valid."
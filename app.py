import streamlit as st
from block import Block, Chain
from datetime import datetime
import pandas as pd

@st.cache(allow_output_mutation=True)
def start(): 
	genesis_block=Block(record=0, prev_hash='0', trade_time=datetime.utcnow().strftime('%H:%M:%S'))
	new_chain=Chain(chain=[genesis_block])
	return new_chain

chain=start()

st.title('Welcome to PyChain!')

shares=st.text_input('Please Input Number of Shares: ', '0 - 100')
if st.button('Submit'): 
	# get prev block (latest block)
	latest_block=chain.chain[-1]
	# hash prev block
	prev_hash=latest_block.hash_block()
	# create new block with prev_hash
	new_block=Block(record=shares, prev_hash=prev_hash, trade_time=datetime.utcnow().strftime('%H:%M:%S'))
	# add new block to chain
	chain.add_block(new_block)

# st.write(shares)

block_ledger=pd.DataFrame(chain.chain).astype(str)
st.write(block_ledger)

st.sidebar.subheader('Validate Hash:')
block_number=st.sidebar.selectbox('Choose Block Number:', range(len(chain.chain)))
if st.sidebar.button('Hash'): 
	block_hash=chain.chain[block_number].hash_block()
	st.sidebar.write(block_hash)

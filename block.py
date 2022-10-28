from dataclasses import dataclass

import hashlib

@dataclass
class Block(): 
    record: float
    prev_hash: str
    trade_time: str
    
    def hash_block(self): 
        sha=hashlib.sha256()
        trade_time_encoded=self.trade_time.encode()
        sha.update(trade_time_encoded)
        record_encoded=str(self.record).encode()
        sha.update(record_encoded)
        hash_encoded=self.prev_hash.encode()
        sha.update(hash_encoded)
        return sha.hexdigest()


from typing import List

@dataclass
class Chain(): 
    chain: List[Block]
    
    def add_block(self, new_block): 
        self.chain.append(new_block)
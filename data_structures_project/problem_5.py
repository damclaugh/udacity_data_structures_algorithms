

import hashlib
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = str(self.timestamp).encode('utf-8') + self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def get_hash(self):
        return self.hash


class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None
  
    def append(self, data):
        if self.head is None:
            self.head = Block(datetime.now(), data, 0)
            return
        
        block = self.head
        while block.next:
            block = block.next
      
        block.next = Block(datetime.now(), data, block.hash)

    def to_list(self):
        out_list = []
        block = self.head
        while block is not None:
            date_time = datetime.now()
            timestr = datetime.strftime(date_time, '%Y-%m-%d %H:%M:%S.%f')
            out_list.append([timestr, block.data, block.hash, block.previous_hash])
            block = block.next

        return out_list


# TEST CASE 1
blockchain1 = BlockChain()
blockchain1.append('data1')
blockchain1.append('data2')
blockchain1.append('data3')
block_items = blockchain1.to_list()
for item in block_items:
    print(item)
# ['2021-02-09 18:51:06.252126', 'data1', 
# '293013e8f565be0c25f35ea41266d079d949423e36a044e1064dfe07ed784f2d', 0]
# ['2021-02-09 18:51:06.252271', 'data2', 
# '68b3cef42627becb1622d10a0cdc2e31033e615d36474c27b434b19e38d573a4', 
# '293013e8f565be0c25f35ea41266d079d949423e36a044e1064dfe07ed784f2d']
# ['2021-02-09 18:51:06.252282', 'data3', 
# '65f0f235aff62f6502a41cc10d82710ea5a6915375065cfa419b3ac66370e1a0', 
# '68b3cef42627becb1622d10a0cdc2e31033e615d36474c27b434b19e38d573a4']


# TEST CASE 3
blockchain2 = BlockChain()
blockchain2.append('my balance: 10 | cash flow: +25 | final balance: 35')
blockchain2.append('my balance: 35 | cash flow: -15 | final balance: 20')
block_items = blockchain2.to_list()
for item in block_items:
    print(item)
# ['2021-02-09 18:51:06.252412', 'my balance: 10 | cash flow: +25 | final balance: 35', 
# 'a9998a5426d545301c4648e5f6a11e4a727e00a75c1f2096deb46c0f0ae820cf', 0]
# ['2021-02-09 18:51:06.252426', 'my balance: 35 | cash flow: -15 | final balance: 20', 
# '260f906babdcc38ab0c72af7fd80a99947f8e331bc65b7be9400a94974e81edf', 
# 'a9998a5426d545301c4648e5f6a11e4a727e00a75c1f2096deb46c0f0ae820cf']


# TEST CASE 2
blockchain3 = BlockChain()
blockchain3.append("")
blockchain3.append("")
block_items = blockchain3.to_list()
for item in block_items:
    print(item)
# ['2021-02-09 18:51:06.252472', '', 
# 'dd685107dbdf8d480f7c55fb488ef4f8757d8174be107a3ec930057241829ecf', 0]
# ['2021-02-09 18:51:06.252482', '', 
# 'e50c5fabd80f6c9e964a7b7c70253b63a1d12619fc05bbf7df89191beb75f8dc', 
# 'dd685107dbdf8d480f7c55fb488ef4f8757d8174be107a3ec930057241829ecf']




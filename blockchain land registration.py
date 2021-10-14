import hashlib #to hash using sha256
import datetime #for timestamp of the block
import random #for generating nonce
import sys #for size
#from flask import Flask, render_template

class block:
    def __init__(self, timestamp, prevhash, transdata, nexthash):
        self.timestamp = timestamp
        self.prevhash = prevhash
        self.transdata = transdata
        self.nexthash = self.grandhash
        self.hash = []
        self.chain = ()
        self.merkelroot = ()
    
    def genesisblock(self):
        print(block("08/06/2021", '0', "genesis", self.nexthash))
    
    #while sys.getsizeof(transdata) == 3145728 and sys.getsizeof(hash) == 3145728:
        
    def transact(self):
        ar = ()
        name = str(input("enter the name of the buyer"))
        uid = str(input("enter the uid of the buyer"))
        sp = int(input("enter the selling price of the land >. " + "/-"))
        r = int(input("enter the rate of tax >. " + "%"))
        #bhulekh data to be eneterd too...uid and name too of the buyer wrt the seller
        tax = sp-((r/100)*sp)
        arobj = ar.append(sp, r, tax, "this land belongs to the buyer .") #will also include bhulekh parameters too...
        dm = name + uid + tax
        return self.transdata.append(arobj)
            
    def nonceey(self):
        nonce = random.randint(0, 1000000)
        return nonce
    
    def hashing(self):
        hasher = hashlib.sha256(self.dm).hexdigest()
        ghash = hashlib.sha256(hasher + self.nonce).hexdigest()
        grandhash = hashlib.sha256(ghash).hexdigest()
        return self.hash.append(str(grandhash))
        

n = int(input("enter the number of transactions you want to add at a particular time >. "))

for i in range (0, n):
    block.str(datetime.datetime.now())
    block.hash[i-1] 
    block.arobj
    block.grandhash
    
class blockchian():

    def __init__(self, chain):
        self.chain = ()
    
    def merkel(self):
        noe = len(self.hash)
    
    # if sys.getsizeof(self.transdata) == 3145728 and sys.getsizeof(self.hash) == 3145728:
        
        if noe%2 == 0:
            for j in self.hash:
                s = j+(j+1)
                mrklrt = hashlib.sha256(s).hexdigest()
                return self.merkelroot.append(mrklrt)
        else:
            temp = ''
            self.hash[len(self.hash)-1] = temp
            for k in self.hash:
                su = k+(k+1)+temp+temp
                mrklrt = hashlib.sha256(su).hexdigest()
                return self.merkelroot.append(mrklrt)
                    
    def abc(self):
        bl = ''
        for l in self.merkelroot:
            for a in self.transdata:    
                bl = self.chain.append(self.merkelroot(l), self.merkelroot(l+1), self.transdata)
                
                f = open("blockchain output", "a")
                f.write(bl)
                f.close()


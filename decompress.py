import pickle
from functools import reduce
import time
import sys



with open('objs.pkl', 'rb') as f:
    vip,dict,padding=pickle.load(f)
#print(vip)



def a2bitsF(chars):
    return ''.join(format(ord(x), 'b').zfill(8) for x in chars)
    
def a2bitsS(chars):
    return bin(reduce(lambda x, y: (x << 8)+y, (ord(c) for c in chars), 1))[3:]




start_time = time.time()

bits = a2bitsF(vip)
#print(bits)

print("--- %s seconds ---" % (time.time() - start_time))



### decoding
temp = ''

dict = {v: k for k, v in dict.items()}  # reversing the dict

with open("ouput_d.txt", "wb") as o:
    for i in range(len(bits) - padding):
        temp = temp + bits[i]
       # print("\r{0}".format((float(i)/ (len(bits) - padding))*100))
        if temp in dict:
            o.write(dict[temp])
            temp = ''
o.close

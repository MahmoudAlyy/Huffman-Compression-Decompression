import pickle
from functools import reduce
import time
import sys


with open('objs.pkl', 'rb') as f:
    vip,dict,padding=pickle.load(f)


def a2bits(chars):
    return bin(reduce(lambda x, y: (x << 8)+y, (ord(c) for c in chars), 1))[3:]

bits = a2bits(vip)
print("HIIIIIII")
### decoding
temp = ''

dict = {v: k for k, v in dict.items()}  # reversing the dict

with open("ouput_d.txt", "wb") as o:
    for i in range(len(bits) - padding):
        temp = temp + bits[i]
        print("\r{0}".format((float(i)/ (len(bits) - padding))*100))
        if temp in dict:
            o.write(dict[temp])
            temp = ''
o.close

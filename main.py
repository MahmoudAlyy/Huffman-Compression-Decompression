import sys
import heapq
#from collections import defaultdict
import binascii
from functools import reduce


def encode(frequency):
    heap = [[weight, [symbol, '']] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))


dict = {}
with open("hi.txt", "rb") as f:
    byte = f.read(1)
    while byte:
        #print(type(byte))
        if byte in dict:
            temp = dict[byte] 
            dict[byte] = temp +1
        else:
            dict[byte] = 1

        byte = f.read(1)
        
#print(dict)


huff = encode(dict)


#print("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
#for p in huff:
 #   print(p[0], end=" ")
  #  print('\t', end=" ")
   # print(str(dict[p[0]]), end=" ")
   # print('\t', end=" ")
   # print(p[1], end=" ")
   # print("")


dict = {}
for p in huff:
    dict[p[0]] = p[1]
#print(dict)

############################################################################################################################
#print(huff(a))


def bits2a(b):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

def a2bits(chars):
    return bin(reduce(lambda x, y: (x << 8)+y, (ord(c) for c in chars), 1))[3:]

out =''
with open("hi.txt", "rb") as f:
    byte = f.read(1)
    while byte:
        temp = dict[byte]
        out = out + temp

        byte = f.read(1)

### padding
padding = 0
while (len(out) % 8 != 0 ):
    zero = '0'
    out = out + zero
    padding = padding + 1
    
count = len(out)
#print(count)
#print("###########################################################################################################################")

t1 = out
#print(out)
#print(bits2a(out))

#t2 = a2bits(bits2a(out))
#print(a2bits(bits2a(out)))


###

#print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
with open("ouput", "w", encoding="utf_8") as o:
    o.write(bits2a(out))
    o.close

with open("ouput", "r", encoding="utf_8") as o:
    content = o.read()
    o.close

for i in range(len(content)):
    if content[i] != bits2a(out)[i]:
        print("hi")
        #print(bits2a(out)[i])
        #print(content[i])
    


if content == bits2a(out):
    print("hmmmmmmmmmmmmmmmmm2?")

bits = a2bits(content)
t2 = bits
#print(bits)

### decoding
temp =''

dict = {v: k for k, v in dict.items()} # reversing the dict

with open("ouput_d.txt", "wb") as o:
    for i in range(len(bits) - padding):
        temp = temp + bits[i]
        #print(temp)
        if temp in dict:
           # print(temp)
            o.write(dict[temp])
            temp = ''
o.close


#ERROR IN WRITING FILE

#print(padding)

#print("hi?")
if t1 == t2 :
    print("HELLLLLLLLLL YHHHHHHHHHHH")

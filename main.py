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


print("Symbol".ljust(10) + "Weight".ljust(10) + "Huffman Code")
for p in huff:
    print(p[0], end=" ")
    print('\t', end=" ")
    print(str(dict[p[0]]), end=" ")
    print('\t', end=" ")
    print(p[1], end=" ")
    print("")


dict = {}
for p in huff:
    dict[p[0]] = p[1]
print(dict)

############################################################################################################################
#print(huff(a))


def bits2a(b):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))

#def a2bits(test_str):
 #   return ''.join(format(ord(i), 'b') for i in test_str)

def a2bits(chars):
    return bin(reduce(lambda x, y: (x << 8)+y, (ord(c) for c in chars), 1))[3:]

out =''
with open("hi.txt", "rb") as f:
    byte = f.read(1)
    while byte:
        temp = dict[byte]
        out = out + temp

        byte = f.read(1)

while (len(out) % 8 != 0 ):
    zero = '0'
    out = out + zero
    
count = len(out)
print(count)
print("#################################")
print(out)
print(bits2a(out))
print(a2bits(bits2a(out)))


#with open("ouput.txt", "w") as o:

import heapq
#from functools import reduce
import pickle
import time

import sys
import os.path


def main():
    print("Enter Name of File: ", end=" ")
    filename = input()

    print("Compress or Decompress (c/d) ?", end=" ")
    method = input()

    if method == 'c':
        compress(filename)
    elif method == 'd':
        decompress(filename)
    else:
        print("Invalid, Try again")
        main()



def bits2a(b):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))


def a2bits(chars):
    return ''.join(format(ord(x), 'b').zfill(8) for x in chars)


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


def countFreq(filename):
    dict = {}
    with open(filename, "rb") as f:
        byte = f.read(1)
        while byte:
            if byte in dict:           
                temp = dict[byte] 
                dict[byte] = temp +1
            else:
                dict[byte] = 1
            byte = f.read(1)
    f.close  
    return dict      


### COMPRESS
def compress(filename) :
    start_time = time.time()

    dict = countFreq(filename)
    huff = encode(dict)

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




    out =''
    with open(filename, "rb") as f:
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


    vip = bits2a(out)

    extension = os.path.splitext(filename)[0]
    output_filename = extension + '.comp'

    with open(output_filename, 'wb') as f:
            pickle.dump([vip,dict,padding], f)


    print("Compressing Time: --- %s seconds ---" % (time.time() - start_time))


### DECOMPRESS

def decompress(fileName):
    start_time = time.time()

    with open(fileName, 'rb') as f:
        vip, dict, padding = pickle.load(f)

    bits = a2bits(vip)
    temp = ''

    dict = {v: k for k, v in dict.items()}  # reversing the dict

    with open("ouput", "wb") as o:
        for i in range(len(bits) - padding):
            temp = temp + bits[i]
            if temp in dict:
                o.write(dict[temp])
                temp = ''
    o.close

    print("Decompressing Time: --- %s seconds ---" % (time.time() - start_time))





if __name__ == '__main__':

    main()
    

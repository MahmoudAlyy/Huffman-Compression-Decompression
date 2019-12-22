import heapq
import pickle
import time
import sys
import os.path
import os
from Node import *
import queue as Q

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

#############################################################################################################################################################


def huffman(charFreq):
    n = len(charFreq)
    heap = []
    for item in charFreq.items():
        #print(item)
        node = Node(item[0], item[1], None, None, None, None)
        heapq.heappush(heap, (node.freq, node))
    if n == 1:
        x = heapq.heappop(heap)
        #zVal = x[0]
        #z = Node(None, zVal, x[1], None, None, None)
        x[1].code = str(1)
        #x[1].parent = z
        heapq.heappush(heap, (x[1].freq, x[1]))
        return heapq.heappop(heap)

    for _ in range(n - 1):
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        zVal = x[0] + y[0]
        z = Node(None, zVal, x[1], y[1], None, None)
        x[1].code = str(0)
        y[1].code = str(1)
        x[1].parent = z
        y[1].parent = z
        heapq.heappush(heap, (z.freq, z))
    return heapq.heappop(heap)


def huffTreeCode(node):
    qu = Q.Queue()

    qu.put(node)

    while not qu.empty():
        state = qu.get()
        if state.parent is not None:
            if state.parent.code is not None:
                state.code += state.parent.code
        if state.left is not None:
            qu.put(state.left)
        if state.right is not None:
            qu.put(state.right)


def saveCodes(node):
    codes = {}
    qu = Q.Queue()

    qu.put(node)

    while not qu.empty():
        state = qu.get()
        if state.char is not None:
            codes[state.char] = state.code[::-1]
            print(state.char, end=" ")
            print('\t', end=" ")
            print(state.freq, end=" ")
            print('\t', end=" ")
            print(state.code[::-1] ,end=" ")
            print("")
        if state.left is not None:
            qu.put(state.left)
        if state.right is not None:
            qu.put(state.right)

    return codes













#############################################################################################################################################################



def bits2a(b):
    return ''.join(chr(int(''.join(x), 2)) for x in zip(*[iter(b)]*8))


def a2bits(chars):
    return ''.join(format(ord(x), 'b').zfill(8) for x in chars)

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


############# COMPRESS
def compress(filename) :
    start_time = time.time()

    
    if os.path.isdir(filename) :
        file_compress(filename)
    else :

        dict = countFreq(filename)

        ########## BASEMMMMMM
        root = huffman(dict)[1]

        huffTreeCode(root)

        codes = saveCodes(root)
        out =''
        with open(filename, "rb") as f:
            byte = f.read(1)
            while byte:
                temp = codes[byte]
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
        ext = os.path.splitext(filename)[1]
        output_filename = extension + '.comp'

        with open(output_filename, 'wb') as f:
                pickle.dump([vip,codes,padding,ext], f)

        uncompressed_size = os.path.getsize(filename)
        compressed_size = os.path.getsize(output_filename)
        #print(uncompressed_size)
        #print(compressed_size)
        print("Compression Ratio = ",end=" ")
        print(uncompressed_size/compressed_size)

        print("Compressing Time: --- %s seconds ---" % (time.time() - start_time))


### DECOMPRESS

def decompress(fileName):
    start_time = time.time()

    with open(fileName, 'rb') as f:
        vip, dict, padding,ext = pickle.load(f)

    bits = a2bits(vip)
    temp = ''

    dict = {v: k for k, v in dict.items()}  # reversing the dict

    output_name = fileName + ext
    with open(output_name, "wb") as o:
        for i in range(len(bits) - padding):
            temp = temp + bits[i]
            if temp in dict:
                o.write(dict[temp])
                temp = ''
    o.close

    print("Decompressing Time: --- %s seconds ---" % (time.time() - start_time))


def file_compress(filename):
    dict = {}
    slash = '\\'
    dir_list = []
    dir_list.append(filename)

    while len(dir_list) != 0:
        current = dir_list.pop()
        for root, dirs, files in os.walk(current):
            dict[root] = files
            for item in dirs:
                temp = str(root) + slash + str(item)
                dir_list.append(temp)


if __name__ == '__main__':

    main()
    

dict = {}
with open("hi2", "rb") as f:
    byte = f.read(1)
    while byte:
        #print(type(byte))
        if byte in dict:
            temp = dict[byte] 
            dict[byte] = temp +1
        else:
            dict[byte] = 1

        byte = f.read(1)
        
print(dict)
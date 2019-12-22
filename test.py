import binascii 

str = "abs"

 # bytes

a =''.join(format(ord(x), 'b') for x in str)

def get_bin(x): return format(x, 'b')


#data = get_bin(str)
print( a )

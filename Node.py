class Node:
    def __init__(self, char, freq, left, right, code, parent):
        self.char = char
        self.freq = freq
        self.right = right
        self.left = left
        self.code = code
        self.parent  = parent

    def __lt__(self, other): #function to compare the nodes , it is as if our class implments the interface Comparable 

        return self.freq < other.freq
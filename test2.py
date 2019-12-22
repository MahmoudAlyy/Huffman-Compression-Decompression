import os
filename = 'hi2'

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

print(dict)
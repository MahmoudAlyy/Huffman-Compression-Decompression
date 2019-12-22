import glob
import os

slash = '\\'
dict = {}

dir_list = []


input = 'hi2'


filename = input
dir_list.append(input)
dict[filename] = []


while len(dir_list) != 0:

    current_file = dir_list.pop()
    print(current_file)
    list = os.listdir(current_file)

    for item in list :
        #print(item)
        temp = current_file + slash + str(item)
        if os.path.isfile(temp):
            dict[temp].append(item)
        else :
            temp = current_file + slash + str(item)
            print("dir is ="+temp)
            dir_list.append(temp)

    filename = filename + slash + str(current_file)
    

print(dict)
print(dir_list)

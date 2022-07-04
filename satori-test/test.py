# # import OS module
# import os

# # Get the list of all files and directories
# path = "./satori-cli"
# dir_list = os.listdir(path)


# print("Files and directories in '", path, "' :")

# # prints all files
# print("\n",dir_list)



# for x in dir_list:
# 	if x.endswith(".yml"):
# 		# Prints only text file present in My Folder
# 		print("Playbooks \n",x)



# Satori cli Define Functions

# import os

# path = "./satori-cli/playbooks"

# fileNames = []

# def fileFinder():
# 	for file in os.listdir(path):
# 		if file.endswith(".yml"):
# 			fileNames.append(file)


# import OS module
# import os

# # This is my path
# path = "./satori-cli/playbooks"

# # to store files in a list
# fileNames = []

# # dirs=directories
# for (root, dirs, file) in os.walk(path):
# 	for f in file:
# 		if '.yml' in f:
# 			print(f)

# import os
# path = './path/to/files/'


# def fileFinder():
# 	for (subdir, dirs, files) in os.walk(path):
# 		fileNames = []
# 		if filesEndswith('.yml'):


# import os

# path= "./satori-cli/playbooks"

# List_of_Subdirectories = list(filter(os.path.isdir, os.listdir()))
# print(List_of_Subdirectories)

# directory_elements = filter(os.path.isdir, os.listdir())
# List_of_Subdirectories = []
# for element in directory_elements:
#     List_of_Subdirectories.append(element)
# print(List_of_Subdirectories)

import os 

path = "../Desarrollo/satori-cli/playbooks"

import os
def fn():       
    file_list=os.listdir(path)
    print (file_list)


print('Playbooks'),fn()


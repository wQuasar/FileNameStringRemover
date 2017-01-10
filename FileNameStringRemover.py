# Simple script to rename all the files in a folder by removing a certain substring from the name.
# Using a pretty simple approach for string search but, it does the job in most cases. 

import os

# Method to do most of the grunt work. Get the list of files in a dir and then remane it
def removeString(sub_string):
	file_list = os.listdir(".")

	for file in file_list:
		if os.path.isfile(file):
			if file != "StringRemover.py":
				new_name = getNewName(file.split(), sub_string.split())

				# Renaming only is a valid name change
				if (new_name == ""):
					print ("Did you just try to remove the entirety of: " + file + " !!!")

				elif (new_name != file): 
					print (file + " -> " + new_name)
					os.rename(file, new_name)


# Get the new name of the file as a string after removing the substring
def getNewName(old_name, sub_string):
	extension = old_name[len(old_name) -1][old_name[len(old_name) - 1].find("."):]
	old_name[len(old_name) - 1] = old_name[len(old_name) -1][:old_name[len(old_name) - 1].find(".")]

	# Traversing through the entire name
	for i in range(len(old_name) - len(sub_string) + 1):
		if (old_name[i] == sub_string[0]):
			# Vars to keep track of the indexes
			begin = i
			end = i

			# Found the name! Let's traverse futher to find if its present in its entirety
			for j in range(1, len(sub_string)):
				if old_name[i + j] != sub_string[j]:
					end = -1
					break
				else:
					end += 1

			# end == -1 indicates that the string was not present in its entirety
			if end != -1:
				for k in range(begin, end + 1):
					old_name[k] = ""

	# if the entire name is "", just return that (will not be renamed)
	if (old_name == [""]):
		return ""

	# Reducing the old_name list untile we end up on a valid index (This is a fix for extension being added to empty string)
	while(old_name[len(old_name) - 1] == ""):
		old_name = old_name[:len(old_name) - 1]

	# Adding the exension to the last index
	old_name[len(old_name) - 1] = old_name[len(old_name) - 1] + extension

	# Finally removing the stripped indices (i.e. indices with "")
	try :
		return " ".join([x for x in old_name if x != ""])
	except ValueError:
		return " ".join(old_name)


# Main init method
def init():
	print ("** KEEP BACKUPS YOU PUNK! **\n")
	sub_string = input("Enter the substring to be removed from the file names in this folder: ")

	print ("----- BEGIN PROCESSING -----")

	if (sub_string != ""):
		removeString(sub_string)
	else :
		print ("WTF! You entered nothing?!")

	print ("\n----- END PROCESSING ----- ")

# Self start
init()
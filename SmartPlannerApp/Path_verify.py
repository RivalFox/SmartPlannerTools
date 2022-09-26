def path_verify(path):
	if path.exists() == True:
		print("The directory does exist")
	else:
		print("The directory does not exist")
		exit()
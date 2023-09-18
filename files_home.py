def compile_files(path):
	data = {}
	for file_ in path:
		if file_.endswith("txt"):
			with open(file_, encoding="utf-8") as f:
				file_data = f.readlines()
				data[len(file_data)] = (file_, " ".join(file_data))


	
	data = dict(sorted(data.items()))
	
	


	with open("result_data", 'w', encoding="utf-8") as new_file:
		for key, value in data.items():
			new_file.write(f"{value[0]} \n")
			new_file.write(f"{key} \n")
			new_file.write(f"{value[1]}\n\n")

compile_files('files')
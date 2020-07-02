if __name__ == '__main__':
	print("hello world")

	#reading a program file from the folder
	program_file = open('program_files\\test.py', 'r')
	program_code = program_file.read()
	print(program_code)
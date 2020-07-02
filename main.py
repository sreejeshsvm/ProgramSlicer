import re
import nltk
import keyword

#global varaiables
PY_KEYWORDS = "False|None|True|and|as|assert|break|class|continue|def|del|elif|else|except|finally|for|from|global|if|import|in|is|lambda|nonlocal|not|or|pass|raise|return|try|while|with|yield"
PY_OPERATORS = ""


def GetAllKeywords():
	keywords = str(keyword.kwlist)
	keywords = str(re.sub("'", "", keywords))
	keywords = str(re.sub(",", "|", keywords))
	keywords = str(re.sub("\s", "", keywords))
	print(keywords)

if __name__ == '__main__':

	#GetAllKeywords()

	#reading a program file from the folder
	program_file = open('program_files\\my_program.py', 'r')
	program_code = program_file.readlines()

	for line in program_code:
		tokens = nltk.word_tokenize(line)
		for token in tokens:
			print(token)	
			print("----------------line end-----------------")
			# print(re.findall(PY_KEYWORDS, token))




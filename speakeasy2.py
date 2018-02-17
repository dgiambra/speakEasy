import subprocess
import nltk

class REPL:

	def __init__(self, library, system):
		self._library = library
		self._core_commands = system
		self._history = []
		self._gloss = None


	def loop(self):
		print("Welcome!")
		while True:
			try:
				scan = str(input('SE >> '))
				processor(scan)
				print(output)
			except Exception as e:
				print("Error..."+str(e))

	def list():
		subprocess.call(["ls", "-a"])

	def remove(type, name):
		if(type == "folder"):
			removeFolder(name)
		if(type == "file"):
			removeFile(name)

	def removeFile(file):
		subprocess.call("rm ./{}".format(file), shell=True)

	def removeFolder(folder):
		subprocess.call("rmdir {}".format(folder), shell = True)

	def make(type, name):
		if(type == "folder"):
			makeFolder(name)
		if(type == "file"):
			makeFile(name)

	def makeFolder(name):
		subprocess.call("mkdir {}".format(name), shell = True)

	def makeFile(name):
		subprocess.call("touch {}".format(name), shell = True)	

	def tokenize(command):
		return nltk.word_tokenize(command)

	def run(fileName):
		if(".py" in fileName and (".c" and ".java" and ".cpp" not in fileName)):
			print("Hello")
			runPython(fileName)
		if(".c" in fileName and (".py" and ".java" and ".cpp"  not in fileName)):
			runC(fileName)
		if(".java" in fileName and(".py" and ".c" and ".cpp" not in fileName)):
			runJava(fileName)
		if(".cpp" in fileName and(".py" and ".c" and ".java" not in fileName)):
			runCpp(fileName)

	def runPython(fileName):
		subprocess.call("python3 {}".format(fileName), shell = True)	
			

	def runC(fileName):
		subprocess.call("gcc -Wall {0} -o {1}".format(fileName, fileName[:-2]),shell = True)
		subprocess.call("./{}".format(fileName[:-2]), shell = True)


	def runJava(fileName):
		subprocess.call("javac {}".format(fileName),shell = True)
		subprocess.call("java {}".format(fileName[:-5]), shell = True)

	def runCpp(fileName):
		subprocess.call("g++ {0} -o {1}".format(fileName, fileName[:-4]), shell = True)
		subprocess.call("./{}".format(fileName[:-4]), shell = True)

	def processor(command):
		tokens = tokenize(command)
		firstWord = tokens[0]
		##print(firstWord)
		if (firstWord =="list"):
			##print("true")
			list()
		if (firstWord == "delete"):
			for x in tokens:
				if(x == "folder"):
					type = "folder"
					index = tokens.index(x)
				if (x == "file"):
					type = "file"
					index = tokens.index(x)
			remove(type, tokens[index + 1])	
		if (firstWord == "make"):
			for x in tokens:
				if (x == "folder"):
					type = "folder"
					index = tokens.index(x)
				if (x == "file"):
					type = "file"
					index = tokens.index(x)
			make(type, tokens[index + 1])
		if (firstWord == "run"):
			run(tokens[1])


def main():
	
	library = {
		'cd':[]
	}

	system = {
		'exit':['exit','leave','go away']
	}

	r = REPL(library=library, system=system)
	r.loop()




# process = Popen(['cat', 'test.py'], stdout=PIPE, stderr=PIPE)
# stdout, stderr = process.communicate()
# print stdout
main()
import subprocess
import nltk

class REPL:

	def __init__(self, library, system):
		self._library = {
		'list':self.list,
		'delete':{'file': self.removeFile,'folder' : self.removeFolder} ,
		'make': {'file' : self.makeFile, 'folder' : self.makeFolder},
		'run':self.run,

		}

		self._core_commands = system
		self._history = []
		self._gloss = None
		self._loop = True


	def loop(self):
		print("Welcome!")
		while self._loop:
			##try:
			scan = str(input('Enter a Command >> '))
			self.processor(scan)

			##except Exception as e:
				##print("Error..."+str(e))

	def list(self):
		subprocess.call(["ls", "-a"])

	def remove(self, type, name):
		if(type == "folder"):
			self.removeFolder(name)
		if(type == "file"):
			self.removeFile(name)

	def removeFile(self, file):
		subprocess.call("rm ./{}".format(file), shell=True)

	def removeFolder(self, folder):
		subprocess.call("rmdir {}".format(folder), shell = True)

	def make(self, type, name):
		if(type == "folder"):
			self.makeFolder(name)
		if(type == "file"):
			self.makeFile(name)

	def makeFolder(self, name):
		subprocess.call("mkdir {}".format(name), shell = True)

	def makeFile(self, name):
		subprocess.call("touch {}".format(name), shell = True)	

	def tokenize(self, command):
		return nltk.word_tokenize(command)

	def run(self, fileName):
		if(".py" in fileName and (".c" and ".java" and ".cpp" not in fileName)):
			#print("Hello")
			self.runPython(fileName)
		if(".c" in fileName and (".py" and ".java" and ".cpp"  not in fileName)):
			self.runC(fileName)
		if(".java" in fileName and(".py" and ".c" and ".cpp" not in fileName)):
			self.runJava(fileName)
		if(".cpp" in fileName and(".py" and ".c" and ".java" not in fileName)):
			self.runCpp(fileName)

	def runPython(self, fileName):
		subprocess.call("python3 {}".format(fileName), shell = True)


	def runC(self, fileName):
		subprocess.call("gcc -Wall {0} -o {1}".format(fileName, fileName[:-2]),shell = True)
		subprocess.call("./{}".format(fileName[:-2]), shell = True)


	def runJava(self, fileName):
		subprocess.call("javac {}".format(fileName),shell = True)
		subprocess.call("java {}".format(fileName[:-5]), shell = True)

	def runCpp(self, fileName):
		subprocess.call("g++ {0} -o {1}".format(fileName, fileName[:-4]), shell = True)
		subprocess.call("./{}".format(fileName[:-4]), shell = True)

	def processor(self, command):
		tokens = self.tokenize(command)
		firstWord = tokens[0]
		if (firstWord == ("make" or "delete")):
			self._library[firstWord][tokens[1]](tokens[2])
		elif firstWord == "run":
			self._library[firstWord](tokens[1])
		elif firstWord =="list":
			self._library[firstWord]()
			
		if (firstWord == "quit"):
			self._loop = False
def main():
	
	library = {}

	system = {
		'exit':['exit','leave','go away']
	}

	r = REPL(library=library, system=system)
	r.loop()




# process = Popen(['cat', 'test.py'], stdout=PIPE, stderr=PIPE)
# stdout, stderr = process.communicate()
# print stdout
main()

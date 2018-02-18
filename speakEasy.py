import subprocess
import nltk
from os import chdir

class REPL:

	def __init__(self, library, system):
		self._library = {   #This library functions as a switch statement
		'list':self.list,   #The key is the intent word, the value is the corresponding function
		'delete':{'file': self.removeFile,'folder' : self.removeFolder} ,
		'make': {'file' : self.makeFile, 'folder' : self.makeFolder},
		'run':self.run,
		'locate': self.locate,
		'move':self.move
		}

		self._translations = system #data for translation
		self._history = []
		self._gloss = None
		self._loop = True

	def translator(self, word):
		'''convert command into intent, uses a dictionary of synonyms to translate 
		Args:
		word(str) -- the word to translate
		
		Return:
		word(str) -- word translated to intent '''
		for i in self._translations:
			if word in self._translations[i]:
				return i
			else:
				return word

	def loop(self):
		'''loop to keep command prompt open and take input'''
		print("Welcome!")
		while self._loop:
			try:
				scan = str(input('Enter a Command >> ')) #Get command
				self.processor(scan)                     #Process command

			except Exception as e:
				print("Error..."+str(e))

	def list(self):
		'''function to list contents of current directory'''
		subprocess.call(["ls", "-a"])

	def remove(self, type, name):
		'''a splitter function to differentiate between file and folder removal
		
		Args:
		type(str) -- file or folder
		name(str) -- file or folder name'''
		if(type == "folder"):
			self.removeFolder(name)
		if(type == "file"):
			self.removeFile(name)

	def removeFile(self, file):
		''' function to remove file'''
		subprocess.call("rm ./{}".format(file), shell=True)

	def removeFolder(self, folder):
		'''function to remove folder'''
		subprocess.call("rmdir {}".format(folder), shell = True)

	def make(self, type, name):
		'''a splitter function to differentiate between file and folder creation
		
		Args:
		type(str) -- file or folder
		name(str) -- file or folder name'''
		if(type == "folder"):
			self.makeFolder(name)
		if(type == "file"):
			self.makeFile(name)

	def makeFolder(self, name):
		'''a function to make a folder'''
		subprocess.call("mkdir {}".format(name), shell = True)

	def makeFile(self, name):
		'''a function to make a file'''
		subprocess.call("touch {}".format(name), shell = True)	

	def tokenize(self, command):
		'''a function to split a word into its tokens (words)
		
		Returns:
		tokens(List[str]) -- a list of words input'''
		return nltk.word_tokenize(command)

	def run(self, fileName):
		'''a splitting function to determine file type for execution
		
		Args:
		fileName(str) -- name of executable'''
		if(".py" in fileName and (".c" and ".java" and ".cpp" not in fileName)):
			#print("Hello")
			self.runPython(fileName)
		if(".c" in fileName and (".py" and ".java" and ".cpp"  not in fileName)):
			self.runC(fileName)
		if(".java" in fileName and(".py" and ".c" and ".cpp" not in fileName)):
			self.runJava(fileName)
		if(".cpp" in fileName and(".py" and ".c" and ".java" not in fileName)):
			self.runCpp(fileName)
		if(".rb" in fileName):
			self.runRuby(fileName)

	def runPython(self, fileName):
		'''a function to run a python3 executable
		
		Args:
		fileName(str) -- name of executable'''
		subprocess.call("python3 {}".format(fileName), shell = True)


	def runC(self, fileName):
		'''a function to compile and run a c executable
		
		Args:
		fileName(str) -- name of executable'''
		subprocess.call("gcc -Wall {0} -o {1}".format(fileName, fileName[:-2]),shell = True)
		subprocess.call("./{}".format(fileName[:-2]), shell = True)


	def runJava(self, fileName):
		'''a function to compile and run a Java executable
		
		Args:
		fileName(str) -- name of executable'''
		subprocess.call("javac {}".format(fileName),shell = True)
		subprocess.call("java {}".format(fileName[:-5]), shell = True)

	def runCpp(self, fileName):
		'''a function to compile and run a C++ executable
		
		Args:
		fileName(str) -- name of executable'''
		subprocess.call("g++ {0} -o {1}".format(fileName, fileName[:-4]), shell = True)
		subprocess.call("./{}".format(fileName[:-4]), shell = True)
		
	def runRuby(self, fileName):
		'''a function to run a ruby executable
		
		Args:
		fileName(str) -- name of executable'''
		#print("huh")
		subprocess.call("ruby {}".format(fileName), shell = True)
	def processor(self, command):
		'''Novel 'Language Processing' Algorithm
		
		Args:
		command(str) -- command text'''
		tokens = self.tokenize(command)
		firstWord = self.translator(tokens[0])
		#print(firstWord)
		if (firstWord in ("make" , "delete")):
			self._library[firstWord][tokens[1]](tokens[2])
		elif (firstWord in ("run" , "locate", "move")):
			#print('but')
			self._library[firstWord](tokens[1])
		elif (firstWord =="list"):
			self._library[firstWord]()
		elif (firstWord == "exit"):
			print('love')
			self._loop = False

	def locate(self, fileName):
		'''a function to locate a file or folder 
		
		Args:
		fileName(str) -- name of file or folder to locate'''
		#print("locate -b '\{}'".format(fileName))
		subprocess.call("locate -b '\{}'".format(fileName),shell = True)
		#print(output)

	def move(self, fileName):
		'''a function to move the current working directory
		
		Args:
		fileName(str) -- directory to enter'''
		output = subprocess.check_output("locate -bc '\{}'".format(fileName), shell = True)
		output = int(output[:-1])
		if output == 1:
			op = subprocess.check_output("locate -b '\{}'".format(fileName), shell = True)
			#print(str(op[:-1]))
			string = str(op)[2:-3]
			chdir(string)	
		else:
			print("Unable to locate {}".format(fileName))	


def main():
	
	library = {}

	system = {
		'exit':['exit','leave', 'quit'],            #This is an editable "dictionary" 
		'make':['make','create'],                   #Keys are intents
		'delete':['delete', 'remove', 'destroy'],   #Values or synonyms that will trigger intent
		'locate':['locate','search','find']
	}

	r = REPL(library=library, system=system)
	r.loop()




# process = Popen(['cat', 'test.py'], stdout=PIPE, stderr=PIPE)
# stdout, stderr = process.communicate()
# print stdout
main()

import nltk
import subprocess

def getCommand():
	command = input("Command: ")
	return command

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
	if(".py" in fileName and (".c" and ".java" not in fileName)):
		runPython(fileName)
	if(".c" in fileName and (".py" and ".java" not in fileName)):
		runC(fileName)
	if(".java" in fileName and(".py" and ".c" not in fileName)):
		runJava(fileName)

def runPython(fileName):
	fileName	
		

def runC(fileName):
	return True
def runJava(fileName):
	return True
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



def speakEasy():
	command = getCommand()
	processor(command)

speakEasy()



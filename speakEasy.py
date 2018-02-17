import nltk
import subprocess

def getCommand():
	command = input("Command: ")
	return command

def list():
	subprocess.call(["ls", "-a"])

def remove(file):
	subprocess.call("rm ./{}".format(file), shell=True)


def tokenize(command):
	return nltk.word_tokenize(command)

def processor(command):
	tokens = tokenize(command)
	firstWord = tokens[0]
	##print(firstWord)
	if (firstWord =="list"):
		##print("true")
		list()
	if (firstWord == "delete"):
		file = tokens[1]
		remove(file)	
def speakEasy():
	command = getCommand()
	processor(command)

speakEasy()


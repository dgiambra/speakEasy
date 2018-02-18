#This code has not been implemented as of version 1.0. This is a proof of concept custom entity recognizer custom built for command line syntax.

import subprocess

class REPL:

	def __init__(self, library, synonyms, vocabulary):
		self.library = library
		self.synonyms = synonyms
		self.vocabulary = vocabulary
		self.history = []
		self.corpus = []
		for v in self.synonyms.values():
			self.corpus.extend(v)

	def loop(self):
		"""REPL loop."""
		print("Welcome! Type commands, then enter to evaluate them.\n")
		while True:
			try:
				scan = str(input('SE >> '))
				if len(self.history) > 50:
					self.history = self.history[1:]
				self.history.append(scan)
				gloss = self.parse(scan)
				output = self.execute(gloss)
				self.display(output)
			except Exception as e:
				print("Error..."+str(e))

	def parse(self, string):
		"""Process string."""
		#Split and clean string
		tokens = string.split()
		while '' in tokens:
			tokens.remove('')
		#Use '=' keyword to pipe straight to CLI
		if tokens[0] is '=':
			return ' '.join(tokens[1:])
		#Match tokens to entities
		parts = []
		for t in tokens:
			parts.append(self.match_tokens(t))

		#Verify entities map to valid CFG phrase structure
		valid_phrase = self.match_syntax(parts)
		if not valid_phrase:
			return self.error(msg="Unable to parse to English.")


		print(parts)
		return parts


	def match_tokens(self, token):
		"""Match string tokens to entities."""
		if token not in self.corpus:
			return (token, '')
		matches = []
		for POS,POSsets in self.vocabulary.items(): #For all synonmys of a part of speech
			for item in POSsets:
				if any([token in self.synonyms[item]]):
					matches.append((item, POS))
		return tuple(matches)

	def match_syntax(self, parts):
		"""Match entities to a CFG fragment of natural English."""
		return True #TODO

	def execute(self, command):
		"""Pipe text to command line for execution."""
		return subprocess.check_output(command, shell=True)

	def display(self, output):
		"""Format and display response from CLI."""
		out = output.decode("utf-8").splitlines()
		for line in out:
			print(line.rstrip())

	def error(self, msg):
		"""Alert use of error on screen."""
		return "echo "+str(msg)

def main():
	"""Main method."""
	if __name__== "__main__":
		synonyms = {
			#COM
			"ls":		['ls','dir','list','show','display'],
			"cd":		['go', 'jump', 'change','open'],
			"exit":		['exit','leave','go away'],
			"rm":		['rm','remove','delete','erase'],
			"rmdir":	['rmdir','remove','delete','erase'],
			"cat":		['cat','touch','less','nano','read','print'],
			#MOD
			"all":		['all','every','each'],
			"none":		['none','no','zero'],
			"this":		['this','current','working'],
			"answer":	['answer','ans','last','previous'],
			#OBJ
			"file":		['file','files','item','items','contents'],
			"folder":	['folder','folders','directory','directories','contents'],
			"path":		['path','filepath','location'],
			#PRP
			"to":		['to'],
			"in":		['in'],
			#CNJ
			"and":		['and'],
			"or":		['or']
		}

		vocabulary = { #When adding to vocab, also add to synonmys
			"COM":['ls','cd','exit','rm','rmdir','cat'],
			"MOD":['all','none','this','answer'],
			"OBJ":['file','folder','path'],
			"PRP":['to','in'],
			"CNJ":['and','or'],

		}

		library = {
			"ls":		[],
		}

		r = REPL(library, synonyms, vocabulary)
		r.loop()
		
#Activate main		
main()
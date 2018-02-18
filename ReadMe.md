# speakEasy

This is a Natural Language Interface for the UNIX terminal written in Python for the 2018 Dandyhacks.
It was written by Dominic Giambra (University of Rochester, Chemical Engineering, 2018) and Tyler Knight (University of Rochester, Computer Science, 2019)

## Getting Started

Download this directory, however only the speakEasy.py file is necessary for complete functionality.
The navigate to the directory and run the following command.
```
python3 speakEasy.py
```
If your Python 3 path variable is not python3 but instead python, enter the following.
```
python speakEasy.py
```
Note: If you do not have the python3 path variable the interface will be unable to run other python scripts.

### Prerequisites

The following programs will be needed:
* gcc (to compile C programs)
* g++ (to compile C++)
* default-javardk (to compile JAVA programs)
* Python 3

The following python packages will be needed:
* NLTK
* subprocess
* os


### Instructions
After running the Python executable a prompt should appear. That is the Natural Language interface.
It currently supports eleven different operations. An example of each follows.

#### View Contents of Current Directory
To view contents of the current directory type any command containing the world list.
```
Enter a Command >> list all files
```
 
#### Make a File
To make a file enter the words "make file" followed by the file name. If I wanted to create hello.txt I would do:
```
Enter a Command >> make file hello.txt
```

#### Make a Folder
To make a folder enter the words "make folder" followed by the folder name. If I wanted to create hello I would do:
```
Enter a Command >> make folder hello
```

#### Remove a File
To remove a file enter the words "remove file" followed by the file name. If I wanted to remove hello.txt I would do:
```
Enter a Command >> remove file hello.txt
```

#### Remove a Folder
To remove a folder enter the words "remove folder" followed by the folder name. If I wanted to remove hello I would do:
```
Enter a Command >> remove folder hello
```

#### Run an Executable (.c, .py, .cpp, .rb,  and .java)
One of the most novel features in this interface is the ability to compile and run multiple types of programs with a simple command.
```
Enter a Command >> run hello.py
```
```
Enter a Command >> run hello.c
```
```
Enter a Command >> run hello.cpp
```
```
Enter a Command >> run hello.java
```
```
Enter a Command >> run helo.rb
```

#### Locate a File or Folder
Enter the name of a file or folder and the Interface will display anything with the same title as entered.
```
Enter a Command >> locate gui.python
```
#### Move Working Directory
Enter the name of a folder or directory to move to that directory. Note, only the name, not the path is needed.
```
Enter a Command >> move Hackathon18
````

#### Exit
To quit, type exit.
```
Enter a Command >> exit
```
### Demo Programs
All files besides the speakEasy.py, speakEasy_OLDSTABLE.py, and ReadMe.md are demo files. All of them can be compiled and run from the Interface, including the GUI.

### Future Engine
This code has not been implemented as of version 1.0. This is a proof of concept custom entity recognizer custom built for command line syntax.

### Alternative commands
The following commands can be subbed in with no loss in functionality.
* exit
	* exit
	* leave
	* quit
* make
	* make
	* create
* delete
	* delete
	* remove
	* destroy
* locate
	* locate
	* search
	* find

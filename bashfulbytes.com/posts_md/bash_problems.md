---
title: BASH: What Needs to Go, What Needs to Stay
date: 2016 09 04
tag: research
---

# BASH: What Needs to Go, What Needs to Stay

## What Is the Problem?
First, let's go through some typical sources of frustration with Bash.

### Whitespace
Bash programmers know that spacing *matters*:  
Variable assignments:  

```bash  	
a = `pwd`  # incorrect assignment
a=`pwd`    # correct assignment
```

If statements:  

```bash  	
    if [-n $some_string]  # incorrect- spaces must follow and preceed square brackets
    then
    	echo $some_string "is not null"
    fi  


	if [ -n $some_string ]  # this one is correct
    then
    	echo $some_string "is not null"
    fi
```

The reason for this is that Bash divides each line into words, delimited by
each whitespace. The first word is seen as the name of the command to be 
executed, while the following words are the arguments to that command.  
  
So, in the variable assignment above, Bash thinks that `a` is a command, 
which does not exist.  
  
Same goes for the if statements: `[` is a command and, in this case, 
`-n` is an argument. Without the whitespace, Bash will think that 
`[-n` is a command, and will return an error since it is not valid.  
  
One slight note about `[`: historically, it was not a shell builtin. Rather,
it was [a separate executable that received the expresson as arguments and 
returned a result. If you didn't surround the `[` with space, the 
shell would be searching $PATH for a different filename (and not find it).](http://stackoverflow.com/questions/9581064/why-should-there-be-a-space-after-and-before-in-a-bash-script)

### Wordsplitting
Another common source of error and frustration: wordsplitting. Bash 
uses parameter expansion, replacing variables with their values, to be able to
access the data stored in variables. Without double-quoting, wordsplitting 
occurs in the expansion (new words will be created at every whitespace).

Take the following example:  

```bash  	
	var="-n -e -v"
	echo $var
```
Output:  
`-v`

All thanks to wordsplitting.  

Add double-quoting:  

```bash  	
	var="-n -e -v"
	echo "$var"  
```
Output:  
`-n -e -v`

In a larger example, take this file, named `args`:  

```bash  	
	#!/bin/bash
	printf "%d args:" $#
	printf " <%s>" "$@"
	echo
```

Consider these commands:

```bash  	
	var="This is a variable"; args "$var"  
```
Output:  
`1 args: <This is a variable>`

```bash  	
	var="This is a variable"; args $var  
```
Output:  
`4 args: <This> <is> <a> <variable>`

### Test
A discrepancy in Bash that also leads to ambiguity (\*frustration) 
is new test (`[[`) vs 
old test (`[`). Both actions essentially do the same thing, 
except for this major difference: wordsplitting and 
glob expansion doesn't happen in new test, because it is a keyword
and not a builtin, like old test. Since new test is a keyword, 
it parses its own arguments and does the expansion itself, 
taking the result as a single argument even if the result contains whitespaces.

### Child Subshells
Have you ever tried to edit a global variable inside of a function?
Or inside of any other action that results in the creation of a 
subshell? Did it work out?  
It didn't work out because
[subshells inherit variables from their parent shells, but a subshell cannot modify the environment of its parent shell](http://stackoverflow.com/a/23565252/6491319) 
You can only return a 
numeric value from functions, between 0-255. If you want to return
anything else, you would have to echo the information and capture 
it with command substitution, or write to a temporary file and source
the variables. Both seem like subpar solutions.

### Command Substitution
Having two ways to execute commands, 

	`` 
and 

	`$()`
is not clear and adds ambiguity to programs. These two commands are 
the same:  
from `man bash`:  
		  
	Bash performs the expansion by executing command and replacing the com-
	mand  substitution  with  the  standard output of the command, with any
	trailing newlines deleted.  Embedded newlines are not deleted, but they
	may  be  removed during word splitting.  The command substitution $(cat
	file) can be replaced by the equivalent but faster $(< file).

	When the old-style backquote form of substitution  is  used,  backslash
	retains  its  literal  meaning except when followed by $, `, or \.  The
	first backquote not preceded by a backslash terminates the command sub-
	stitution.   When using the $(command) form, all characters between the
	parentheses make up the command; none are treated specially.
 

##What Is the Solution?
In a new language, I'd like to see the following:  
- More whitespace, for the sake of clarity. But also, I don't think
lack of whitespace should result in as much errors as Bash has now.  
- Different parameter expansion. There needs to be some means of 
replacing variable names with their values, but it is too error-prone 
the way it is now.  
- Clear and unique keywords and operations to eliminate ambiguity.  

##Notes
####1. 
Should the only type be strings (disregarding `declare`)? Is this a problem?  
####2. 
Each line represents a command and its arguments? Is this a problem?  
####3.
Is it a problem that Bash doesn't display errors for undeclared variables? 
####4. 
Function returns- only numeric. Issue?   
####5.
Inconsistency in control flow structures. `if` ends with `fi`, `case` ends
with `esac`, but `for` and `while` end with `done`.
####6. 
Bash is not self-contained and does not have a standard 
library. Scripts depend on the environment you are working in, 
which typically makes scripts have a bunch of moving parts. Also,
a Bash script generally uses a lot of other small languages, like
Awk, Sed, and Expect. This is kind of just part of the shell game, 
but better integration is desired. 
####7.
Is the lack of simple arithmetic operations a problem?
####8.
Portability vs features?


---
title: Why BASH Sucks 
date: 2016 8 28
tag: research
---

# Why BASH Sucks

Bash is by far the most common shell used by the industry 
today. Even though it is so common, it is not as predictable 
or readable as one would imagine. Below are some reasons why 
Bash isn't as good as it should be, given how much it is 
used and how much it permeates the computing world today.


## Examples
###1.
Bash starts a subshell for any code on the right hand side of
a pipeline. This can be useful, but can also lead to unreadable
and unpredictable code, not easily debuggable. 

```bash
 echo -e "1\n2\n3" | while read i; do   
    echo $i  
    exit 1  
done  
echo END  
```

Output:  
`1`  
`END`   
  
You can get this to work (i.e. be more predictable) with 
process substitution, but that isn't POSIX compliant.  

```bash	
while read i; do
	echo $i
	exit 1
done < <(echo -e "1\n2\n3")
echo END
```

Output:  
`1`  

This is definitely not as readable. Piping is very common 
and useful for manipulating the shell, so Bash should 
somewhat cater to this need.  

###2.
Why does spacing matter so much? Most seasoned Bash programmers 
know that spacing matters a lot, so they don't run into too 
many issues, but wouldn't it be nice if spacing mattered less?  
  
Also, am I the only one curious to see what the parser looks like
for this? Interesting thought, right?  
  



Variable assignments:  

```bash	
a = `pwd`  # incorrect assignment
a=`pwd`    # correct assignment
```
If statements:  

```bash	
  if [-n $some_string]  # incorrect- spaces must follow & preceed square brackets
  then
    echo $some_string "is not null"
  fi  


  if [ -n $some_string ]  # this one is correct
  then
    echo $some_string "is not null"
  fi
```
Whitespace, when used intelligently, makes code more readable. 
It might be a more pleasing stylistic choice to some coders to 
eliminate the spaces in the previous incorrect snippets, but 
why should the programmer be forced to abide by these rules?

###3.
This nonsense:  

```bash	
var="-n -e -v"
echo $var
```

Output:  
`-v`

All thanks to word-splitting.  

This can be fixed with double-quoting:  

```bash	
var="-n -e -v"
echo "$var"  
```
Output:  
`-n -e -v`

Given this file, named `args`:  

```bash	
#!/bin/bash
printf "%d args:" $#
printf " <%s>" "$@"
echo
```

Consider these commands:

	var="This is a variable"; args "$var"  

Output:  
`1 args: <This is a variable>`

	var="This is a variable"; args $var  
Output:  
`4 args: <This> <is> <a> <variable>`

Word splitting is not completely invalid. There are
many scenarios in which this is useful. However, 
there should be a more clear way to specify 
expansion and word splitting to improve code
readablity and the shell coding experience. 

###4.
The craziest [script](https://gist.github.com/jehiah/2771678) that has ever been:  

```bash	
COUNT=1
FILE=$0

# run this script with bash
# i bet you can't predict the outcome

function printsleep {
    echo COUNT=$(( COUNT++ ))
    echo printsleep >> $FILE
    sleep 2
}

printsleep  
```

Code from [Jehiah Czebotar](https://gist.github.com/jehiah).

There are so many things going on here, and to be honest I'm 
not sure why this works. However, I don't think this is due to
snarky or sneaky code, but rather the  mind-bending, 
inherently unreadable and complex inner-workings of Bash.

###5.
Actually doing math in Bash is not great. It's far from great
actually. The syntax is unintuitive and simple arithmetic is
not uncommon in coding in scripts or from the command line.

	expr 1 + 1
Output:  
`2`

	myvar=$(expr 1 + 1)
	echo $myvar
Output:  
`2`

Sure, this is a bit annoying, but at least you *can* do 
integer arithmetic from the command line. If you want to 
do floating point arithmetic, you have to use a command 
line tool, like [bc](https://www.gnu.org/software/bc/).


###6.
New test (`[[`) vs old test (`[`) in Bash is very unclear. 
First, new test is not in the POSIX standard. That may 
matter in some instances, but is not the most important thing
to note. No word splitting or glob expansion happens inside 
of new test, which somewhat addresses the previously noted concern
on avoiding word splitting, but the language is clunky and 
somewhat unintutive here.  
Additionally, along these lines, comparisons are also not clear.
There are different comparisons for strings, numbers, and booleans.
To make this ubiquitous is to make life easier.  

###7.
Having two ways to execute commands, 

	`` 
and 

	`$()`
is not
clear and makes programs inconsistent across the board. It is
better practice to have consistent code and to be able to read
others' code, which isn't as easy as it could be with these 
two options. A replacement for Bash would have a standard 
and would enforce code consistency.   




##Other Notes
After talking to a few peers, there have been a few 
notes that everyone seems to have.  

###1. 
Bash sourcing is rather complicated. A fallback source file can be in 
multiple places, which is inconsistent and could be fixed to 
be more manageable.  

###2.  
Bash is not self-contained and does not have a standard 
library. Scripts depend on the environment you are working in, 
which typically makes scripts have a bunch of moving parts. Also,
a Bash script generally uses a lot of other small languages, like
Awk, Sed, and Expect. This is kind of just part of the shell game, 
but better integration is desired. 
  
###3.
Bash history search is a bit unintuitive. When you search 
for a previous command and do not find what you want, the next 
time you do a reverse search it doesn't reset back to your current
point in time but rather searches backwards from wherever were
you just were.  

###4.
Bash is not scalable and there really are only 
a few ways for multiprocessing. A new language could 
cater to this need. 

###5.
There really are no builtin data structures in Bash, 
besides arrays. This is a tad frustrating and many 
commented that a better shell language would have more
builtins.





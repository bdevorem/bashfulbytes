---
title: New Scripting Language: The Looks 
date: 2016 9 11
tag: research
summary: What a new shell scripting language that's better than BASH would look like
---

#New Shell Scripting Language: The Looks
So we have established that BASH 
[sucks](http://bashfulbytes.com/posts/bash_sux.html), 
[certain things need to go](http://bashfulbytes.com/posts/bash_problems.html), 
and we need to replace it with a new and improved shell language. But what should
this new language look like?


__Variables:__  
	
	string $url = "http://blahblah.com" // strict typing; `$` denotes variable
	int $day = 35 // newline delimits commands
	bool $is_True = True // `True` and `False` are keywords
	float $salary = 5600.00
	string $find = { find, $dir, -type f } 
		// can set return values of commands to variables

__Running Commands:__  
  
	[ firefox, $url ] // plain words are assumed to be commands, `$` denotes variable
	[ wget, $url ]
	[ pkill, -9, $pid ] // options are given after command name, preceded by `-`  

Nested commands:  

	[ [ find, $dir, -type f, -printf "%p %s\n", 2>/dev/null ],
	  |, 
	  [ sed, 's/.*\/[^.]*\.//' ] ] 

Equivalent expression in BASH:   

	find $DIR -type f -printf "%p %s\n" 2>/dev/null | sed 's/.*\/[^.]*\.//'

__Functions:__  
	
	string summary() [ // functions have strict return types
		return [ [ df, -Th, $dir,
				 |,
				 [ tail, -1 ],
				 [ awk, '{print $1, $2, $5, $6;}' ],
				 |,
				 [ column, -t]
			   ]
	]

Semi-equivalent function in BASH (no return value):  
	
	summary(){
		df -Th $DIR | tail -1 | awk '{print $1, $2, $5, $6;}' | column -t
	}

__Conditionals:__  
	
	if ( $var is True ) // condition in parentheses for easy parsing
	[ // commands inside of square brackets for consistency and more easy parsing
		int $month = 9
		int $day = 11
		float $money = 32.32
		[ [ ps, -aux ], |, [grep, $money] ] // nested brackets for each command 
	] 
	  
	switch ($key) [
		case ('-h' | '--help') [
			$HELP = True
		]
		case ( '-f', '--file') [
			$FILE = True
		]
		default [
			$HELP = True
		]
	]
		

Equivalent case structure in BASH:  
	
	key="$1"
	case $key in
		-h|--help)
		    HELP=true
			;;
		-f|--file)
			FILE="$2"
			shift
			;;
		*)
			HELP=true
			;;
	esac

__Loops:__  
	
	for ( $i = 0, $i < 10, $i++) [
		[ echo, $i ]
	]



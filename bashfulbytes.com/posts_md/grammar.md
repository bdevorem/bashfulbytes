---
title: New Shell Language: Proposed Grammar 
date: 2016 9 19 
tag: research 
---

# New Shell Language: Proposed Grammar (Updated)
####Not an LL grammar... yet

## Basics

```  
P : L  
L : statement  
  | statement L
statement : L;   
		  | V;   
		  | E;  
		  | F; 
```

## Variables

	V : type $id
	  | type $id = expr
	  | $id = expr
	type : string  
		 | int  
		 | bool  
		 | float  
		 | array

## Expressions
	
	expr : "str"
		 | $id
		 | *expr
		 | num
		 | E
		 | F
		 | { elements }
		 | expr + expr
		 | expr * expr
		 | expr / expr
		 | expr % expr
		 | expr - expr
		 | expr ^ expr
		 | expr++
		 | expr--

	comp : expr != expr
		 | expr == expr
		 | expr >= expr
		 | expr <= expr
		 | expr < expr
		 | expr > expr
		 | expr && expr
		 | expr || expr

## Executions
	
	E : pipeline 
	pipeline : pipeline redirect commad 
			 | command 
	command : [ cmd ] 
	redirect : <<
			 | <
			 | >>
			 | <>
			 | >
			 | |
			 | >&
			 | >|
			 | <&
			 | ;
			 | &

## Functions
	
	F : type $id( parameters ) body END
	  | $id( parameters )
	parameters : param
	param : type $id, param 
		  | epsilon
	body : L body
	  | return expr body
	  | epsilon

## Conditionals

	F : cond 
	  | loop
	cond : IF 
	     | SWITCH
	IF : if ( comparison ) body cont END
	cont : ELSE 
	    | ELIF
		| epsilon
	comparison : comp
			   | expr
	ELSE : else body
	ELIF : else if ( comparison ) body cont
	SWITCH : switch ( comparison ) CASE DEFAULT END
	CASE : case ( expression ) body CASE 
	     | epsilon
	DEFAULT : default body

## Loops

	loop : WHILE 
		 | FOR
	FOR : for ( loop_conditional ) body END
	WHILE : while ( loop_conditional ) body END



## Notes
- Need to define basic unix/linux tokens? Some defined here, only PIPE, BG, RW in scanner.
Need `2>`, for example?
- Need to define language functions, like `atoi`?
- Changed the `{}` block construct to having `END` statements to be more intuitive

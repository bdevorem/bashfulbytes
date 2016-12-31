---
title: Strict Shell Update 
date: 2016 12 16
tag: research
summary: New shell scripting language, strict shell
---

# Strict Shell - Current Overview
So the semester had ended, and many changes have been made to Strict Shell. In 
fact, now it even has a name! (Though the name may change, because how do 
you even say `stsh`?)  
Well, here you will find all the new information on Strict Shell.  
  

## Grammar
	
	program : stmt_list
			;
	
	decl_list : real_decl_list
			  | /* nothing */
			  ;
	
	real_decl_list : decl COMMA decl_list
				   | decl
				   ;
	
	decl : type id
		 | type id ASSIGN expr
		 | type id L_PAREN decl_list R_PAREN stmt_list END
		 | ARRAY id ASSIGN L_BRACKET expr_list R_BRACKET
		 ;
	
	id : IDENTIFIER
	   ;
		 
	stmt_list : stmt stmt_list
			  |
			  ;
	
	stmt : decl SEMICOLON
		 | FOR L_PAREN expr_or_nothing SEMICOLON expr_or_nothing SEMICOLON expr_or_nothing R_PAREN stmt_list END SEMICOLON
		 | RETURN expr SEMICOLON
		 | IF L_PAREN expr R_PAREN stmt_list END SEMICOLON
		 | IF L_PAREN expr R_PAREN stmt_list ELSE stmt_list END SEMICOLON
		 | expr SEMICOLON
		 | PRINT expr_list SEMICOLON
		 | WHILE L_PAREN expr R_PAREN stmt_list END SEMICOLON
		 | BREAK SEMICOLON
		 ;
	
	expr_list : real_expr_list
			  | /*nothing */
			  ;
	
	real_expr_list : expr COMMA real_expr_list
				   | expr
	
	expr_or_nothing : expr
			        | /* nothing */
			        ;
	
	expr : or_expr ASSIGN expr
		 | or_expr
		 ;
	
	or_expr : or_expr OR and_expr
		    | and_expr
		    ;
	
	and_expr : and_expr AND expr_compare
		     | expr_compare
		     ;
	
	expr_compare : expr_compare GT add_expr
		         | expr_compare GE add_expr
		         | expr_compare LT add_expr
		         | expr_compare LE add_expr
		         | expr_compare EQ add_expr
		         | expr_compare NE add_expr
		         | add_expr
		         ;
	
	add_expr : add_expr ADD mul_expr
			 | add_expr MINUS mul_expr
			 | mul_expr
		     ;
	
	mul_expr : mul_expr MULTIPLY exp_expr
			  | mul_expr MOD exp_expr
			  | mul_expr DIVIDE exp_expr
			  | exp_expr
		      ;
	
	exp_expr : exp_expr EXPON un_expr
			 | un_expr
		     ;
	
	un_expr : MINUS un_expr
			| NOT un_expr
			| incr_expr
			;
	
	incr_expr : expr_group INCREMENT
			  | expr_group DECREMENT
			  | expr_group
		      ;
	
	expr_group : L_PAREN expr R_PAREN
			   | id L_PAREN expr_list R_PAREN
			   | command
			   ;

	command :  L_BRACE expr_list R_BRACE
		       | atomic
				;
	
	atomic : TRUE
		   | FALSE 
		   | id 
		   | STRING_LITERAL
		   | CHAR_LITERAL
		   | INTEGER_LITERAL 
		   | FLOAT_LITERAL 
		   | COMMAND
		   ;
	
	type : STRING 
	     | BOOLEAN 
		 | INTEGER 
		 | VOID
		 | FLOAT 
		 ;
	

## Examples
  
__Variables:__  
	
	string $url = "http://blahblah.com"
	int $day = 35; 
	bool $is_True = True;
	float $salary = 5600.00;
	string $find = { find, $dir, "-type f" };

__Running Commands:__  
  
	{ firefox, $url };
	{ wget, $url };
	{ pkill, "-9", $pid }; 
	{ find, $dir, "-type f", "-printf \"%p %s\n\"", "2>/dev/null" };

__Functions:__  
	
	string $summary()
		return { df, "-Th", $dir};
	END;

__Conditionals:__  
	
	if ( $var == True )
		int $month = 9;
		int $day = 11;
		float $money = 32.32;
	END; 
	  
__Loops:__  
	
	for ( $i = 0; $i < 10; $i++)
		{echo, $i};
	END;

## Types
  
Strict Shell has strong typing and enforces type safety, so operations are
only allowd on matching types. This may change, since I have found it handy
to add characters with integers in some sneaky computations, but we will see.

## Evaluation
  
Evaluation is the next step in this process. I started evaluating expressions, 
but quickly fell into the strong typing trap. I also started statement 
evaluation, but not much can be finished until we take a step back from the
language and come back with fresh eyes. 
  
### More updates to come in the Spring of 2017.

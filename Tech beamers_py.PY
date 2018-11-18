 					TOPIC

KEYWORD
	#Keywords are special words which are reserved and have a specific meaning. Python has a set of keywords that cannot be used as variables in programs.
	>>> import keyword
	>>> keyword.kwlist
	>>> keyword.iskeyword('try') function is used to whether the keyword is valid or not.

IDENTIFIER (user defined names)
	
	#Python Identifiers are user-defined names to represent a variable, function, class, module or any other object. If you assign some name to a programmable entity in Python, then it is nothing but technically called an identifier.
	
	- 'techbeamers'.isidentifier() function is used to whether the identifier is valid or not.
	
VARIABLE
	>>> test = 10 / the variable 'test' is reference to the value '10'.

	>>> test = 10
	>>> id(test)
		1716585200

PYTHON STATEMENT
	- STATEMENT 
		 # logical instruction which Python interpreter can read and execute

	- Expression
		# type Python statement which contains a logical sequence of numbers, strings, objects, and operators.

		EX :

		# Using Arithmetic expressions
		>>> ((10 + 2) * 100 / 5 - 200)
			40.0
		#############
		# Using functions in an expression
		>>> pow(2, 10)
		1024
		#############
		# Using eval in an expression
		>>> eval( "2.5+2.5" )
		5.0

	- simple assignment STATEMENT
	 	# we create new variables, assign and change values.
	 	- variable = expression

	 	- value based assignment:
	 		>>> test = "Learn Python" # Creating the name value will led to create a new object and assign to different location.
			>>> id(test1)
			6589104
			>>> test2 = "Learn Python"
			>>> id(test2)
			6589488

	- augmented assignment STATEMENT:
		# You can combine arithmetic operators in assignments to form an augmented assignment statement.
		 EX :
		 	 >>> x += y --> is shothand of x = x + y

		 	 >>> list_vowels = ['a','e','i']
			 >>> list_vowels += ['o', 'u',]
			 >>> print(list_vowels)
			 ['a', 'e', 'i', 'o', 'u']


	MULTI-LINE STATEMENT
		# we can extend it over to multiple lines using the line continuation character (\).
		
		- Explicit line continuation
			>>> my_list = [1, \
				... 2, 3\
				... ,4,5 \
				... ]

			>>> eval ( \
				... " 2.5 \
				... + \
				... 3.5")
				6.0

		- Implicit line continuation :
			# mplicit line continuation is when you split a statement using either of parentheses ( ), brackets [ ] and braces { }.
			>>> result = (10 + 100
				... * 5 - 5
				... / 100 + 10
				... )

			>>> subjects = [
				... 'Maths',
				... 'English',
				... 'Science'
				... ]
	INDENTATION

		-ideal identation size
		-why is identation important

		EX:
			>>> def demo_routine(num):
					 print('I am a demo function')
					 if num % 2 == 0:
					 	return True
					 else:
					 	return False

					num = int(input('Enter a number:'))
					if demo_routine(num) is True:
					 	print(num, 'is an even number')
					else:
				 		print(num, 'is an odd number')

COMMENTS
	-Single line COMMENTS
		# Good code is self-documenting.

	-MULTI-LINE COMMENTS:
		# To Learn any language you must follow the below rules.
		# 1. Know the basic syntax, data types, control structures and conditional

	- Docstring:
		# Python has the documentation strings (or docstrings) feature. It gives programmers an easy way of adding quick notes with every Python module, function, class, and method.

		myobj.__doc__
		EX:
			>>> def theFunction():
			    '''
			This function demonstrate the use of docstring in Python.
			    '''
			    print("Python docstrings are not comments.")

				print("\nJust printing the docstring value...")
				print(theFunction.__doc__)

DATA TYPES
	- Booleans (True == 1 or False == 0 : These values are constants and can be used to assign or compare boolean values.)
		EX:
			>>> condition = False <--- This works without the explicit comparison.
			>>> if condition == True:
			    print("You can continue with the prpgram.")
			else:
			    print("The program will end here.")
		##############
			>>> str = "Learn Python"
			>>> len(str)
			12

			>>> len(str) == 12
			True

			>>> len(str) != 12
			False

	- Numbers (type(), isinstance(num, complex))

		# Numbers are classified using int,float,complex.
		# type(1) function is to determine the datatype of the variable or value.
		# isinstance(3+5j,  complex) function is there for testing the type of an object.
		# Adding j or J will make the number imaginary.

		EX:
			>>> num = 2
			>>> print("The number (", num, ") is of type", type(num))
			The number ( 2 ) is of type <class 'int'>

			>>> num = 3.0
			>>> print("The number (", num, ") is of type", type(num))
			The number ( 3.0 ) is of type <class 'float'>

			>>> num = 3+5j
			>>> print("The number ", num, " is of type", type(num))
			>>> print("The number ", num, " is complex number?", isinstance(3+5j, complex))
			The number (3+5j) is of type <class 'complex'>
			The number (3+5j) is complex number? True

		- Constructors :
			>>> int(2)
			2
			>>> float(2)
			2.0
			>>> complex(2, 2)
			(2+2j)

		NOTE : var_name.bit_length() <--- To find bit length.


	- Strings : (Immutable - unable to change.)
		EX:

			- Single line:

				>>> str = 'A string wrapped in single quotes'

			- Multi Line:

				>>> str = """A multiline string
							starts and ends with
							a triple quotation mark."""

			- Replacing string :

				>>> substr_var = String_var.replace("document", "tutorial")
				print (substr_var)

			- Accessing the characters in Python :

				- Slicing :

				>>> sample_str = 'Python String'
				>>> print (sample_str[0])
					P

				>>> str = "Learn Python"
				>>> first_5_chars = str[0:5]
				>>> print(first_5_chars)
				Learn

				>>> substr_from_2_to_5 = str[1:5]
				>>> print(substr_from_2_to_5)
				earn

				>>> substr_from_6_to_end = str[6:]
				>>> print(substr_from_6_to_end)
				Python

				>>> last_2_chars = str[-2:]
				>>> print(last_2_chars)
				on

				>>> first_2_chars = str[:2]
				>>> print(first_2_chars)
				Le
				
				>>> two_chars_before_last = str[-3:-1]
				>>> print(two_chars_before_last)
				ho

			- Immutable :
				>>> A = 'Python3'
				>>> id(A)
				56272968
				>>> B = A
				>>> id(B)
				56272968

			- Python String Operators :
			
				
				+		Concatenation						Combining two Strings into one.							var1 = ‘Python’
																												var2 = ‘String’
																												print (var1+var2)
																												# PythonString

				*		Repetition							Creates new String by repeating 						var1 = ‘Python’
														the String given number of times.						print (var1*3)
																								
																												# PythonPythonPython

				[ ]		Slicing								Prints the character at given index.					var1 = ‘Python’
																												print (var1[2])
																												# t

				[ : ]	Range Slicing						Prints the characters present at the given range.	var1 = ‘Python’
																												print (var1[2:5])
																												# tho

				in											Membership	Returns ‘True’ value if character 		var1 = ‘Python’
															is present in the given String.						print (‘n’ in var1)
																												# True
																												
				not in										Membership	Returns ‘True’ value if character 		var1 = ‘Python’
															is not present in given String.						print (‘N’ not in var1)
																												# True
																											
				for	Iterating								Using for we can iterate through all				var1 = 'Python'
															the characters of the String.						for var in var1:
																												print (var)					    
																												# P
																												# y
																												# t
																												# h
																												# o
																												# n

					r/R	Raw String							Used to ignore the actual meaning of 				print (r’\n’)
															Escape characters inside a string.					# \n
															For this we add ‘r’ or ‘R’ in front 				print (R’\n’)
															of the String. 										# \n
					
					
					
	- Bytes (Immutable or Unchanged) :
		# Byte objects contain a sequence of bytes whereas the strings store sequence of characters.
		# The bytes are machine-readable objects whereas the strings are just in human-readable form.

		>>> # Make an empty bytes object (8-bit bytes)
		>>> empty_object = bytes(16)
		>>> print(type(empty_object))
		<class 'bytes'>
		>>> print(empty_object)
		b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

	- List [mutable] :
		# Python list is an array like construct which stores arbitrarily typed objects in an ordered sequence.
		# Index in a list begins with zero in Python.

		>>> list = [True, False, 1, 1.1, 1+2j, 'Learn', b'Python']
		>>> list[0]
		True

		# List object are mutable.
		>>> list = [True, False, 1, 1.1, 1+2j, 'Learn', b'Python']
		>>> id(list)
		1605296162952
		>>>list[2] = 2
		>>> id(list)
		1605296162952

		#########
		
		- Nesting inside a List :
			
			>>> nested = [[1,1,1], [2,2,2], [3,3,3]]
			>>> for items in nested:
				for item in items:
					print(item, end=', ')
					
			1 1 1 2 2 2 3 3 3

		##########
		
		- Slicing a list :

			>>> languages = ['C', 'C++', 'Python', 'Java', 'Go', 'Angular']
			>>> print('languages[0:3] = ', languages[0:3])
			languages[0:3] =  ['C', 'C++', 'Python']
			>>> print('languages[2:] = ', languages[2:])
			languages[2:] =  ['Python', 'Java', 'Go', 'Angular']

		###########

		- Tuples - (Tuples, Nested_tuples, repetition in tuples, Slicing) :
			# objects of different data types can co-exist in a tuple.
				# nested tuples
				>>> first_tuple = (3, 5, 7, 9)
				>>> second_tuple = ('learn', 'python 3')
				>>> nested_tuple = (first_tuple, second_tuple)
				>>> print(nested_tuple)
				((3, 5, 7, 9), ('learn', 'python 3'))

				###########

				# repetition in tuples

				>>> sample_tuple = ('Python 3',)*3 # The string multiplies into 3 times.
				>>> print(sample_tuple)
				('python', 'python', 'python')

				###########

				# Slicing in Tuples :

				sample_tuple = (0 ,1, 2, 3, 4)

				>>> tuple_without_first_item = sample_tuple[1:]
				>>> print(tuple_without_first_item)
				(1, 2, 3, 4)

				>>> tuple_reverse = sample_tuple[::-1]
				>>> print(tuple_reverse)
				(4, 3, 2, 1, 0)

				>>> tuple_from_3_to_5 = sample_tuple[2:4]
				>>> print(tuple_from_3_to_5)
				(2, 3)

				############

		- Sets :
			# set is one which supports mathematical operations like union, intersection, symmetric difference etc.
			# set is an unordered collection of unique and immutable objects.
			# It implements a highly optimized method that checks whether the container hosts a specific element or not.

			>>> sample_set = set("Python data types")
			>>> type(sample_set)
			<class 'set'>
			>>> sample_set
			{'e', 'y', 't', 'o', ' ', 'd', 's', 'P', 'p', 'n', 'h', 'a'}

			##############

			>>> another_set = {'red', 'green', 'black'}
			>>> type(another_set)
			<class 'set'>
			>>> another_set
			{'red', 'green', 'black'}

			- FROZEN SET :
				#  It is immutable and only supports methods and operators that executes without altering the frozen set used in the context.

				EX:
				# An empty frozenset
				>>> frozenset()
				frozenset()
				>>> type(cities)
				# <class 'frozenset'>
				
				# Standard set :
				>>> sample_set = {'jai', 'sonu'}

				# Add an element to the standard set
				>>> sample_set.add("black")

				>>> print("Standard Set")
				>>> print(sample_set)

				# A frozen set
				>>> frozen_set = frozenset(["red", "green", "black"])

				>>> print("Frozen Set")
				>>> print(frozen_set)
				

		- Dictionaries - (creating, Modifying-Add/update/delete) :

			# A dictionary in Python is an unordered collection of key-value pairs. It’s a built-in mapping type in Python where keys map to values.
			# These key-value pairs provide an intuitive way to store data.

			EX :
				>>> sample_dict = {'name' : 'jai', 'age': 24, 'place' : 'chennai'}
				>>> sample_dict
				{'name': 'jai', 'age': 24, 'place': 'chennai'}	

			# Accessing the Dict Elements :

				>>> sample_dict['name']
				jai

			# Methods to access dict elements :

				keys() – It isolates the keys from a dictionary.
				values() – It isolates the values from a dictionary.
				items() – It returns the items in a list style of (key, value) pairs.

				EX :
				>>> sample_dict.keys()
				dict_keys(['name', 'age', 'place'])
				>>> sample_dict.values()
				dict_values(['jai', 24, 'chennai'])
				>>> sample_dict.items()
				dict_items([('name', 'jai'), ('age', 24), ('place', 'chennai')])

			# Modifying  a Dict ( update ) :
				# Since the dictionary object is mutable, so we can call add, update and delete operations on a dictionary object.
				EX:
					>>> sample_dict.update({'name' : 'jai', 'age' : 23 })
					>>> sample_dict
					{'name': 'jai', 'age': 23, 'place': 'chennai'}


NUMBERS
	- Intiger, Float, Complex
	- Binary, Octal, Hex
	- to chck class type of  no. use '.isinstance(object, class)
	- divmod(7, 2)--function for division.
	- Type conversion(Casting)- coericon uses int(), float(),complex()
	- Python Decimal module
	- Python Fractions module
	- Python mathematics - [abs(), cmp(), max(), min(), round()]

PYTHON LIST :
	- list(tuple) - to create a list.
		EX:
			 L2 = [expression, ...]
			 L3 = [1, "Hello", 3.4]

		>>> theList = list() #empty list
		>>> len(theList) # length of the list.
			0

		theList = list([n1, n2, ...] or [n1, n2, [x1, x2, ...]])
					#STANDARD				# NESTED SEQUENCE

	- list comprehension theList = [expression(iter) for iter in oldList if filter(iter)]
		EX:
			>>> theList = [iter for iter in range(5)]
			>>> theList
				[0, 1, 2, 3, 4]

			>>> listofCountries = ["India","America","England","Germany","Brazil","Vietnam"]
			>>> firstLetters = [ country[0] for country in listofCountries ]
			>>> print(firstLetters)
				['I', 'A', 'E', 'G', 'B', 'V']
			########
			>>> print ([x+y for x in 'get' for y in 'set'])
				['gs', 'ge', 'gt', 'es', 'ee', 'et', 'ts', 'te', 'tt']
			########
			>>> months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
			>>> oddMonths = [iter for index, iter in enumerate(months) if (index%2 == 0)]
			>>> oddMonths
				['jan', 'mar', 'may', 'jul', 'sep', 'nov']
			#########
	- Creating a Multi_dimensinol List - NESTED LIST
		EX:
			>>> init_list = [0]*3
			>>> print(init_list)
				[0, 0, 0]
			##########
			>>>two_dim_list = [ [0]*3 ] *3 --> # two dimensional list
			##########
			>>> two_dim_list = [ [0]*3 ] *3
			>>> print(two_dim_list)
			[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
			>>> two_dim_list[0][2] = 1
			>>> print(two_dim_list)
			[[0, 0, 1], [0, 0, 1], [0, 0, 1]]
			##########  use list comprehensions
			>>> two_dim_list = [[0]*3 for i in range(3)]
			>>> print(two_dim_list)
				[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
			>>> two_dim_list[0][2] = 1
			>>> print(two_dim_list)
				[[0, 0, 1], [0, 0, 0], [0, 0, 0]]
			##########

	- List Extension
		EX:
			>>> L1 = ['a', 'b']
			>>> L2 = [1, 2]
			>>> L1 + L2 + L3
				['a', 'b', 1, 2, 'Learn', 'Python']
			########## extend() METHOD
			>>> L1 = ['a', 'b'] 
			>>> L2 = ['c', 'd']
			>>> L1.extend(L2)
			>>> print(L1)
			['a', 'b', 'c', 'd']
			########### append() method
			>>> L1 = ['x', 'y']
			>>> L1.append(['a', 'b'])
			>>> L1
			['x', 'y', ['a', 'b']]
			###########
			>>>vowels = ['a','e','i','o','u']
			>>>consonants = ['b', 'c', 'd', 'f']
			>>>print(vowels[0])
				a
			>>>print(vowels[2])
				d
			try:
			 vowels[1.0]
			except Exception as ex:
			 print("Note:", ex)

			 >>>alphabets = [vowels, consonants]
			 print(alphabets[0][2])
			 	i 
			 print(alphabets[1][2])
			 	d

	- Reverse indexing
			>>>vowels = ['a','e','i','o','u']
			>>> print(vowels[-1])
				u

	-  Slicing
			[start(optional):stop(optional):step(optional)] # SYNTAK=X

			>>> theList = [1, 2, 3, 4, 5, 6, 7, 8]
			>>> theList[2:5]
				[3, 4, 5]
			>>> theList[2:5:2]
				[3, 5]
			>>> theList[2:-1]
				[3, 4, 5, 6, 7]
			>>> theList[::-1]	# REVERSING THE LIST
				[8, 7, 6, 5, 4, 3, 2, 1] 
			>>> theList[::-2] # SKIPPING SECOND MEMBER
				[8, 6, 4, 2]

	- SHALLOW COPY OF FULL PYTHON LIST 
			>>> id(theList)
				55530056
			>>> id(theList[::])
				55463496

	- COPY OF THE LIST CONTAINING EVERY OTHER ELEMENT
			>>> theList[::2]
				[1, 3, 5, 7]

	- ITERATING LIST IN PYTHON
			- enumerate() function :
				>>> for index, element in enumerate(theList):
					print(index, element)

			- built-in iter function :
				>>> theList = ['Python', 'C', 'C++', 'Java', 'CSharp']
				>>> for language in theList:
					print("I like", language)
				OUTPUT :
				I like Python
				I like C
				I like C++
				I like Java
				I like CSharp

	- ADD / UPDATE AN ELEMENT TO A LIST :
			EX :
				>>> theList = ['Python', 'C', 'C++', 'Java', 'CSharp']
				>>> theList[4] = 'Angular'
				>>> print(theList)
					['Python', 'C', 'C++', 'Java', 'Angular']
				############
			- insert() method :
				>>> theList = [55, 66]
				>>> theList.insert(0, 33)
				>>> print(theList)
					[33, 55, 66]
				############
			- slice assignment :
				>>> theList = [55, 66]
				>>> theList[2:2] = [77, 88]
				>>> print(theList)
					[55, 66, 77, 88]

	- REMOVE / DELETE ELEMENTS FROAM A LIST :
			EX :
			- del keyword
				>>> vowels = ['a','e','i','o','u']

				>>> del vowels[2]
				>>> vowels
					['a', 'e', 'o', 'u']

				>>> del vowels[1:3]
				>>> vowels
					['a','u']

				>>> del vowels - deletes the entire vowels

			-.remove() method :
				>>> vowels.remove('a')
				>>> vowels
					['e','i','o','u']

			- .pop() method :

				>>> vowels.pop(1)
					['e', 'o', 'u']

			- .clear() method....clears the list.

			- vowels = [] # BLANK LIST removes the entire list.

	- SEARCHING ELEMENT IN A LIST :
			- 'in' operator :
				>>> if value in theList:
    					print("list contains", value)

    		- .index() method :
    			>>> loc = theList.index(77)
    				2
    			############
    			>>> try:
    					loc = theList.index(value)
					except ValueError:
    					loc = -1 # no match
    			##############
    			>>> loc = -1
				>>> try:
					    while 1:
					        loc = theList.index(value, loc+1)
					        print("match at", loc)
					except ValueError:
					    pass
    			################
    			>>> theList = ['a','e','i','o','u']
				>>> def matchall(theList, value, pos=0):
					    loc = pos - 1
					    try:
					        loc = theList.index(value, loc+1)
					        yield loc
					    except ValueError:
					        pass

					value = 'i'
					for loc in matchall(theList, value):
					    print("match at", loc+1, "position.")

					 match at 3 position.

				###################
			- min() and  max() method :
				>>> theList = [1, 2, 33, 3, 4]
				>>> low = min(theList)
				>>> low
				1
				>>> high = max(theList)
				>>> high
				33

	- SORTING A LIST IN PYTHON :
			- sort() method by default in ascending order :
				>>>theList = ['a','e','i','o','u']
				>>>theList.sort()
				>>>print(theList)
			#################
			- sort() method in reverse order(decending):
				>>>theList = ['a','e','i','o','u']
				>>>theList.sort(reverse=True)
				>>>print(theList)
					['u', 'o', 'i', 'e', 'a']
			#################
			- built-in sorted() method :
				- newList = sorted(theList) # returns the original copy of the list.
				EX :
					theList = ['a','e','i','o','u']
					newList = sorted(theList)
					print("Original list:", theList, "Memory addr:", id(theList))
					print("Copy of the list:", newList, "Memory addr:", id(newList))

	- PYTHON LIST MEHTODS :
		append()	It adds a new element to end of the list.

		extend()	It extends a list by adding elements from another list.
		
		insert()	It injects a new element at the desired index.
		
		remove()	It deletes the desired element from the list.
		
		pop()	It removes as well as returns an item from the given position.
		
		clear()	It flushes out all elements of a list.
		
		index()	It returns the index of an element that matches first.
		
		count()	It returns the total no. of elements passed as an argument.
		
		sort()	It orders the elements of a list in an ascending manner.
		
		reverse()	It inverts the order of the elements in a list.
		
		copy()	It performs a shallow copy of the list and returns.

	- PYTHON LIST BUILT-IN FUNCTIONS :
		all()	It returns True if the list has elements with a True value or is blank.
		
		any()	If any of the members has a True value, then it also returns True.
		
		enumerate()	It returns a tuple with an index and value of all the list elements.
		
		len()	The return value is the size of the list.
		
		list()	It converts all iterable objects and returns as a list.
		
		max()	The member which has the maximum value.
		
		min()	The member which has the minimum value.
		
		sorted()	It returns the sorted copy of the list.
		
		sum()	The return value is the aggregate of all elements of a list.


- SETS IN PYTHON :
	
	# COLLECTION OF ELEMENTS FROM DIFFERENT DATA TYPES WHICH IS STORED RANDOMLY.
	# USED TO PERFORM MATHEMATICAL OPERATIONS SUCH AS UNION, INTERSECTION,
	#	SYMMETRIC, DIFFERENCE, COMPLEMENT.

	- INSTANTIATE A SET IN PYTHON :	
		- create a set of numbers
			>>> py_set_num = {3, 7, 11, 15, 3} # can't store duplicate values.
			>>> print(py_set_num)
				{3, 11, 7, 15}
			##############
			>>> py_set_mix = {11, 1.1, "11", (1, 2)}
			>>> print(py_set_mix)
				{(1, 2), 1.1, 11, '11'}
		
		- SET using set() method :
			>>> py_set_mix = set([11, 1.1, "11", (1, 2)])
			>>> print(py_set_mix)
				{(1, 2), 1.1, 11, '11'}

		NOTE : 
			>>> py_empty = {} # Makes it as a dictionary.
			>>> py_empty = set() # Using  set function will make it as SET.

		- Modifying SET in python using .add(single element) and .update([multiple element]) mehtods :
			>>> py_set_num = {77, 88}
			>>> try:
				    print(py_set_num[0])
				except Exception as ex:
				    print("Error in py_set_num[0]:", ex)

				print("The value of py_set_num:", py_set_num)

				Error in py_set_num[0]: 'set' object does not support indexing
			########## ADDING ELEMENT :
			>>> py_set_num.add(99)
			>>> print("The value of py_set_num:", py_set_num)
				The value of py_set_num: {88, 99, 77}
			########## UPDATING BUNCH OF ELEMENTS :
			>>> py_set_num.update([4.4, 5.5, 6.6], {2.2, 4.4, 6.6})
			>>> print("The value of py_set_num:", py_set_num)
				The value of py_set_num: {66, 99, 4.4, 5.5, 6.6, 2.2, 44, 77, 55, 88}

		- Deleting elements using .discard(), .clear(), pop() and .remove() mentod :
			>>> py_set_num = {22, 33, 55, 77, 99}
			>>> py_set_num.discard(99) # It wont throw any error.
			>>>py_set_num.remove(99) # It throws KeyError.

		- Python SET Native Operations :
			set supports operations like union, intersection, difference,
				and complement so does it in Python.

			- UNION OPERATION : # MINGLES BOTH A AND B.
				>>> setA = {'a', 'e', 'i', 'o', 'u', 'g', 'h'}
				>>> setB = {'a', 'e', 'z', 'b', 't', 'o', 'u'}
				>>> setA | setB # By using pipe symbol.
				>>> setA.union(setB) # By using .union() method.

			- INTERSECTION OPERATION : # Produces only common element.
				>>> setA & setB
					{'o', 'e', 'u', 'a'}
				>>> setA.intersection(setB) # By using .intersection() method.

			- Difference operations on the set : # Shows remaining elemnts.
				>>> setA - setB
					{'i', 'g', 'h'}
				>>> setA.difference(setB)
					{'i', 'g', 'h'}

			- Symmetric difference operation on SET : # Shows elements exists in both A and B but neglects the common elements.

				>>> setA^setB
					{'z', 'i', 't', 'b', 'h', 'g'}
				>>> setA.symmetric_difference(setB)
					{'z', 'i', 't', 'b', 'h', 'g'}


		- Miscellaneous SET operations :
			- Accessing data elements :
				>>> basket = set(["apple", "mango", "banana", "grapes", "orange"])
				>>> for fruit in basket:
						print(fruit)

					apple
					banana
					mango
					orange
					grapes

			- Perform membership test in a SET : # To find particular element present or not using ' in ' keyword.
				>>> basket = set(["apple", "mango", "banana", "grapes", "orange"])
				>>> print("Is 'apple' in the basket?", 'apple' in basket)
					Is 'apple' in the basket? True

			- Frozen SETs in python :
				>>> std_set = set(["apple", "mango","orange"])
				>>> frozen_set = frozenset(["apple", "mango","orange"])
				######### ERROR RAISING :
				>>> try:
					    frozen_set.add("banana")
					except Exception as ex:
					    print("Error:", ex)

- TUPLES IN PYTHON :
	# Tuple in python is a heterogenous collection of elements which is immutable.
	- INSTANTIATE A TUPLE IN PYTHON :
		- Creating tuple :
			>>> groceries = ['apricot', 'appple', 'banana'] # LIST
		 
				>>> security_numbers = ('12323434', '2323123', 'jai') # TUPLES
		
			>>> groceries.append('cheese')
				The 'cheese' will be added in the list.
		
			>>> security_numbes.append('cheese')
				'cheese' cant be added in Tuples.

		- built-in Fuction ' tuple() ' :
			>>> py_tuple = tuple({33, 44, 55})
			>>> py_tuple = tuple([33, 44, 55])

		- Creating Tuple of size one :
			>>> py_tuple = ('single',)

	- Acessing Tuple in python :
			>>> vowel_tuple = ('a','e','i','o','u')

		- Via Indexing :
			>>> 












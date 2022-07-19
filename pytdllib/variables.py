__all__ = ['Stroka', 'Boolean']

class Stroka:
	''' Help on class.

	Name:
		Stroka - Data descriptor.

	Note:
		A data descriptor, which is a string designation 
		with type checking, as well as changing 
		the variable name for private access through 
		getters and setters.

	Files:
		variables.py

	Methods
	----------
		verify_str(cls, value):
			Checking the string data type.
		__set_name__(self, owner, name):
			Setting the variable name with 
			two underscores at the beginning of this line.
		__get__(self, instance, owner):
			Getter of the variable.
		__set__(self, instance, value: str):
			Variable setter.	
	'''

	@classmethod
	def verify_str(cls, value):
		''' Checking the string data type. '''
		if type(value) != str:
			raise TypeError('Enter the line!')

	def __set_name__(self, owner, name):
		''' Setting the variable name with 
		two underscores at the beginning of this line. '''
		self.name = "__" + name

	def __get__(self, instance, owner):
		''' Getter of the variable. '''
		return getattr(instance, self.name)

	def __set__(self, instance, value: str):
		''' Variable setter. '''
		self.verify_str(value)
		setattr(instance, self.name, value)

class Boolean:
	''' Help on class.

	Name:
		Boolean - Data descriptor.

	Note:
		A data descriptor, which is a boolean notation 
		with type checking, as well as changing 
		the variable name for private access 
		via getters and setters.

	Files:
		variables.py

	Methods
	----------
		verify_bool(cls, value):
			Checking the boolean data type.
		__set_name__(self, owner, name):
			Setting the variable name with 
			two underscores at the beginning of this line.
		__get__(self, instance, owner):
			Getter of the variable.
		__set__(self, instance, value: str):
			Variable setter.	
	'''

	@classmethod
	def verify_bool(cls, value):
		''' Checking the boolean data type. '''
		if type(value) != bool:
			raise TypeError('Enter the boolean!')

	def __set_name__(self, owner, name):
		''' Setting the variable name with 
		two underscores at the beginning of this line. '''
		self.name = "__" + name

	def __get__(self, instance, owner):
		''' Getter of the variable. '''
		return getattr(instance, self.name)

	def __set__(self, instance, value: bool):
		''' Variable setter. '''
		self.verify_bool(value)
		setattr(instance, self.name, value)

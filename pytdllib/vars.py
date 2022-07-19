__all__ = ['Stroka', 'Boolean']

class Stroka:

	@classmethod
	def verify_str(cls, value):
		if type(value) != str:
			raise TypeError('Enter the line!')

	def __set_name__(self, owner, name):
		self.name = "__" + name

	def __get__(self, instance, owner):
		return getattr(instance, self.name)

	def __set__(self, instance, value: str):
		self.verify_str(value)
		setattr(instance, self.name, value)

class Boolean:

	@classmethod
	def verify_bool(cls, value):
		if type(value) != bool:
			raise TypeError('Enter the boolean!')

	def __set_name__(self, owner, name):
		self.name = "__" + name

	def __get__(self, instance, owner):
		return getattr(instance, self.name)

	def __set__(self, instance, value: bool):
		self.verify_bool(value)
		setattr(instance, self.name, value)

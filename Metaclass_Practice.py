
def One():
	print("In function one")
def Two():
	print("In function two")
def required():
	try:
		g = int(input())
	except ValueError:
		print("Invalid, enter an integer")
		quit()
	if g == 1:
		return 1
	else:
		return 2
class Extra(object):
	def __init__(self, classname, superclasses, attributedict):
			self.classname = classname
			self.superclasses = superclasses
			self.attributedict = attributedict
			print(classname, superclasses, attributedict)
#			print(dir(self.__class__))
			if required() == 1:
				self.f = One()
				attributedict["g"](self.__class__, name="Charles")
#				attributedict['__init__']()
			else:
				self.f = Two()
				attributedict["g"](self.__class__, name="Tai")
#				attributedict['__init__']()
			attributedict["g"](self.__class__, name="Called from Metaclass")
class Ham(metaclass=Extra):
		def __init__(self):
			pass
		def g(self, name):
			print("In class {} g is called with name {}".format(self.__class__.__qualname__, name))
#			super(Ham, Extra).__init__()
class Eggs(metaclass=Extra):
		def __init__(self):
			pass
		def g(self, name):
			print("In class {} g is called with name {}".format(self.__class__.__qualname__, name))
#			super(Eggs, Extra).__init__()
def Charles():
	I = Ham()
	J = Eggs()
	for n in [I, J]:
		n.f()
Charles()
			
			
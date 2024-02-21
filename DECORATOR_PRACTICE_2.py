def W(F):
	class wrap:
		def __init__(self, *args):
			self.wrapped = F(*args)
		def square(self, n):
			return self.wrapped.f(n)
		def name(self):
			return self.wrapped.name
	return wrap
@W
class T:
	def __init__(self, x, y):
		self.f = x
		self.name = y
		
def Charles():
	CT = T(lambda x: x ** 2, "Charles")
	num = int(input("Enter a number "))
	print("That number squared is: {}".format(CT.square(num)))
	print("My name is {}".format(CT.name()))
Charles()
def decorator(F):
	class wrapper:
		def __init__(self, *args):
			self.w = F(*args)
		def squared(self, n):
			return self.w.square(n)
		def cubed(self, n):
			return self.w.cube(n)
			
	return wrapper

@decorator
class L:
	def __init__(self, square, cube):
		self.square = square
		self.cube = cube
		
def Charles():
	for n in range(1, 7):
		lamb = L(lambda x: x ** 2, lambda x: x **3)
		print("{} squared is {} and {} cubed is {}".format(n, lamb.squared(n), n, lamb.cubed(n)))
Charles()
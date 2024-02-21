class Invoke:
	def __init__(self, F):
		self.F = F
	def __call__(self):
		self.F(1, 2)
@Invoke
def Charles(a, b):
	print("{}, {}".format(a, b))
Charles()
	
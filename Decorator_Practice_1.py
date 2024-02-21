def decorator(cls):
	class Wrapper:
		def __init__(self, *args):
			self.w = cls(*args)
		def __call__(self, n):
			getattr(self.w, n)
			print(self.w)
			return 0
		def sq(self):
			return self.w.x(16)
		def name(self):
			print(self.w.y)
	return Wrapper			
@decorator
class C:
	def __init__(self, x, y):
		self.x = x
		self.y = y
def main(f, name):
	D = C(f, name)
	print(D.sq())
	D.name()
main(f = lambda x: x ** 2, name="Charles")
class R:
	def __init__(self, token):
		self.token = token

class S:
	def __init__(self, token):
		if (token in ['OR', 'AND', 'NOT', '.', '+', '?']):
			self.token = token
		else:
			raise Exception("nope")

_char = " "
while _char in '\t #':
	if _char == ' ':
		print("true")
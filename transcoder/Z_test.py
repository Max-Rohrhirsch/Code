


def flatten(_array):
	if isinstance(_array, list):
		res = ''
		for element in _array:
			res += str(flatten(element)) + ' '
		return res + '\n'
	return _array

print(flatten(["if", ["a"], "in", [3, 4], ":", ["djdjf:", ["res"]]]))







for a in [4]:
    print("hi")
    if a = 4:
        print("not")



















# .

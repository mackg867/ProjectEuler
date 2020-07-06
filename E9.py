

def compute():
	for a in range(1,1001):
		for b in range(1,1001):
			if 1000-a-b < 0:
				break
			if (a**2+b**2) == (1000-a-b)**2:
				return [a,b,1000-a-b,a*b*(1000-a-b)]

	return('empty')








if __name__ == '__main__':
	print(compute())
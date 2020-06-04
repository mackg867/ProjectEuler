from eulerlib import primes

def compute():
	end_num = 2000000
	nums = [True] * end_num
	nums[:2] = [False] * 2
	for i in range(end_num):
		if nums[i]:
			for j in range(i*i, end_num, i):
				nums[j] = False

	temp = [i for i, x in enumerate(nums) if x]
	return(sum(temp))


# Call the sieve of Eratosthenes and sum the primes found.
def compute2():
	ans = sum(primes(1999999))
	return str(ans)


if __name__ == '__main__':
	print(compute())
	print(compute2())

Fibonacci Sequence
# TODO: Write function to return nth term of Fibonacci Sequence

from functools import lru_cache # least recently used cached

@lru_cache(maxsize = 1000)
def fibonacci(n):
	# Check that the input is a positive integer
	if type(n) != int:
		raise TypeError("n must be a positive int")
	if n < 1:
		raise TypeError("n must be a positive int")
	if n == 1:
		return 1
	elif n == 2:
		return 1
	elif n > 2:
		return fibonacci(n - 1) + fibonacci(n - 2)

for n in range(1, 501):
	print(n, ":", fibonacci(n))

# memoization - cache values
# clarity over compactness golden ratio??

# implic
fibonacci_cache = {}
def fibonacci(n):
	# if we have cached the value, then return it
	if n in fibonacci_cache:
		return fibonacci_cache[n]
	#  compute the nth term
	if n == 1:
		value = 1
	elif n <= 2:
		value = 1
	elif n > 2:
		value = fibonacci(n - 1) + fibonacci(n - 2)
	#  cache the value and return
	fibonacci_cache[n] = value
	return value

for n in range(1, 1001):
	print(n, ":", fibonacci(n))


# random walk - monte carlo
import random

def random_walk(n):
	"""Return coordinates after 'n' block random walk."""
	x = 0
	y = 0
	for i in range(n):
		step = random.choice(['N', 'S', 'E', 'W'])
		if step == 'N':
			y = y + 1
		elif step == 'S':
			y = y - 1
		elif step == 'E':
			x = x + 1
		else:
			x = x - 1
	return (x, y)

def random_walk_2(n):
	x, y = 0, 0
	for i in range(n):
		(dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
		x += dx
		y += dy
	return (x, y)

for i in range(25):
	walk = random_walk(10)
	print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

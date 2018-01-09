import itertools


def read_input(filepath):
	with open(filepath) as f:
		return [[int(x) for x in line.strip().split()] for line in f]


def solve(input):
	return sum(max(l) - min(l) for l in input)


def solve2(input):
	s = 0
	for l in input:
		for x,y in itertools.combinations(l, 2):
			x,y = max(x,y), min(x,y)
			if x // y == x / y:
				s += x // y
				break
	return s


if __name__ == "__main__":
	input = read_input("day02.txt")

	ans = solve(input)
	print(f"Part1: {ans}")

	ans = solve2(input)
	print(f"Part2: {ans}")
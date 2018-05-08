def read_input(filepath):
	with open(filepath) as f:
		return [int(line.strip()) for line in f]


def solve(input):
	size = len(input)
	n = 0
	nb_steps = 0
	while 0 <= n < size:
		input[n] += 1

		n += input[n] - 1
		nb_steps += 1

	return nb_steps


def solve2(input):
	size = len(input)
	n = 0
	nb_steps = 0
	while 0 <= n < size:
		jump_size = input[n]
		input[n] += 1 if jump_size < 3 else -1

		n += jump_size
		nb_steps += 1

	return nb_steps


if __name__ == "__main__":
	input = read_input("day05.txt")

	ans = solve(input)
	print(f"Part1: {ans}")

	input = read_input("day05.txt")
	ans = solve2(input)
	print(f"Part2: {ans}")
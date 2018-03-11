import collections
 

def read_input(filepath):
	with open(filepath) as f:
		return [line.strip().split() for line in f]


def solve(input):
	return sum(len(line) == len(set(line)) for line in input)
	#return sum(collections.Counter(line).most_common(1)[0][1] == 1 for line in input)


def solve2(input):
	return sum(len(line) == len(set("".join(sorted(x)) for x in line)) for line in input)
	
	#Worked for my input but doesnt work for "abb" and "aab"
	#return sum(collections.Counter([frozenset(x) for x in line]).most_common(1)[0][1] == 1 for line in input)


if __name__ == "__main__":
	input = read_input("day04.txt")

	ans = solve(input)
	print(f"Part1: {ans}")

	ans = solve2(input)
	print(f"Part2: {ans}")

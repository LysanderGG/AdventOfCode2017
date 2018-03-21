input = 361527


from enum import Enum


class Direction(Enum):
	LEFT = (-1, 0)
	RIGHT = (1, 0)
	TOP = (0, 1)
	BOT = (0, -1)


def next_dir(d):
	next_direction = {
		Direction.LEFT: Direction.BOT,
		Direction.BOT: Direction.RIGHT,
		Direction.RIGHT: Direction.TOP,
		Direction.TOP: Direction.LEFT,
	}

	return next_direction[d]

def generate(max):
	l = {}
	c = (0, 0)
	dir = Direction.RIGHT
	go_top_next = False

	for i in range(1, max+1):
		l[i] = c
		if go_top_next:
			dir = Direction.TOP
			go_top_next = False
		elif abs(c[0]) == abs(c[1]):
			if dir == Direction.RIGHT:
				go_top_next = True
			else:
				dir = next_dir(dir)

		c = (c[0] + dir.value[0], c[1] + dir.value[1])

	return l


def adjacent_values_sum(l, coord):
	res = 0
	adj_list = [
		(-1, -1),
		(-1,  0),
		(-1,  1),
		( 0, -1),
		( 0,  1),
		( 1, -1),
		( 1,  0),
		( 1,  1)
		]

	for c in adj_list:
		adj = (c[0] + coord[0], c[1] + coord[1])
		if adj in l:
			res += l[adj] 

	return res


def generate2(max):
	l = {(0,0) : 1}
	c = (1, 0)
	dir = Direction.RIGHT
	go_top_next = True
	last_val = 1
	
	while last_val < max:
		last_val = adjacent_values_sum(l, c)
		l[c] = last_val

		if go_top_next:
			dir = Direction.TOP
			go_top_next = False
		elif abs(c[0]) == abs(c[1]):
			if dir == Direction.RIGHT:
				go_top_next = True
			else:
				dir = next_dir(dir)

		c = (c[0] + dir.value[0], c[1] + dir.value[1])

	return last_val



def solve(input):
	grid = generate(input)
	return abs(grid[input][0]) + abs(grid[input][1])


def solve2(input):
	return generate2(input)


if __name__ == "__main__":

	ans = solve(input)
	print(f"Part1: {ans}")

	ans = solve2(input)
	print(f"Part2: {ans}")

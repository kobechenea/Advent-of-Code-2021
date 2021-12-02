f = open("input.txt")
lines = f.readlines()

data = []

for l in lines:
	data.append(l)

depth = 0
horiz = 0

for i in range(len(data)):
	data[i] = data[i].split()
	direction = data[i][0]
	val = int(data[i][1])

	#print(direction, val)

	if direction == "forward":
		horiz += val
	if direction == "up":
		depth -= val
	if direction == "down":
		depth += val

ans = depth * horiz

print(depth)
print(horiz)
print(ans)

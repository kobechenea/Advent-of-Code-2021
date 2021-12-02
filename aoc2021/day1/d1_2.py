f = open("input.txt")
lines = f.readlines()

data = []

for l in lines:
	data.append(int(l))

count = 0
prev = 0
curr = 0

for i in range(2,len(data)):
	curr = data[i] + data[i-1] + data [i-2]
	if prev == 0:
		prev = curr
		continue
	if curr > prev:
		count += 1
	prev = curr

print(count)
	

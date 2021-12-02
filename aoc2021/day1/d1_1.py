f = open("input.txt")
lines = f.readlines()

data = []

for l in lines:
	data.append(int(l))

count = 0

for i in range(1,len(data)):
	if data[i] > data[i-1]:
		count += 1

print(count)
	

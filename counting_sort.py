def sort(a, k):
	c = []
	b = []
	for i in range(len(a)):
		b.append(0)
	for i in range(k):
		c.append(0)
	for i in range(len(a)):
		c[a[i]] = c[a[i]] + 1
	for i in range(1, k):
		c[i] = c[i] + c[i - 1]
	for i in range(len(a)-1, -1, -1):
		b[c[a[i]]-1	] = a[i]
		c[a[i]] = c[a[i]] - 1
	return b

def main():
	inp = [2, 5, 3, 0, 2, 3, 0, 3]
	k = 6
	print('Unordered: ', inp)
	print('Ordered: ', sort(inp, k))

main()

def intervalos_n(a, k, d, e):
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
	valor_n = c[e] - c[d]
	return valor_n

def main():
	inp = [2, 5, 3, 0, 2, 3, 0, 3]
	k = 6
	print(intervalos_n(inp, k, 1, 3))

main()
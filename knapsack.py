from random import randint
import time
def knapsack_lesstrash(W, w, v, n):
	# matrix construction
	K = [[0 for i in range(W+1)] for j in range(n+1)]
	for i in range(n+1):
		for j in range(W+1):
			# no capacity or no items
			if i == 0 or j == 0:
				K[i][j] = 0
			# item not in the knapsack
			elif w[i-1] > W:
				K[i][j] = K[i-1][j]
			# max between item in the knapsack or not
			else:
				K[i][j] = max(v[i-1] + K[i-1][j-w[i-1]], K[i-1][j])

	return K[n][W]


def knapsack_trash(W, w, v, n):
	if W == 0 or n == 0:
		return 0
	if w[n-1] > W:
		return knapsack_trash(W, w, v, n-1)
	else:
		return max(v[n-1] + knapsack_trash(W - w[n-1], w, v, n-1), 
			knapsack_trash(W, w, v, n-1))

def update(w,v,W,n):
	for i in range(2*W):
		v.append(randint(1,20))
		w.append(randint(1,2))
	W *= 2
	n *= 2

def main():
	w = [10,20,30]
	v = [60,100,120]
	W = 50
	n = 3
	print(knapsack_trash(W, w, v, n))
	# for i in range(20):
	# 	start = time.time()
	# 	value = knapsack_trash(W, w, v, n)
	# 	print('Rodou recursivo em ', time.time() - start , ' segundos')
	# 	update(w,v, W,n)

if __name__ == '__main__':
	main()


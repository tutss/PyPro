# Baseado na aula de Análise de Algoritmos


# Função que faz a recursão para encontrar a soma
# otimizada
def cutting_rods(p, n, r):
	if r[n] >= 0:
		return r[n]
	else: 
		q = -1
		for i in range(n):
			# máximo entre o q e o preço somado a os otimizados
			# já calculados.
			q = max(q, p[i] + cutting_rods(p, n-i-1, r))
		r[n] = q
		return q

# Vetor das somas otimizadas é r
def return_value(p, n):
	r = []
	r.append(0)
	for i in range(n):
		r.append(-1)
	print(r)
	return cutting_rods(p, n, r)


def main():
	# p = [int(x) for x in input().split()]
	p = [1, 5, 8, 9]
	print(return_value(p, len(p)))

main()

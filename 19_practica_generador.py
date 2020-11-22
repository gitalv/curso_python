# yield

def generaPares(limite):
	num = 1
	miLista = []
	while num < limite:
		miLista.append(num * 2)
		num += 1
	return miLista

print(generaPares(10))



def generaParesGenerador(limite):
	num = 1
	while num < limite:
		yield num * 2
		num += 1

#print(generaParesGenerador(10)) # <generator object generaParesGenerador at 0x02D3AE60>
devuelvePares = generaParesGenerador(10)
for i in devuelvePares:
	print(i)

devuelvePares = generaParesGenerador(10)
print(next(devuelvePares))
print("Más codigo")
print(next(devuelvePares))
print("Más codigo")
print(next(devuelvePares))
print("Más codigo")
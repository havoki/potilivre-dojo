def umAcem():
	lista = []
	lista = range(1, 101)
	return lista

def getElement(lista):
	for a in lista:
		if(a%3 == 0 and a%5 == 0): 
			return "FizzBuzz"
		elif(a%3 == 0):
			return "Fizz"
		elif(a%5==0):
			return "Buzz"



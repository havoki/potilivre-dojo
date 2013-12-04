import unittest 
import dojo

class listar(unittest.TestCase):
	def testa_lista_size(self):
		lista = dojo.umAcem()	
		self.assertEqual(
				range(1, 101),
				lista
			)

	def testa_fizz(self):
		lista = range(1, 4)
		fizzTest = dojo.getElement(lista)

		self.assertEqual(
				"Fizz",
				dojo.getElement(lista)
			)
	def testa_buzz(self):
		lista = range(4, 6)
		buzzTest = dojo.getElement(lista)


		self.assertEqual(
			"Buzz",
			dojo.getElement(lista)
			)
	def testa_fizz_buzz(self):
		lista = range(14, 16)
		fizzBuzzTest = dojo.getElement(lista)


		self.assertEqual(
			"FizzBuzz",
			dojo.getElement(lista)
			)	

if __name__ == "__main__":
	unittest.main()


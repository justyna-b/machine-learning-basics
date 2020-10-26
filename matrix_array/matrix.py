import numpy as np

arrayZeros = np.zeros(10)
arrayFives = np.ones(10)*5
print("tablica zawierająca 10 zer: ")
print(arrayZeros)
print("---------------------------------------------------------------------------------", '\n')

print("tablica zawierająca 10 piątek: ")
print(arrayFives)
print("---------------------------------------------------------------------------------", '\n')

print("tablica zawierająca liczby od 10 do 50: ")
arrayFromTo = np.arange(10, 51, 1)
print(arrayFromTo)
print("---------------------------------------------------------------------------------", '\n')

print("macierz o wymiarach 3x3 zawierająca liczby od 0 do 8: ")
x =  np.arange(0, 9).reshape(3,3)
print(x)
print("---------------------------------------------------------------------------------", '\n')


print("macierz jendostkowa o wymiarach 3x3: ")
y = np.eye(3)
print(y)
print("---------------------------------------------------------------------------------", '\n')

print("macierz o wymiarach 5x5 zawierającą liczby z dystrybucji normalnej: ")
mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 25).reshape(5,5)
print(s)
print("---------------------------------------------------------------------------------", '\n')

print("macierz o wymiarach 10x10 zawierającą liczby od 0,01 do 1 z krokiem 0,01")
template = np.arange(0.01, 1.01, 0.01).reshape(10,10)
print(template)
print("---------------------------------------------------------------------------------", '\n')

print("tablica zawierająca 20 liniowo rozłożonych liczb między 0 a 1")
linearArray = np.arange(0, 1.05, 0.05)
print(linearArray)
print("---------------------------------------------------------------------------------", '\n')

print("tablica zawierająca losowe liczby z przedziału (1, 25) zamieniona na macierz 5x5:")
arrayRand = np.random.randint(1, 25, (25))
arrayRand = arrayRand.reshape(5, 5)
print(arrayRand)

print("suma wszystkich liczb w macierzy: ", end='')
print(np.sum(arrayRand))

print("średnia wszystkich liczb w macierzy: ", end='')
print(np.mean(arrayRand))

print("standardowa dewiacja dla wszystkich liczb w macierzy: ", end='')
print(np.std(arrayRand))

print("suma każdej kolumny w macierzy zapisana do tablicy: ")
print(np.cumsum(arrayRand))
print("---------------------------------------------------------------------------------", '\n')

print("macierz 5x5 zawierająca losowe liczby z przedziału (0, 100)")
matrixRand = np.random.randint(100, size=(5, 5))
print(matrixRand)

print("mediana liczb w tej macierzy: ", end='')
print(np.median(matrixRand))

print("najmiejsza wśród liczb tej macierzy: ", end='')
print(np.min(matrixRand))

print("największa wśród liczb tej macierzy: ", end='')
print(np.max(matrixRand))
print("---------------------------------------------------------------------------------", '\n')

print("macierz o wymiarach x!=y zawierająca losowe liczby z przedziału (0, 100)")
matrixToTranspose = np.random.randint(100, size=(3, 5))
print(matrixToTranspose)
print("transpozycja zadanej macierzy")
print(np.transpose(matrixToTranspose))
print("---------------------------------------------------------------------------------", '\n')

matrixA = np.random.randint(10, size=(7,3))
matrixB = np.random.randint(10, size=(7, 3))
print("matrixA= ", '\n', matrixA, '\n', "matrixB= ", '\n', matrixB)
print("wynik po dodaniu do macierzy A macierzy B: ", '\n', matrixA.__add__(matrixB))
print("---------------------------------------------------------------------------------", '\n')

matrixA = np.random.randint(10, size=(3,5))
matrixB = np.random.randint(10, size=(5, 7))
print("matrixA= ", '\n', matrixA, '\n', "matrixB= ", '\n', matrixB)
print("wynik po pomnorzeniu macierzy A przez macierz B: ", '\n', np.matmul(matrixA, matrixB))

print('\n', "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ", '\n')
print("wynik po pomnorzeniu macierzy A przez macierz B drugim sposobem: ", '\n', matrixA.dot(matrixB))
import numpy as np

np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])  # tablica wielowymiarowa

print(np1)
print(np1.shape)  # ilość elementów w tablicy

np2 = np.arange(10) # drukuje liczby od 0 do x
print(np2)

np3 = np.arange(1, 10, 2) # drukuje liczby od 1 do 10  co 2
print(np3)

np4 = np.arange(10).reshape(2, 5) # drukuje liczby od 0 do x w tablicy 10x10
print(np4)

# konwertowanie listy python na numpy

lista = [0,1,2,3,4,5]

lista = np.array(lista)

print(lista)
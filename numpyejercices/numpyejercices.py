
import numpy as np


a=np.array([1,2,3 ])

print(type(a))

print(a.shape)

print(a[2])

a[0]=100
a[1]+=1000
a[2]-=1000

print(a)




b = np.array([[1, 2, 3], [1, 2, 3]])
print(type(b))
print(b.shape)
print(b)


print(b[1,1])
b[1,2]+=100

print(b)

a=np.zeros([4,5])
print(a)
print(a.shape)

b=np.ones((3,4))
print(b)


c=np.eye(4)
print(c)


d=np.full((5,5),8)
print(d)


e=np.random.random((3,3))
print(e)


f = np.random.choice(np.arange(1, 11), size=(3, 4))
print(f)


print('*************************')
g = np.random.randint(11, 100, size=(3, 4))
print(g)

sub = g[0:2, 1:3]
print(sub)
print("*" * 40)

print('*************************')
h = np.random.randint(11, 20, size=(5, 4))
print(h)

subt = h[0:2, 0:3]
print(subt)
print("*" * 40)


a=np.array([[1,2],[3,4],[5,6]])
print(a)
print(a.shape)

filter=(a>2)
print(filter)

arreglo = np.linspace(1, 100, 49, dtype=int).reshape(7, 7)
print("Arreglo original 7x7:")
print(arreglo)

# Filtrar valores entre 40 y 60
filtro = arreglo[(arreglo >= 40) & (arreglo <= 60)]
print("\nValores filtrados (entre 40 y 60):")
print(filtro)
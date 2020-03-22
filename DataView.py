import matplotlib.pyplot as plt 

y = [1, 2, 5, 3, 8]
x = [2, 3, 7, 5, 4]

plt.title("Grafico em Python")

plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")


plt.bar(x, y)
plt.show()
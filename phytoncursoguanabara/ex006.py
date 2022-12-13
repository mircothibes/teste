# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.


n = int(input("digite um numero: "))
d = n * 2
t = n * 3
r = n ** (1 / 2)
print("O dobro é {} \nO triplo é {} \nraiz é {}".format(d, t, r))

n = int(input("digite um numero: "))
print("O dobro é {} \nO triplo é {} \nraiz é {:.2f}".format((n * 2), (n * 3), (n ** (1 / 2))))

'''Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
'''

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
n3 = (n1 + n2) / 2
print("A sua primeira nota foi {}, a sua segunda nota foi {}, sendo assim sua media é {:.1f} ".format(n1, n2, n3))
if n3 >= 7:
    print("APROVADO")
elif n3 < 7:
    print("Prestar Exame")

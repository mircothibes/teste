'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.'''

larg = float(input("Qual a largura: "))
alt = float(input("Qual a altura: "))
area = larg * alt
print("Sua parede tem a dimensão de {} x {} e sua area é de {:.2f}m2".format(larg, alt, area))
tinta = area / 2
print("Para pintar esta parede, você precisará de  {} de tinta." . format(tinta))





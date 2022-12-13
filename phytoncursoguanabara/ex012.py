'''Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
'''

preço = float(input("Qual o preço do produto: R$"))
novo_preço = preço - (preço * 5 / 100)
print("Seu preço era é de R${:.2f}, e agora com 5% de desconto seu novo preço é de R${:.2f}" .format(preço, novo_preço))

'''Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.'''

km_percorido = float(input("Quantos Km foram percoridos: "))
quantos_dias = int(input(("Quantos dias foram de aluguel: ")))
a_pagar1 = km_percorido * 0.15
a_pagar2 = quantos_dias * 60
print('Você alugou o carro por {} dias e pagou '
      'o valor de R${}, e rodou {:.2f}km,\nsendo assim irá pagar R${:.2f} pelos Kilometros rodados.'
      .format(quantos_dias, a_pagar2, km_percorido, a_pagar1))




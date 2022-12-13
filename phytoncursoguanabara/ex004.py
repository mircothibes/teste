# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

a = input('digite um valor: ')
print('O tipo primitivo desse valor', type(a))
print('Só tem espaços?', a.isspace())
print('O valor é numerico?', a.isnumeric())
print('O valor é com letra alphabetico?', a.isalpha())
print('O valor é alphanumerico?', a.isalnum())
print('O valor é com letra maiuscula?', a.isupper())
print('O valor é com letra minuscula?', a.islower())






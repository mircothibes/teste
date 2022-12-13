'''Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros'''

media = float(input("Uma distancia em metros: "))
cm = 100 * media
dm = 1000 * media
print("A medida de {} metros corresponde a {} centimetros e {} decimetros" .format(media, cm, dm))


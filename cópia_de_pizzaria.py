# -*- coding: utf-8 -*-
"""Cópia de pizzaria

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ud0zi15NdoDvuKxeugErTgoen_oghvlE
"""

print('Pizzaria Rancho Mineiro')
print('Pizzaria de Cuiabá')

print('Pizza')

print('Opção 1: mussarela e tomate R$ 40,00')
print('Opção 2: Frango supremo R$ 32,00')
print('Opção 3: Mexicana R$ 26,00')
print ('Opção 4: Italiano R$ 30,00' )
print ('Opção 5: Americana R$ 35,00')
print ('Opção 6: vegetariana R$ 46,00 ')
print ('Opção 7: Calabresa R% 40,00')
print ('Opção 8: Havaiana R$ 30,00')
print ('Opção 9: Pepperoni R$ 35,00')
print ('Opção 10: Presunto e queijo R$ 35,00')
print ('Opção 11: Mineira R$ 30,00')

pedido = 'S'

while (pedido == 'S'):
  pedido=str(input('Deseja pedir uma ou mais pizza? S/N'));

  if (pedido=='S'):
    op=float(input('Digite o código da sua pizza: '));

  if(op==1):
    vl = 40.00
    print('Você digitou a opção 1: mussarela e tomate')
  elif(op==2):
    vl = 32.00
    print('Você digitou opção 2: Frango supremo')
  elif(op==3):
    vl = 26.00
    print('Você digitou a opção 3: Mexicana')
  elif(op==4):
    vl = 30.00
    print('Você digitou a opção 4: Italiano')
  elif(op==5):
    vl = 35.00
    print ('Você digitou a opção 5: Americana')
  elif(op==6):
    vl = 46.00
    print('Você digitou a opção 6: Vegetariana')
  elif(op==7):
    vl = 40.00
    print('Você digitou a opção 7: Calabresa')
  elif (op==8):
    vl = 30.00
    print('Você digitou a opção 8: Havaiana ')
  elif (op==9):
    vl = 35.00
    print ('Você digitou a opção 9: Pepperoni')
  elif (op==10):
    vl = 35.00
    print ('Você digitou a opção 10: Presunto e queijo')
  elif (op==11):
    vl = 30.00
    print ('Você digitou a opção 11: Mineira')

  quanti=int(input('Digite a quantidade:'))

  vl = vl * quanti

  pedido=str(input('Deseja pedir novamente: S/N'));
    
acom= 'S'

while(acom == 'S'):
  acom=str(input('Deseja acompanhamento? S/N'))

  print ('Opção 1: Pão de alho R$ 6,00')
  print ('Opção 2: Batata frita R4 18,00')
  print ('Opção 3: Esfirras com fritas R$ 20,00')
  print ('Opção 4: Salada variada R$ 6,00')
  print ('Opção 5: Batata recheada R4 12,00')
  print ('Opção 6: Batata rustica R$ 16,00')
  acom1 = float (input ('Qual opção deseja?'))

  if (acom1==1):
    valor = 6.00
  elif (acom1==2):
    valor = 18.00
  elif (acom1==3):
    valor = 20.00
  elif (acom1==4):
    valor = 6.00
  elif (acom1==5):
    valor = 12.00
  elif (acom1==6):
    valor = 16.00

  quantia=int(input('Digite a quantidade de acompanhamento:'));
  valor = valor * quantia  

  acom=str(input('Deseja pedir novamente:'))

bebidas= 'S'
while (bebidas == 'S'):
  bebidas=str(input('Quer inclui bebidas: S/N'));

  if (bebidas =='S'):
    print('Opção 1: Coca cola 2 litros R$ 12,00')
    print('Opção 2: Suco de laranja  1 litros R$ 12,00')
    print('Opção 3: Fanta laranja 2 litros R$ 13,00')
    print ('Opção 4: Sprint 2 litros R$ 14,00')

  bebes=int(input('Qual opção deseja: '))

  if (bebes==1):
    vlor= 12.00
    print('Você escolheu opção 1: Coca Cola')
  elif (bebes==2):
    vlor=12.00
    print('Você escolheu opção 2: Suco de laranja')
  elif (bebes==3):
    vlor=13.00
    print('Você escolheu opção 3: Fanta laranja')
  elif (bebes == 4):
    vlor=14.00
    print('Você escolheu opção 4: Sprint')

  quant=int(input('Digite a quantia desejada:'))

  vlor = vlor * quant

  bebidas=str(input('Quer bebida pedir novamente:'))

while (bebidas == 'N'):
  print('O valor total do pedido é',vl+valor+vlor)
  break
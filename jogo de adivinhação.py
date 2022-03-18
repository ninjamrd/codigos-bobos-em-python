from random import randint
x=randint(0,5)
y=int(input('adivinhe o numero de 0 a 5:'))
print('você venceu' if x==y else 'você perdeu o numero era {}'.format(x))

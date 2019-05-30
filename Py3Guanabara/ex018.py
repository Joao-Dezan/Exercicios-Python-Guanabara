import math, emoji
print(emoji.emojize(':boom: 18ª :boom:  aula  :boom: de  :boom: Python :exclamation:', use_aliases=True))
an = float(input('Digite o ângulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))
print('O seno de {}° é {:.2f}\nO cosseno de {}° é {:.2f}\nA tangente de {}° é {:.2f}'.format(an, sen, an, cos, an, tan))

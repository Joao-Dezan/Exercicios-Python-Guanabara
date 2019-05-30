from time import sleep
import emoji
print('Os fogos de artifícios começam em:')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize('\033[31m:boom: :boom::boom:\n :boom:  :boom:\033[m', use_aliases=True))
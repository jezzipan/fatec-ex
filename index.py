from __future__ import unicode_literals

def xadrez(n):
    for i in range(n):
        for j in range(n):
            if (i+j) % 2 == 0: print(chr(9608)*2, end='')
            else: print(''*2, end='')
        print()

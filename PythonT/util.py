# util.h - funções úteis desenvolvidas para a disciplina IAL-501 (Prof. Silvio Lago)

from math import ceil, cos, exp, factorial, floor, hypot, log, log2, sin, sqrt
from random import *
from copy import copy, deepcopy
from time  import clock, time, sleep
from pylab import plot, title, legend, xlabel, ylabel, grid, show, ticklabel_format, hist, scatter, axis
from sys import stdout, stderr, setrecursionlimit
from re import findall
from itertools import product, permutations
import sys


#####################################################################################################
#                                      Recursão e rastreamento                                      #
#####################################################################################################

setrecursionlimit(2000)

def rastrear(f):
    '''Ativa ou desativa o rastreamento de chamadas e retornos da função f'''
    globais = sys._getframe().f_back.f_globals
    if '__orig__' in f.__dict__:
        f = f.__dict__.get('__orig__')
        f.__dict__.pop('i',None)
        globais[f.__name__] = f
    else:
        f.i = 0
        def nova(*x):
            print('%s%s%s' % ('| '*f.i, f.__name__, x if len(x)>1 else ('(%s)' % x[0])),file=stderr)
            sleep(0.25)
            f.i += 1
            y = f(*x)
            f.i -= 1
            print('%s%s' % ('| '*f.i,y))
            sleep(0.25)
            return y
        nova.__orig__ = f
        nova.__name__ = f.__name__
        globais[f.__name__] = nova


#####################################################################################################
#                                        Lógica proposicional                                       #
#####################################################################################################

def Bool(n):
    assert n>=1
    if n==1: return [False,True]
    return list(product([False,True],repeat=n))

def então(a,b): return (not a or b)

#####################################################################################################
#                                        Estados e asserções                                        #
#####################################################################################################

def R(x): return isinstance(x,(int,float))

def Z(x): return isinstance(x,int)

def N(x): return isinstance(x,int) and (x>=0)

def sat(*args,s0=False):
    '''Verifica se um estado satisfaz um conjunto de asserções.
       Use  $v  para denotar o valor inicial de uma variável v.'''

    def var(x): return isinstance(x,(bool,int,float,list,set,tuple))

    if len(args)>0 and isinstance(args[0],dict): estado = args[0]; args=list(args[1:])
    
    elif sys._getframe().f_back.f_code.co_name=='<module>':
        estado = dict((x,v) for (x,v) in sys._getframe().f_back.f_locals.items() if var(v) and x not in __builtins__)
    else:
        estado  = sys._getframe().f_back.f_locals

    if sat.__dict__.get('caller','') != sys._getframe().f_back.f_code.co_name:
        sat.caller = sys._getframe().f_back.f_code.co_name
        s0 = True

    if sys._getframe().f_back.f_code.co_name=='<module>':
        sat.Δ = {}
    else:
        sat.Δ =  sys._getframe().f_back.f_globals[sys._getframe().f_back.f_code.co_name].__dict__
    
    if s0:
        sat.τ,sat.σ,sat.ι = (0,{},{})
        if 'pre' in sat.Δ: print('pre: α ≐ %s' % sat.Δ['pre'])
        if 'gua' in sat.Δ: print('gua: β ≐ %s' % sat.Δ['gua'])
        if 'inv' in sat.Δ: print('inv: γ ≐ %s' % sat.Δ['inv'])
        if 'pos' in sat.Δ: print('pos: δ ≐ %s' % sat.Δ['pos'])
        
    args = sorted(sat.Δ.keys()) + list(args)

    sat.ι.update(dict(deepcopy(list((n,estado[n]) for n in (set(estado)-set(sat.σ))))))
    sat.σ = dict(deepcopy(list(estado.items())))
    if sat.τ==0 and len(sat.Δ)>0: print()
    s = ', '.join(('%s↦%s' % (v,estado[v])).replace(' ','') for v in sorted(estado.keys()))
    if s: print('σ%s: ⟨%s⟩ ' % (sat.τ,s),end='')
    sat.τ += 1

    globais = dict(p for p in sys._getframe().f_back.f_globals.items() if callable(p[1]))
    for k in sys._getframe().f_back.f_code.co_varnames: globais.pop(k,None)
    globais.update(estado)

    símbolo = {'pre':'α','gua':'β','inv':'γ','pos':'δ'}
    resultados = []
    
    for (i,nome) in enumerate(args):
        asserção = sat.Δ.get(nome,nome)
        if not isinstance(asserção,str): continue
        for s in findall(r'\$\w+',asserção):
            asserção = asserção.replace(s,'sat.ι["'+s[1:]+'"]')
        try: v = eval(asserção,globais,estado)
        except NameError as ne:
            if ne.__str__().split("'")[1] in sys._getframe().f_back.f_code.co_varnames: continue
            raise NameError
        nome = símbolo.get(nome,nome)
        fmt = '%s' if nome.isidentifier() else '(%s)'
        resultados.append(('%%s%s ' % fmt) % ('' if v else '¬',nome))
    resultados.sort(key= lambda x: x[1] if x[0]=='¬' else x[0])
    if len(resultados)>0:
        print('⊨ ',end='')
        for (i,s) in enumerate(resultados):
            if i>0: print('∧ ',end='')
            print('%s' % s,end='',file=(stdout if s[0]!='¬' else stderr))
        
    if s: input()


def satrec(f):
    '''Ativa ou desativa a verificação de precondição e poscondição
       da função recursiva f. Use _res  para denotar o resultado da
       função f.'''
    if 'orig' in f.__dict__:
        f = f.__dict__.get('orig')
        sys._getframe().f_back.f_globals[f.__name__] = f
        return
    var  = f.__code__.co_varnames
    def g(*args):
        sat(dict(zip(var,args)),s0=(g.depth==0))
        g.depth += 1
        _res = f(*args)
        g.depth -= 1
        sat(dict(zip(var+('_res',),args+(_res,))))
        if g.depth == 0: sat.τ = 0
        return _res
    g.pre = f.__dict__.get('pre','True')
    g.pos = f.__dict__.get('pos','True')
    g.depth = 0
    g.orig = f 
    sys._getframe().f_back.f_globals[f.__name__] = g
    sys._getframe().f_globals['g'] = g
    g.__name__ = f.__name__


#####################################################################################################
#                                        Gráficos de funções                                        #
#####################################################################################################

def lg(n) : return log2(n)

def gráfico(*F,N=(1,10,1)):
    '''Mostra os gráficos das funções F com entrada n em N=(1,10,1)'''
    M = ['o','s','d','h','p','x','*','v','^','<','>']
    C = ['b','r','g','c','m','y']
    X = range(N[0],N[1]+1,N[2])
    for i,f in enumerate(F):
        Y = [f(x) for x in X]
        c = C[i%len(C)]
        m = M[i%len(M)]
        plot(X,Y,color=c,marker=m,linewidth=1,label=f.__name__)
    xlabel(F[0].__code__.co_varnames[0])
    ylabel('%s(%s)' % (F[0].__name__,F[0].__code__.co_varnames[0]))
    ticklabel_format(style='sci', axis='both', scilimits=(-3,+4))
    legend(loc='upper left')
    grid(True)
    show()

#####################################################################################################
#                                        Geração de sequências                                      #
#####################################################################################################

def U(*args):
    '''Devolve uma função para escolha de valor em distribuição discreta uniforme
       U(a,b): escolhe valores no intervalo [a,b)
       U(s)..: escolhe valores na sequência s'''
    if len(args)==2 and isinstance(args[0],int) and isinstance(args[1],int): X = range(args[0],args[1])
    elif len(args)==1 and isinstance(args[0],(range,list,tuple,str)): X = args[0]
    else: raise Exception('parâmetros inválidos!')
    def escolha(): return choice(X)
    return escolha

def A(*args,mostra=False):
    '''Devolve uma função para escolha de valor em distribuição discreta aleatória (com no máximo 50 categorias)
       A(a,b): escolhe valores no intervalo [a,b)
       A(s)..: escolhe valores na sequência s'''
    if len(args)==2 and isinstance(args[0],int) and isinstance(args[1],int): X = range(args[0],args[1])
    elif len(args)==1 and isinstance(args[0],(range,list,tuple,str)): X = args[0]
    else: raise Exception('parâmetros inválidos!')
    if not isinstance(X[0],(range,list,tuple,str)) and len(X)>50:
        C = sorted(sample(range(1,len(X)),49)+[0,len(X)])
        X = [range(C[i],C[i+1]) for i in range(0,len(C)-1)]
    P = pda(len(X))
    if mostra: print('pda(%s)' % P)
    return M(X,P)

def M(X,P):
    '''Devolve uma função para escolha de valor numa distribuição discreta P'''
    if abs(1-sum(P))>1e-5: raise Exception('distribuição inválida!')
    I,P = alias(P)
    if isinstance(X[0],(range,list,tuple,str)):
        def escolha():
            k = floor(random()*len(I))
            if random()<P[k]: return choice(X[k])
            else: return choice(X[I[k]])
    else:
        def escolha():
            k = floor(random()*len(I))
            if random()<P[k]: return X[k]
            else: return X[I[k]]
    return escolha

def pda(k):
    '''Devolve uma função de probabilidade discreta aleatória com k>2 categorias'''
    if k<2: raise Exception('parâmetro inválido!')
    p = [0] + sorted([random() for i in range(k-1)]) +[1]
    d = [p[i]-p[i-1] for i in range(1,k+1)]
    return d

def alias(P):
    '''Devolve estrutura para escolha em tempo constante de valor em distribuição discreta P'''
    baixa = []
    alta = []
    for i in range(len(P)):
        P[i] *= len(P)
        if P[i]<1.0: baixa.append(i)
        else: alta.append(i)
    I = len(P)*[0]
    while len(baixa)>0 and len(alta)>0:
        i = baixa.pop()
        j = alta.pop()
        I[i] = j
        P[j] -=  (1.0 - P[i])
        if P[j]<1.0: baixa.append(j)
        else: alta.append(j)
    return I,P

def seq(n,*args):
    '''Devolve uma sequência com n itens aleatórios
       seq(n)....: n itens distintos são escolhidos no intervalo [0,10*n)
       seq(n,a,b): se n <= (b-a), n itens distintos são escolhidos no intervalo [a,b)
       seq(n,a,b): se n > (b-a), n itens são escolhidos em [a,b), com distribuição uniforme
       seq(n,f)..: n itens são escolhidos, de acordo com a função de probabilidade f'''
    if len(args)==0: return sample(range(0,10*n),n)
    if len(args)==2 and isinstance(args[0],int) and isinstance(args[1],int) and args[0]<args[1]:
        if n <= (args[1]-args[0]): return sample(range(args[0],args[1]),n)
        else: escolha = U(args[0],args[1])
    elif len(args)==1 and callable(args[0]): escolha = args[0]
    else: raise Exception('parâmetros inválidos!')
    return [escolha() for i in range(n)]


#####################################################################################################
#                                  Tempo de algoritmos de ordenação                                 #
#####################################################################################################

def tempo(f,*a):
    '''Devolve o tempo de execução (aproximado) de uma função f com argumentos *a'''
    i = time()
    f(*a)
    return time()-i

def troca(v,i,j):
    x = v[i]
    v[i] = v[j]
    v[j] = x

def cpu(*F,N=(500,5000,500)):
    '''Mostra gráfico com o consumo de tempo das funções *F, para
       entradas com tamanho variando no intervalo N=(500,5000,500).
       Um parâmetro E = g define a função que gera as entradas'''
    C = ['r','b','g','c','m','y','k','w']
    M = ['o','s','p','h','+','x','v','^']
    X = []
    Y = [[] for _ in range(len(F))]
    print('n = ',end='')
    inicio = time()
    rodada = 1
    for n in range(N[0],N[1]+1,N[2]):
        print('%s ' % rodada,end='')
        X.append(n)
        v = sample(range(0,n),n)
        for i,f in enumerate(F):
            w = deepcopy(v)
            Y[i].append(tempo(f,w))
        rodada += 1
    print('\nTempo total: %.1fs' % (time()-inicio))
    xlabel('tamanho da entrada')
    ylabel('tempo de execução (s)')
    ticklabel_format(style='sci', axis='both', scilimits=(-3,+4))
    grid(True)
    for i,f in enumerate(F):
        plot(X,Y[i],color=C[i%len(C)],marker=M[i%len(M)],label=f.__name__)
    legend(loc='upper left')
    show()




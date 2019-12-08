# -*- coding: utf-8 -*-
import io
import sys
import numbers
from random import randint
from random import randrange

entradasValidasDeSenha = ["A", "B", "C", "D", "E", "a", "b", "c", "d", "e"]

arquivoEntrada = 'MATR.TXT'
arquivoSaida = 'SENHAS.TXT'
listaMatriculas = []
listaSenhas = []
tipoGlobal = "inicializando tipo"
totalGlobal = 0

MAIUSCULAS_ASCII_PRIMEIRO_DECIMAL = 65
MAIUSCULAS_ASCII_ULTIMO_DECIMAL = 90

MINUSCULAS_ASCII_PRIMEIRO_DECIMAL = 97
MINUSCULAS_ASCII_ULTIMO_DECIMAL = 122

ALGARISMOS_ASCII_PRIMEIRO_DECIMAL = 48
ALGARISMOS_ASCII_ULTIMO_DECIMAL = 57

CARACTERES_ESPECIAIS_PARTE_I_ASCII_INICIO = 33
CARACTERES_ESPECIAIS_PARTE_I_ASCII_FIM = 46
CARACTERES_ESPECIAIS_PARTE_II_ASCII_INICIO = 58
CARACTERES_ESPECIAIS_PARTE_II_ASCII_FIM = 64

def confereSeNumeroEPar(numero):
  if (numero % 2) == 0:
    return True
  return False

def GerarNumeroAleatorioComNDigitos(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def leiaArquivo(nomeDoArquivo):
  with open(nomeDoArquivo) as arquivo:
      conteudoArquivoEmLista = arquivo.read().splitlines() 
  return conteudoArquivoEmLista


def regitrarArquivo(arquivoSaida, lista):
  arquivo = open(arquivoSaida, 'w') 
  for item in lista:
        arquivo.write("%s\n" % item)
  arquivo.close() 

def validaTipoSenha(SenhaDigitada):
  if entradasValidasDeSenha.count(SenhaDigitada): 
    return True 
  return False 


def leiaTipoSenha():
    global tipoGlobal
    global totalGlobal

    print("Por favor, escolha um tipo de senha:")
    print("a. Numérica – conterá apenas algarismos")
    print("b. Alfabética – conterá apenas letras maiúsculas e minúsculas")
    print("c. Alfanumérica 1 – conterá letras maiúsculas e algarismos")
    print("d. Alfanumérica 2 – conterá letras maiúsculas, minúsculas e algarismos")
    print("e. Geral – conterá letras maiúsculas, minúsculas, algarismos e os caracteres ASCII [33, 46] e [58, 64]")

    
    Tipo = sys.stdin.read(1) 
    if validaTipoSenha(Tipo): 
      tipoGlobal = Tipo
      totalGlobal = int (input ("Digite o tamanho da senha (número inteiro): "))
    else:
      print("Por favor, digite um tipo válido de senha.")
      exit()

def gerarSenhasTipo1(Tamanho):
  Senha = GerarNumeroAleatorioComNDigitos(Tamanho)
  return Senha

def gerarSenhasTipo1(Tamanho):
  senha = list(range(Tamanho))

  for indice in range(Tamanho):
    if confereSeNumeroEPar(indice):
     senha[indice] = chr(randrange(MAIUSCULAS_ASCII_PRIMEIRO_DECIMAL, MAIUSCULAS_ASCII_ULTIMO_DECIMAL + 1))
    else:
      senha[indice] = chr(randrange(MINUSCULAS_ASCII_PRIMEIRO_DECIMAL, MINUSCULAS_ASCII_ULTIMO_DECIMAL + 1))
  Senha = "".join((senha))
  return Senha

def gerarSenhasTipo3(Tamanho):

  senha = list(range(Tamanho))

  for indice in range(Tamanho):
    if confereSeNumeroEPar(indice):
      senha[indice] = chr(randrange(ALGARISMOS_ASCII_PRIMEIRO_DECIMAL, ALGARISMOS_ASCII_ULTIMO_DECIMAL + 1))
    else:
      senha[indice] = chr(randrange(MAIUSCULAS_ASCII_PRIMEIRO_DECIMAL, MAIUSCULAS_ASCII_ULTIMO_DECIMAL + 1))
  Senha = "".join((senha))
  return Senha

def gerarSenhasTipo4(Tamanho):
  opcoesAscii = {
    0: 'MAIUSCULAS',
    1: 'MINUSCULAS',
    2: 'ALGARISMOS',
    3: 'ESPECIAIS_I',
    4: 'ESPECIAIS_II',
  }
  senha = list(range(Tamanho))
  for indice in range(Tamanho):
    numeroAleatorio = randrange(0,3)
    if (opcoesAscii.get(numeroAleatorio) == 'MAIUSCULAS'):
      caractere = chr(randrange(MAIUSCULAS_ASCII_PRIMEIRO_DECIMAL, MAIUSCULAS_ASCII_ULTIMO_DECIMAL + 1))
    elif (opcoesAscii.get(numeroAleatorio) == 'MINUSCULAS'):
      caractere = chr(randrange(MINUSCULAS_ASCII_PRIMEIRO_DECIMAL, MINUSCULAS_ASCII_ULTIMO_DECIMAL + 1))
    elif (opcoesAscii.get(numeroAleatorio) == 'ALGARISMOS'):
      caractere = chr(randrange(ALGARISMOS_ASCII_PRIMEIRO_DECIMAL, ALGARISMOS_ASCII_ULTIMO_DECIMAL + 1))
    senha[indice] = caractere
  Senha = "".join((senha))
  return Senha

def gerarSenhasTipo5(Tamanho):
  opcoesAscii = {
    0: 'MAIUSCULAS',
    1: 'MINUSCULAS',
    2: 'ALGARISMOS',
    3: 'ESPECIAIS_I',
    4: 'ESPECIAIS_II',
  }
  senha = list(range(Tamanho))

  for indice in range(Tamanho):
    numeroAleatorio = randrange(0,5)
    if (opcoesAscii.get(numeroAleatorio) == 'MAIUSCULAS'):
      caractere = chr(randrange(MAIUSCULAS_ASCII_PRIMEIRO_DECIMAL, MAIUSCULAS_ASCII_ULTIMO_DECIMAL + 1))
    elif (opcoesAscii.get(numeroAleatorio) == 'MINUSCULAS'):
      caractere = chr(randrange(MINUSCULAS_ASCII_PRIMEIRO_DECIMAL, MINUSCULAS_ASCII_ULTIMO_DECIMAL + 1))
    elif (opcoesAscii.get(numeroAleatorio) == 'ALGARISMOS'):
      caractere = chr(randrange(ALGARISMOS_ASCII_PRIMEIRO_DECIMAL, ALGARISMOS_ASCII_ULTIMO_DECIMAL + 1))
    elif (opcoesAscii.get(numeroAleatorio) == 'ESPECIAIS_I'):
      caractere = chr(randrange(CARACTERES_ESPECIAIS_PARTE_I_ASCII_INICIO, CARACTERES_ESPECIAIS_PARTE_I_ASCII_FIM + 1))
    elif (opcoesAscii.get(numeroAleatorio) == 'ESPECIAIS_II'):
      caractere = chr(randrange(CARACTERES_ESPECIAIS_PARTE_II_ASCII_INICIO, CARACTERES_ESPECIAIS_PARTE_II_ASCII_FIM + 1))
    senha[indice] = caractere
  Senha = "".join((senha))
  return Senha

switcher = {
        "a": gerarSenhasTipo1,
        "A": gerarSenhasTipo1,
        "b": gerarSenhasTipo1,
        "B": gerarSenhasTipo1,
        "c": gerarSenhasTipo3,
        "C": gerarSenhasTipo3,
        "d": gerarSenhasTipo4,
        "D": gerarSenhasTipo4,
        "e": gerarSenhasTipo5,
        "E": gerarSenhasTipo5,
    }
 
 
def tipoParaFuncao(tipo):
    func = switcher.get(tipo, "nenhum tipo")
    return func

def geraSenha(Tipo, Tam):
  gerarSenhasPorTipo = tipoParaFuncao(Tipo)
  senha = gerarSenhasPorTipo(Tam)
  return senha


def iniciarPrograma():
  global tipoGlobal
  global totalGlobal

  leiaTipoSenha() 
  
  listaMatriculas = leiaArquivo(arquivoEntrada) 

  for matricula in listaMatriculas:
    senha = geraSenha(tipoGlobal, totalGlobal)
    listaSenhas.append(str(matricula) + ';' + str(senha) + ';')

  regitrarArquivo(nomeDoArquivoSaida, listaSenhas)

iniciarPrograma()
# Helena Kuchinski Ferreira 
# Hiudy Martinhago Carvalho
# Loise Andruski Farion
# Grupo Projeto Compilador 1

from collections.abc import Container
from pyparsing import nestedExpr
from functools import reduce
import sys

def verificaComandosEspeciais(listaArquivo):
  for item in listaArquivo:
    if isinstance(item, list):
      if verificaComandosEspeciais(item):
        return True
    elif isinstance(item, str) and (item == 'RES' or item == 'MEM'):
      return True
  return False

def operacao(A, B, conta):
  if conta == '+':
    return A + B
  elif conta == '-':
    return A - B
  elif conta == '*':
    return A * B
  elif conta == '|':
    if B != 0:
      return A / B
    else:
      raise ValueError("Divisão por zero não é válida!")
  elif conta == '/':
    if B != 0:
      return A // B
    else:
      raise ValueError("Divisão por zero não é válida!")
  elif conta == '%':
    return A % B
  elif conta == '^':
    if type(B) != int:
      B = int(B)
    if B < 0:
      B = abs(B)
    return pow(A, B)
  else:
    raise ValueError("Operador não suportado")

def resolvendoOperacoes(listaOperacoes, listaResultado, MEM):
  for i in range(len(listaOperacoes)): 
    temComandoEspecial = verificaComandosEspeciais(listaOperacoes[i])
    if temComandoEspecial:
      listaEspTemp = listaOperacoes[i]
      
      for x in range(len(listaEspTemp)):
        if isinstance(listaEspTemp[x], list):
          temFuncaoNRes = any(isinstance(item, float) or item == 'RES' for item in listaEspTemp[x])
          
          if temFuncaoNRes:
            funcaoNRes = resolvendoExpressoes(listaEspTemp)
            indice = int((len(listaResultado) - listaEspTemp[x][0]))
            funcaoNRes = listaResultado[indice]
            listaEspTemp[x] = funcaoNRes
            listaOperacoes[i] = listaEspTemp
            VMEM = resolvendoExpressoes(listaOperacoes[i])
            MEM = VMEM
            listaOperacoes[i] = VMEM
            listaOperacoes.remove(VMEM)
            listaResultado.append(VMEM)
            
        else:
          for n in range(len(listaOperacoes[i])):

            if listaOperacoes[i][n] == 'MEM':
              listaOperacoes[i][n] = MEM
              resolucao = resolvendoExpressoes(listaOperacoes[i])
              listaOperacoes[i] = resolucao
              listaOperacoes.remove(resolucao)
              listaResultado.append(resolucao)
              resolvendoOperacoes(listaOperacoes, listaResultado, MEM)
              return listaResultado
              
            if listaOperacoes[i][n] == 'RES':
              indice = int((len(listaResultado) - listaOperacoes[i][0]))
              funcaoNRes = listaResultado[indice]
              listaEspTemp = funcaoNRes
              listaOperacoes[i] = listaEspTemp
              listaOperacoes.remove(listaEspTemp)
              listaResultado.append(listaEspTemp)
              resolvendoOperacoes(listaOperacoes, listaResultado, MEM)
              return listaResultado

    elif type(listaOperacoes[i]) is list and len(listaOperacoes[i]) == 3:
      listaTemp = listaOperacoes[i]
      for j in range(len(listaTemp)):
        if isinstance(listaTemp[j], list):
          if type(listaTemp[j][0]) is float and type(listaTemp[j][1]) is float:
            resolucao = resolvendoExpressoes(listaTemp[j])
            listaTemp[j] = resolucao
            
        else:
          if isinstance(listaTemp[1], list):
            if type(listaTemp[0]) is float and type(listaTemp[1]) is float:
              resolucao = resolvendoExpressoes(listaTemp[j + 1])
              listaTemp[j][1] = resolucao
              
          else:
            resolucao = resolvendoExpressoes(listaTemp)
            listaOperacoes[i] = resolucao
            listaOperacoes.remove(resolucao)
            listaResultado.append(resolucao)
            resolvendoOperacoes(listaOperacoes, listaResultado, MEM)
            return listaResultado
            
    elif type(listaOperacoes[i][0]) is float and type(
        listaOperacoes[i][1]) is float:
      resolucao = resolvendoExpressoes(listaOperacoes[i])
      listaOperacoes[i] = resolucao
      listaOperacoes.remove(resolucao)
      listaResultado.append(resolucao)


def resolvendoExpressoes(lista):
  resultado = None
  operadores = ['+', '-', '*', '|', '/', '%', '^']
  operadorLocalizado = False

  for j in range(len(lista)):
    if lista[j] == 'MEM':
      if isinstance(lista[j - 1], float):
        resultado = lista[j - 1]
        break
    elif lista[j] in operadores:
      if operadorLocalizado:
        raise ValueError("Operação inválida")

      resultado = operacao(float(lista[j - 2]), float(lista[j - 1]), lista[j])
      operadorLocalizado = True

  return resultado

def tipoFloat(listaArquivo):
  listaArquivoFloat = list()
  for i in listaArquivo:
    if isinstance(i, str):
      try:
        listaArquivoFloat.append(float(i))
      except ValueError:
        listaArquivoFloat.append(i)
    elif isinstance(i, list):
      listaArquivoFloat.append(tipoFloat(i))
    else:
      listaArquivoFloat.append(i)
  return listaArquivoFloat

def _main_(nomeArquivo):
  MEM = 0
  nomeArquivo = nomeArquivo.lower()
  if not nomeArquivo.endswith(".txt"):
    nomeArquivo += ".txt"
  try:
    arquivoTxt = open(nomeArquivo, "r")
    linhas = arquivoTxt.readlines()
  except:
    print("Erro ao abrir o arquivo")

  operacoes = []
  resultados = []
  for i in linhas:
    if ',' in i:
      i = i.replace(',', '.')
    operacoes.extend(nestedExpr('(', ')').parseString(i).asList())

  operacoesContas = tipoFloat(operacoes)
  resolvendoOperacoes(operacoesContas, resultados, MEM)

  for i in range(len(linhas)):
    linhaFormatada = linhas[i].strip().replace(',', '.')
    if not linhaFormatada:
      continue  
    print('->', linhaFormatada, ' = ', round(resultados[i], 2))
  arquivoTxt.close()
      
nomeArquivo = sys.argv[1]
_main_(nomeArquivo)

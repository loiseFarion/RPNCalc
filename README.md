# PROJETO CALCULADORA - FASE 1 - A

Este é um programa desenvolvido em Python para solucionar expressões aritméticas em notação RPN. O programa realia a leitura das expressões em um arquivo txt e realiza o calculo das expressões. As expressões realiza adição, subtração, mutiplicação, divisão real, divisão de inteiros, resto da divisão de inteiros, potenciação e três comandos especiais sendo eles: (N RES), (V MEM) e (MEM).

## Operações em notação RPN
  ->  A e B representam números reais

  a) Adição:+, no formato (A B +);
  b) Subtração: - no formato (A B -) ;
  c) Multiplicação: * no formato (A B *);
  d) Divisão Real: | no formato (A B |);
  e) Divisão de inteiros: / no formato (A B /);
  f) Resto da Divisão de Inteiros: % no formato (A B %);
  g) Potenciação: ^ no formato (A B ^);

### Comandos Especiais
  a) (N RES): devolve o resultado da expressão que está N linhas antes, onde N é um número inteiro não negativo; 
  b) (V MEM): armazena um valor, V, em um espaço de memória chamado de MEM, capaz de armazenar um valor real; 
  c) (MEM): devolve o valor armazenado na memória. Se a memória não tiver sido usada anteriormente devolve o número real zero. Cada arquivo de textos é um escopo de aplicação.

### Observações adicionais de requisitos
  Use o ponto para indicar a vírgula decimal.
  O expoente da operação de potenciação será sempre um inteiro positivo.
  As expressões indicadas podem ser aninhadas para a criação de expressões compostas.
  O programa deverá ser executado recebendo como argumento, na linha de comando, o nome do arquivo de teste.

## Executando o Programa
  A execução do programa pode ser feita da seguinte forma:

  --- Replit Shell
    python main.py nomeArquivoTeste

  É necessário substituir 'nomeArquivoTeste' pelo nome do arquivo que deseja solucionar.

## Exemplo de execução
### Arquivo txt
  Nome arquivo txt: 'calculos'
  Conteúdo do arquivo txt: (2 2 +)
                           (3 (1 2 *) *)
                           (16 (2 2 ^) /)
                           ((9 5 *) 10 +)
                           ((3 2 ^) (2 2 ^) *)
### Execução do programa
  --- Replit Shell
  python main.py 'calculos'

### Resultado da execuçã do programa
  Os resultados das expressões contidas no arquivo 'calculos.txt' serão apresentadas no formato '-> expressão = X', onde 'expressão' é o cálculo realizado e 'X' o resultado do cálculo.

  --- Replit
  -> (2 2 +) = 4.0
  -> (3 (1 2 *) *) = 6.0
  -> (16 (2 2 ^) /) = 4.0
  -> ((9 5 *) 10 +) = 55.0
  -> ((3 2 ^) (2 2 ^) *) = 36.0
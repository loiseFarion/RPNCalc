# CALCULATOR PROJECT - PHASE 1 - A

This is a Python program developed to solve arithmetic expressions in Reverse Polish Notation (RPN). The program reads expressions from a .txt file and performs the calculations. The expressions involve addition, subtraction, multiplication, real division, integer division, integer division remainder, exponentiation, and three special commands: (N RES), (V MEM), and (MEM).

## Operations in RPN Notation
  -> A and B represent real numbers

  a) Addition: +, in the format (A B +);<br>
  b) Subtraction: -, in the format (A B -);<br>
  c) Multiplication: *, in the format (A B *);<br>
  d) Real Division: |, in the format (A B |);<br>
  e) Integer Division: /, in the format (A B /);
  f) Integer Division Remainder: %, in the format (A B %);<br>
  g) Exponentiation: ^, in the format (A B ^);<br>

### Special Commands
  a) (N RES): returns the result of the expression that is N lines before, where N is a non-negative integer;<br>
  b) (V MEM): stores a value, V, in a memory space called MEM, which can store a real value;<br>
  c) (MEM): returns the value stored in memory. If the memory has not been used before, it returns the real number zero. Each text file is an application scope.<br>

### Additional Requirements and Observations
  - Use a period to indicate the decimal point.<br>
  - The exponent in the exponentiation operation will always be a positive integer.<br>
  - The expressions may be nested to create compound expressions.<br>
  - The program should be executed by passing the name of the test file as an argument in the command line.<br>

## Running the Program
  The program can be run as follows:

  --- Replit Shell
    python main.py testFileName

  You need to replace 'testFileName' with the name of the file you want to solve.

## Example of Execution
### Text File
  Text file name: 'calculations'
  Content of the text file:
  (2 2 +)<br>
  (3 (1 2 *) *)<br>
  (16 (2 2 ^) /)<br>
  ((9 5 *) 10 +)<br>
  ((3 2 ^) (2 2 ^) *)<br>

### Running the Program
  --- Replit Shell
  python main.py 'calculations'

### Program Execution Result
  The results of the expressions in the 'calculations.txt' file will be presented in the format '-> expression = X', where 'expression' is the calculation performed, and 'X' is the result of the calculation.

  --- Replit<br>
  -> (2 2 +) = 4.0<br>
  -> (3 (1 2 *) *) = 6.0<br>
  -> (16 (2 2 ^) /) = 4.0<br>
  -> ((9 5 *) 10 +) = 55.0<br>
  -> ((3 2 ^) (2 2 ^) *) = 36.0v

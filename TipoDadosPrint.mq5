//+------------------------------------------------------------------+
//|                                                   HelloWorld.mq5 |
//|                                                        SrJohn369 |
//|                                     https://github.com/SrJohn369 |
//+------------------------------------------------------------------+
#property copyright "SrJohn369"
#property link      "https://github.com/SrJohn369"
#property version   "1.00"
//--- Parâmetros

//--- Vars Global

//+------------------------------------------------------------------+
//| Função de inicio                                                 |
//+------------------------------------------------------------------+
void OnStart() {
   //--- TIPOS CHAR UCHAR SHORT USHORT INT UINT LONG ULONG
   char var_ch = -12;
   /* O tipo char usa 1 byte de memória (8 bits) e permite expressar em
    notação binária 2^8=256 valores. O tipo char pode conter tanto
   valores positivos quanto negativos. A faixa de valores é de -128
     a 127.*/
   uchar var_uch = 34;
   /*O tipo inteiro uchar também ocupa 1 byte de memória, assim como o
   tipo char , mas diferente dele uchar é destinado apenas para valores
   positivos. O valor mínimo é zero, o valor máximo é 255. A primeira
   letra u no nome do tipo uchar é abreviatura de unsigned (sem sinal).*/
   short var_sh = 30789;
   /*O tamanho do tipo short é de 2 bytes (16 bits) e, conseqüentemente,
   ele permite expressar a faixa de valores igual a 2 elevado a 16:
   2^16 = 65 536. Como o tipo short é um tipo com sinal, e contém tanto
   valores positivos quanto negativos, a faixa de valores é entre
   -32 768 e 32 767.*/
   ushort var_ush = 60001;
   /*O tipo short sem sinal é o tipo ushort, que também tem 2 bytes de
   tamanho. O valor mínimo é 0, o valor máximo é 65 535.*/
   int var_int = 2100999777;
   /*O tamanho do tipo int é de 4 bytes (32 bits). O valor mínimo é
   -2 147 483 648, o valor máximo é 2 147 483 647.*/
   uint var_uint = 3090999555;
   /*O tipo integer sem sinal é uint. Ele usa 4 bytes de memória e
   permite expressar inteiros de 0 a 4 294 967 295.*/
   long var_long = 9000000000000000000;
   /*O tamanho do tipo long é de 8 bytes (64 bits). O valor mínimo
   é -9 223 372 036 854 775 808,
   o valor máximo é 9 223 372 036 854 775 807.*/
   ulong var_ulong = 18000000000000000000;
   /*O tipo ulong também ocupa 8 bytes e pode armazenar valores
   de 0 a 18 446 744 073 709 551 615.*/
   //--- TIPO BOOLEAN
   /*O tipo bool é destinado para armazenar os valores lógicos true
   ou false, a representação numérica deles é 1 ou 0,
   respectivamente.*/
   bool valorBool_1 = true;
   bool valorBool_2 = false;
   bool valorBool_3 = 1; // true
   bool valorBool_5 = 34; // true
   bool valorBool_4 = 0; // false
   //--- TIPO STRING
   /*O tipo string é usado para armazenar cadeias de texto. Uma
   cadeia de texto é uma seqüência de caracteres no formato Unicode
   com zero no final do mesmo. Uma constante string pode ser atribuída
   a uma variável string. Uma constante string é uma seqüência de
   caracteres entre aspas duplas: "This is a string constant".
   Se for preciso incluir um aspas duplo (") em uma string, a barra
   invertida (\) deve ser colocada antes dele. Quaisquer constantes
   de caractere especial podem ser escritos em uma string, se a barra
   invertida (\) for digitada antes deles.*/
   string str_pais = "Brasil";
   string str_pais_citacao = "Brasil \"terra de ladrão\"";
   //--- outros arquivos serão criados para explorar melhor isso
   //--- TIPOS REAIS (double, float)
   /*Tipos Reais (double, float)

   Tipos Reais (ou tipos de ponto flutuante) representam valores com
   um parte fracionária. Na linguagem MQL5 existem dois tipos para
   números de ponto flutuante. O método de representação dos números
   reais na memória do computador é definido pelo padrão IEEE 754 e é
   independente de plataformas, sistemas operacionais ou linguagens
   de programação.*/
   //--- double
   /* Tipo de número real double ocupa 64 bits (1 bit de sinal,
   11 bits de expoente e 52 bits de mantissa).*/
   double var_double = 5.785455345; // Double é MAIS preciso do que float
   //--- float
   /*Tipo de número real float ocupa 32 bits (1 bit de sinal, 8 bits
   de expoente e 23 bits de mantissa).*/
   float var_float = 45.9054; // Float é MENOS preciso do que Double
   //--- TIPO COLOR
   /* O tipo color é destinado para armazenar informações sobre cor
   e ocupa 4 bytes na memória. O primeiro byte é ignorado, os
   restantes 3 bytes contém os componentes RGB.*/
   //--- TIPO DATETIME
   /*O tipo datetime é destinado a armazenar data e hora como o número
   de segundos decorridos desde 01 de Janeiro de 1970. Este tipo
   ocupa 8 bytes de memória.*/
   /*Constantes de data e hora podem ser representados como string
   literal, que consiste de 6 partes mostrando o valor numérico do
   ano, mês, dia (ou dia, mês, ano), horas, minutos e segundos. A
   constante é colocado entre aspas simples e começa com o
   caractere D.*/
   /*Os valores variam de 1 de Janeiro de 1970 a 31 de Dezembro de 3000.
   Tanto a data (ano, mês, dia)
   quanto a hora (horas, minutos, segundos),
   ou ambos podem ser omitidos.*/
   datetime NY = D'2015.01.01 00:00';     // Data Hora de começo do ano 2015
   datetime d1 = D'1980.07.19 12:30:27';  // Ano Mês Dia Horas Minutos Segundos
   datetime d2 = D'19.07.1980 12:30:27';  // Igual a D'1980.07.19 12:30:27';
   datetime d3 = D'19.07.1980 12';        // Igual a D'1980.07.19 12:00:00'
   datetime d4 = D'01.01.2004';           // Igual a D'01.01.2004 00:00:00'
   datetime compilation_date=__DATE__;             // Data de Compilação
   datetime compilation_date_time=__DATETIME__;    // Data e Hora de Compilação
   datetime compilation_time=__DATETIME__-__DATE__;// Hora de Compilação
   //--- Exemplos de declarações após o qual avisos do compilador serão retornados
   datetime warning1 = D'12:30:27';       // Igual a D'[data de compilação] 12:30:27'
   datetime warning2 = D'';               // Igual a __DATETIME__
}
//+------------------------------------------------------------------+
//|Funções de uso                                                    |
//+------------------------------------------------------------------+

//+------------------------------------------------------------------+
//+------------------------------------------------------------------+

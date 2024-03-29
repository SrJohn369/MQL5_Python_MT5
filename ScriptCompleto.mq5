//+------------------------------------------------------------------+
//|                                                   HelloWorld.mq5 |
//|                                                        SrJohn369 |
//|                                     https://github.com/SrJohn369 |
//+------------------------------------------------------------------+
#property copyright "SrJohn369"
#property link      "https://github.com/SrJohn369"
#property version   "1.00"
#property script_show_inputs // Apresenta janela de parâmetros
//--- Parâmetros
input int INP_vezes = 10;
//--- Vars Global
string nome = "Maria";
//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart() {
   imprimeNome();
   printf("Finalizado...");
}
//+------------------------------------------------------------------+
void imprimeNome() {
   for(int i=0; i<INP_vezes; i++) {
      printf("Repedindo %s pela %s vez", nome, IntegerToString(i+1)+"ª");
   }
}
//+------------------------------------------------------------------+

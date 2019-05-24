Instruções para execução do código em que verifica tempo de atividade entre uma maquina virtual maquina real. 

 O código consiste em um exemplo de comparação entre os algoritmos de ordenação, o partição tem é baseado no princípio da "dividir para conquistar" e com versoes probabilísticas apresentados na disciplina Análise do Algoritmo 

Baixar ou clonar a pasta contendo o util do arquivo

Pasta  Milton
2013: Orientações
Trabalho em grupo: Desempenho de máquina virtual.doc.


#########################

*Aaron, Antonio, Danny e Jessica*

#########################


**Tema**: Instalação e testes em **máquina virtual**.
Referências: Material no repositório: \\sever\Milton  
(server2000; vmware)
HTTP://download.virtualbox.org/virtualbox/4.2.4/VirtualBox-4.2.4-81684-win.exe
     
Regras para o trabalho.
1- Relatório similar a um trabalho de PESQUISA conforme modelo do Simpósio em Congresso.
O nome dos participantes estará no corpo do trabalho.
A parte formal do trabalho terá peso 50%. Isto significa seguir a confecção do texto como o modelo de simpósio. Também inclui apresentar a máquina virtual em operação. 
2– A introdução deverá contemplar uma análise de porque usar máquina virtual. Uma comparação com outras formas de uso, exemplo: Vantagens/desvantagens de instalações de sistemas em Sistemas Operacionais antigos em máquinas virtuais, testes de softwares, operações arriscadas. Este item terá peso 20%.
4 - O corpo do trabalho deverá mostrar a instalação com um software de desenvolvimento para programação de um loop para realizar uma tarefa qualquer que “gaste tempo de CPU”, por exemplo em Pascal: 
For i:= 1 to ni do 
For j:= 1 to nj do 
For k:= 1 to nk do 
C:=exp(9);
Ni=310=nj=nk   310*310*310= 27 000 000 (10seg)
No. instruções    tempo
(em milhões)
27                         10
30                          12
32                         15
34
35
bt.fatecsp.br



/* Faça algo: cálculo, texto; ...Livre */


O valor final do loop deverá ser suficientemente grande e mensurável para “gastar” algumas dezenas de segundo.
O teste deverá contemplar pelo menos sete valores diferentes de ni* nj nk (que está associado ao tempo de execução) e verificar o comportamento do produto ni nj *nk  e o tempo gasto na execução do loop;

Verifique  se há linearidade no comportamento, isto é se o tempo de execução está diretamente relacionado à quantidade de instruções realizadas (ao valor de n). 
Estes testes deverão ser realizados no ambiente virtual e ambiente de máquina host, e deverão ser comparados para comparação de desempenho.
Montar a forma representação destes dados (tabela e gráfico). Peso 30%.

ni* nj *nk
Tempo (máquina real)
Tempo (máquina virtual)
1
27 000 000
10
10
2
30 000 000 
15
15
3



4



5



6



7



8



9



10



Executar na maq. Virtual    
Executar na maq.  REAL       comparar os desempenhos   para gerar o relatório


5 – A corpo do trabalho, conclusão e bibliografia terão peso 30%. A bibliografia deverá conter nome de livros conforme padrão, assim como referências de internet (não somente wikipedia). A conclusão será baseada nos resultados obtidos nos testes de desempenho do programa 

Dicas para a realização do trabalho

1 - Instalem um software de programação: Pascal,  C, assembly, ou outro compilador a sua escolha

3 – Sugestão de programa com loop encadeado. Exemplo:
Var i,j,k: integer;   c:real;
Begin
Write(‘inicio’);
For i:= 1 to 300 do     {o valor 300 define o tempo de execução}
For j:= 1 to 300 do                      {ajustar o valor final para obter tempos diferentes}
For k:= 1 to 300 do  
c:= 2^3;                                         {pode implementar outras operações}
write(‘fim’); 
readln;
end.
	

5 - Analisar os tempos gastos pelo programa operando no ambiente host e no convidado. Faça preferencialmente um gráfico para comparar os desempenhos
 
A introdução e as conclusões são feitas no final do trabalho
6 - Bibliografia. Faça à medida que for consultando.
7 - NÃO faça referência apenas da wikipedia. Inclua livros e mais referências em internet.
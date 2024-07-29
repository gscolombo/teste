# Desenvolvimento de Soluções

## Introdução

A atividade será dividida em duas partes: uma **teórica** que está detalhada na primeira questão e uma **prática** que consiste na aplicação prática dos conceitos discutidos.

## Primeira questão
Dentro do que você atua e conhece, apresente uma solução para o cliente de uma aplicação, podendo ser web com o intuito de ser um **simulador de compras**. O seu fluxo deve se basear respectivamente em três etapas: coleta de informações de um cliente fictício por meio de perguntas, busca no banco de dados das informações necessárias, tratamento desses dados.

> Para o envio desta atividade faça um fork deste respositório e escreva a solução na pasta respostas no arquvio `primeiraQuestao.txt`


## Segunda questão

### a) Informações do cliente

A coleta de informações é uma parte muito importante em um simulador de compras, para isso é necessário obter estas informações do usuário:

- Nome;
- E-mail;
- Valor de interesse(valor bem).

Para garantir que o processo ocorreu como esperado, envie um e-mail notificando o usuário das informações que serão analisadas.

> É importante que essas informações sejam armazenadas no banco de dados.

### b) Busca no Banco de Dados
Com as informações obtidas na etapa anterior, é necessário fazer uma filtragem no banco de dados (estão na forma de um arquivo .csv) para encontrar quais são os valores interessantes para o cliente. Dessa forma, deve-se encontrar grupos que estão entre `valorDeInteresse ≤ valorDoBanco ≤ 1.1 * valorDeInteresse`.

### Extra

Para realizar testes de informações pode-se utilizar estes dados:

- Nome: Fábio;
- E-mail: fabio.kikuti@azconex.com.br;
- Valor de interesse (valor bem): R$: 130.000,00.


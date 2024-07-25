# Desenvolvimento de Soluções

## Introdução
Desenvolva uma aplicação web com o intuito de ser um simulador de compras. O seu fluxo deve se basear respectivamente em três etapas: coleta de informações de um cliente fictício por meio de perguntas, busca no banco de dados das informações necessárias, tratamento desses dados.


## Detalhamento

### Informações do cliente
Para a coleta de informações é necessário obter do usuário:

- Nome;
- Telefone;
- Valor de interesse.

> É importante que essas informações sejam armazenadas no banco de dados.

### Busca no Banco de Dados
Nesta etapa é necessário fazer uma filtragem no banco de dados (estão na forma de um .csv) para encontrar quais são os valores interessantes para o cliente. Dessa forma, deve-se encontrar grupos que estão entre `valorDeInteresse ≤ valorDoBanco ≤ 1.1 * valorDeInteresse`.

### Tratamento dos dados 
Já com as informações filtradas do Banco de Dados, será necssário fazer três filtros para apresentar ao usuário final:

- Maior prazo;
- Menor parcela;
- Menor porcentagem de contemplação.

> Essas informações precisam ser mostradas para o cliente da maneira que for melhor.


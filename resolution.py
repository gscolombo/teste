import csv

# Função para filtrar os dados
def filtrar_valores_interessantes(arquivo_csv, valorDeInteresse):
    """ Leitura das informações e armazenamento na lista """
    
    valores_interessantes = []

    with open(arquivo_csv, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Ler o cabeçalho, se houver
        
        for linha in reader:
            # Supondo que a coluna de interesse seja a primeira (índice 0)
            # print(linha[7].index(","))
            # linha[7].remove(",")
            # print(linha[7])
            # break
            valorDoBanco = float(linha[7])  # Converter para float
            
            # Verificar se o valorDoBanco está no intervalo desejado
            if valorDeInteresse <= valorDoBanco <= 1.1 * valorDeInteresse:
                valores_interessantes.append(valorDoBanco)

    return valores_interessantes

# Exemplo de uso
arquivo_csv = 'banco.csv'
valorDeInteresse = 1000  # Valor de interesse definido pelo cliente
valores_interessantes = filtrar_valores_interessantes(arquivo_csv, valorDeInteresse)

# Exibir os resultados
print("Valores interessantes encontrados:")
for valor in valores_interessantes:
    print(valor)

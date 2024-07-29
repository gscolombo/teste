import csv
# Função para filtrar os dados
import pandas as pd


def filtrar_valores_interessantes(arquivo_csv, valorDeInteresse):
    """ Leitura das informações e armazenamento na lista. """

    # Criação das listas
    valores_interessantes = []
    grupo_atual = []

    with open(arquivo_csv, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Ler o cabeçalho, se houver

        for linha in reader:
            # Definindo as informações
            grupo = linha[0]
            valor = linha[7]
            parcela = linha[8]
            contemplacao = linha[11]

            # Converter para float e formatando
            valorDoBanco = float(valor.replace(",", ""))

            # Verificar se o valorDoBanco está no intervalo desejado
            if (valorDeInteresse <= valorDoBanco and valorDeInteresse * 1.1 >= valorDoBanco):
                # todas as informações desejadas estão o no grupo atual
                grupo_atual = [grupo, valor, parcela, contemplacao]
                valores_interessantes.append(grupo_atual)

        if valores_interessantes:
            return valores_interessantes
        else:
            return None


def main():
    # Exemplo de uso
    arquivo_csv = 'banco.csv'
    valorDeInteresse = 130000  # Valor de interesse definido pelo cliente
    valores_interessantes = filtrar_valores_interessantes(
        arquivo_csv, float(valorDeInteresse))

    # Exibir os resultados
    if valores_interessantes != None:
        print("Valores interessantes encontrados:")
        for dado in valores_interessantes:
            print(dado)
        
        # Adicionando ao arquivo csv
        df = pd.DataFrame(valores_interessantes, columns=['Grupo', 'Valor', 'Parcela', 'Contemplação'])
        df.to_csv('output.csv', index=False)
    else:
        print("Valores não encontrados")

if __name__ == "__main__":
    main()

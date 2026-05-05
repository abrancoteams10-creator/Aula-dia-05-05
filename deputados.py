import csv

def carregar_deputados(caminho_arquivo):
    deputados = []
    with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            deputados.append(linha)
    return deputados

def listar_por_estado(deputados, estado):
    encontrados = [d for d in deputados if d['estado'].lower() == estado.lower()]
    
    if not encontrados:
        print(f"Nenhum deputado encontrado para o estado: {estado}")
    else:
        print(f"\nDeputados do estado {estado}:")
        for d in encontrados:
            print(f"- {d['nome']}")

def main():
    caminho = "deputados_2022.csv"
    deputados = carregar_deputados(caminho)

    while True:
        estado = input("\nDigite a sigla do estado (ou 'sair' para encerrar): ")
        
        if estado.lower() == 'sair':
            break
        
        listar_por_estado(deputados, estado)

if __name__ == "__main__":
    main()



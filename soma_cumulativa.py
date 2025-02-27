def soma_cumulativa(lista):
    resultado = []
    soma = 0
    for numero in lista:
        soma += numero
        resultado.append(soma)
    return resultado

def main():
    print("Bem-vindo ao calculador de soma cumulativa!")
    print("Digite os números que deseja somar, separados por espaço.")
    
    while True:
        entrada = input("\nDigite os números (ou 'sair' para encerrar): ")
        
        if entrada.lower() == "sair":
            print("Encerrando o programa...")
            break
        
        try:
            lista_numeros = list(map(int, entrada.split()))
        except ValueError:
            print("Entrada inválida! Certifique-se de digitar apenas números inteiros.")
            continue
        
        resultado = soma_cumulativa(lista_numeros)
        
        print("A soma cumulativa da lista é:", resultado)

if __name__ == "__main__":
    main()

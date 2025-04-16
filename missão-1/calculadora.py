def calculadora(operacao, num1, num2):
    num1 = float(num1)
    num2 = float(num2)
    if operacao == 'soma':
        return num1 + num2
    elif operacao == 'subtracao':
        return num1 - num2
    elif operacao == 'multiplicacao':
        return num1 * num2
    elif operacao == 'divisao':
        if num2 == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return num1 / num2
    else:
        raise ValueError("Operação inválida. Use 'soma', 'subtracao', 'multiplicacao' ou 'divisao'.")

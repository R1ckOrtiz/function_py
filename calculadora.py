def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y

def calculadora():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        escolha = input("Digite sua escolha (1/2/3/4): ")

        if escolha in ['1', '2', '3', '4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")

            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")

            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")

            elif escolha == '4':
                resultado = dividir(num1, num2)
                if isinstance(resultado, str):
                    print(resultado)
                else:
                    print(f"Resultado: {num1} / {num2} = {resultado}")

        else:
            print("Escolha inválida. Por favor, tente novamente.")

        # Pergunta ao usuário se ele quer realizar outra operação
        continuar = input("Deseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Encerrando a calculadora. Até mais!")
            break

if __name__ == "__main__":
    calculadora()

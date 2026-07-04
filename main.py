## Aqui é uma espécie de menu, mostrando o que fazer e perguntando a entrada do usuário
print("== Calculadora ==")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - DIvisão")
operacao = int(input("Escolha uma opção: "))

## Aqui, o sistema pede os números que serão usados na operacao escolhida
num1 = float(input("Primeiro número  -> "))
num2 = float(input("Segundo número -> "))

## Aqui ele realiza as operações de acordo com a escolha do usuário
if(operacao == 1):
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif(operacao == 2):
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif(operacao == 3):
    resultado = num1 * num2
    print(f"{num1} x {num2} = {resultado}")
elif(operacao == 4):
    resultado = num1 / num2
    print(f"{num1} : {num2} = {resultado}")
else: ## Se uma operação inválida for escolhida, ele trata o erro
    print("Operação inválida!")
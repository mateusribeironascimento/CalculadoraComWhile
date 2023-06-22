print(f'{"Calculadora While":.^25}')
print('-' * 25)
while True:
    sair = input('Deseja fazer uma conta? ').upper().strip()[0]
    if sair == 'N':
        break
    else:
        print('-' * 25)
        entrada1 = input('Digite o primeiro valor: ')
        entrada2 = input('Digite o segundo valor: ')
        try:
            valor1 = float(entrada1)
            valor2 = float(entrada2)
            print('-' * 25)
            operador = int(input('Qual operação você deseja?'
                                 '\n[1] Somar'
                                 '\n[2] Subtrair'
                                 '\n[3] Multiplicar'
                                 '\n[4] Dividir'
                                 '\nSua opção: '))
            if operador == 1:
                print(f'A soma dos valores é {valor1 + valor2}')
            elif operador == 2:
                print(f'A subtração dos valores é {valor1 - valor2}')
            elif operador == 3:
                print(f'A multiplicação dos valores é {valor1 * valor2}')
            elif operador == 4:
                print(f'A divisão dos valores é {valor1 / valor2}')
            else:
                print('Operador inválido, digite de 1 a 4.')
            print('-' * 25)
        except:
            print('Você não digitou um número')
            continue
print('-' * 25)
print('Obrigado. Volte sempre!')
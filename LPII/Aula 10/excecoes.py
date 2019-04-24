print("Vamos dividir 5 por um número digitado")
while True:
    try:
        while True:
            try:
                n = input('Entre com um número inteiro')
                x= int(n)
                break
            except ValueError:
                print('Não é um inteiro!Tente novamente')
        
        resposta= 5/x
        print('O resultado de 5 dividido por',x,' é: ',resposta)
        break
    except ZeroDivisionError:
        print('\n--------------------------------')
        print("|Nenhum número é divisível por 0!|\n --------------------------------")
        

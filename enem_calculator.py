import os

clear = lambda: os.system('cls')
clear()

print('#### Bem vindo a calculadora da nota do ENEM ####')
repeat = True

while repeat:
    print('\n' * 5 + "Escreva suas notas na seguinte ordem:\nlinguagens, Ciencias Humanas, Ciencias da Natureza, " +
          'Matemática, Redação')
    print('\nPor exemplo:\n605, 707.8, 625, 749, 640')
    scores = input('\nSuas notas:\n')

    print(('\n' * 5 + 'Agora coloque o peso de cada matéria na mesma ordem'))
    print('\nPor exemplo:\n2, 1, 1, 2, 2')
    weights = input('\nPesos:\n')

    try:
        scores = scores.replace(',', ' ').split()
        weights = weights.replace(',', ' ').split()

        for c, i in enumerate(weights):
            weights[c] = float(i)

        for c, i in enumerate(scores):
            scores[c] = float(i)

        weights_sum = [sum(digit for digit in weights)]
        multiplication = 0

        for j, k in zip(weights, scores):
            multiplication += j*k

        final_score = multiplication/weights_sum[0]
        print('\n' * 5 + f'Sua nota final é: {final_score}' + '\n' * 5)
        check = input('Gostaria de calcular novamente?(s ou n): ')

        if 's' in check:
            print('\n'*10)
            repeat = True

        else:
            repeat = False

    except:
        clear()
        print('Valores inseridos incorretamente, por favor tente novamente:')

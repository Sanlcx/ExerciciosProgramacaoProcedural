from string import ascii_uppercase # módulo para gerar alfabeto em letras maiúsculas

letras_digitadas = []

palavra = 'TABASCO'
chances = 3
dica = ''

print('=-' * 30)
print('Jogo da forca. Tente adivinhar a palavra! (Chances: 3)')
print('=-' * 30)
print()
numbers_list = list(str(range(10))) # lista de string dos números 0 a 9 para não deixar o usuário digitar números
alphabet_list = list(ascii_uppercase) # lista do alfabeto para não deixar o usuário digitar caracteres especiais

while True:
    letra_a_ser_digitada = input('Digite uma letra:\n').strip().upper()
    print()
    if len(letra_a_ser_digitada) > 1 or letra_a_ser_digitada in numbers_list or letra_a_ser_digitada not in alphabet_list:
        continue
    if letra_a_ser_digitada in letras_digitadas:
        chances -= 1
        print(f'Digitar uma letra que você já digitou antes também irá diminuir suas chances! Chances restantes: {chances}')
        print()
        if chances == 0:
            print('Você perdeu!')
            break
    letras_digitadas.append(letra_a_ser_digitada)
    letras_digitadas = sorted(set(letras_digitadas))

    if letra_a_ser_digitada not in palavra:
        chances -= 1
        print(f'A palavra secreta não têm essa letra. Chances restantes: {chances}')
        if chances == 0:
            print('Você perdeu!')
            break
    for letra in palavra:
        if letra in letras_digitadas:
            dica += letra
        else:
            dica += '*'
    print(f'palavra: {dica}')
    print()
    print(f'Letras já digitadas: {letras_digitadas}')
    print()
    if dica == palavra:
        print('Parabéns! Você ganhou.')
        break
    dica = ''

from random import randint

cpf = str(randint(100000000, 999999999)) # gerador de valores randômicos de 9 dígitos de 100000000 até 999999999

decrementador = 10 # parte da fórmula para validar CPF
total = 0
while True:
    for i in range(19): # a fórmula para validar CPF necessita fazer uma conta 19 vezes.
        if i > 8:
            i -= 9
        total += int(cpf[i]) * decrementador
        decrementador -= 1
        if decrementador < 2:
            novo_digito = 11 - (total % 11)
            if novo_digito > 9:
                novo_digito = 0
            cpf += str(novo_digito)
            decrementador = 11
            total = 0
    cpf_formatado = cpf[:3] + '.' + cpf[3:6] + '.' + cpf[6:9] + '-' + cpf[9:] # colocar os caracteres '.' e '-' no CPF gerado
    print(cpf_formatado)
    break

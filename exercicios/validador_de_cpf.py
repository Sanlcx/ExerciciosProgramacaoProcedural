from re import sub # módulo para tirar '.' e '-' do CPF e para não deixar o usuário escrever letras
cpf = input('Digite um CPF:\n').strip()
cpf_formatado = sub('[.a-z-]', '', cpf) # tirar '.' e '-' para fazer os cálculos embaixo
cpf_formatado2 = sub('[a-z]', '', cpf) # tirar letras caso o usuário as digite e para apresentar o CPF ao final do script.
novo_cpf = cpf_formatado[:-2] # pegando e excluindo os dois últimos valores do CPF
decrementador = 10 # parte da fórmula para validar CPF
total = 0
while True:
    for i in range(19): # a fórmula para validar CPF necessita fazer uma conta 19 vezes.
        if i > 8:
            i -= 9
        total += int(novo_cpf[i]) * decrementador
        decrementador -= 1
        if decrementador < 2:
            novo_digito = 11 - (total % 11)
            if novo_digito > 9:
                novo_digito = 0
            novo_cpf += str(novo_digito)
            decrementador = 11
            total = 0
    sequencia = str(cpf_formatado[0]) * len(cpf_formatado) == cpf_formatado

    if novo_cpf == cpf_formatado and not sequencia:
        print(f'O CPF {cpf_formatado2} é válido.')
        break
    else:
        print(f'O CPF {cpf_formatado2} NÃO é válido.')
        break

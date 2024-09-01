print("BEM VINDO A LOJA DE GELADOS DO DIEGO OSEKO")
print('-'*20,'Cardapio', '-'*20)
print('TAMANHO  |  CUPUACU (CP) | ACAI (AC) |')
print('   P     |     R$ 9,00   |  R$ 11,00 |')
print('   M     |    R$ 14,00   |  R$ 16,00 |')
print('   G     |    R$ 18,00   |  R$ 20,00 |')
print('-'* 50)
#inicializacao das variaveis
valor = 0  
vT = 0
quant = 0
#estrutura de repeticao do codigo
#teste de erro de input
while True:
    sab = input('Qual o sabor desejado? (CP/AC)')      
    if(sab != 'CP' and sab != 'AC'):
        print('Sabor inválido, tente novamente')
        continue

    tam = input('Qual o tamanho desejado? (P/M/G)')
    if(tam != 'P' and tam != 'M' and tam != 'G'):
        print('Tamanho invalido, tente novamente')
        continue
#atribuicao de valores para cada escolha
    if (sab == 'CP' and tam == 'P'):
        valor = 9
    elif (sab == 'CP' and tam == 'M'):
        valor = 14
    elif (sab == 'CP' and tam == 'G'):
        valor = 18
    elif (sab == 'AC' and tam == 'P'):
        valor = 11
    elif (sab == 'AC' and tam == 'M'):
        valor = 16
    elif (sab == 'AC' and tam == 'G'):   
        valor = 20     

    vT += valor 
    quant += 1
    #escolha de continuacao de execucao
    aesc = input('Deseja pedir mais alguma coisa? (S/N)')
    if(aesc == 'S'):
        continue
    elif(aesc == 'N'):
        break
#print do acumulador
print(f'Total do valor a pagar: {vT} ')
print(quant)

print('Bem vindo a loja de Diego Oseko')
print('DESCONTO ACIMA DE 2500 = 4%')
print('DESCONTO ACIMA DE 6000 = 7%')
print('DESCONTO ACIMA DE 10000 = 11%')
valor = float(input('Qual o valor do produto: '))
quant = int(input('Qual a quantidade do produto: '))
total = valor * quant
totalsdc = total   
#CASO O VALOR SEJA ACIMA OU IGUAL A 10000
if (total >= 10000):
    total = total - (total*0.11) 
#CASO O VALOR SEJA ENTRE 6000 E 10000
elif (total >= 6000 and total < 10000):
    total = total - (total*0.07)
#CASO O VALOR SEJA ENTRE 2500 E 6000
elif (total >= 2500 and total < 6000):
    total = total - (total*0.04)
#VALOR ABAIXO, SEM DESCONTO
else:
    print("não tem desconto")

print(f'total sem Desconto: {totalsdc}')
print(f'total com Desconto: {total}')

